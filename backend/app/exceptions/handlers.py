from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.exceptions.errors import AppException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "status": exc.status_code,
                "message": exc.message,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "status": 422,
                "message": "Validation failed",
                "errors": exc.errors(),
            },
        )

    @app.exception_handler(SQLAlchemyError)
    async def database_exception_handler(
        request: Request,
        exc: SQLAlchemyError,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "status": 500,
                "message": "Database error",
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "status": 500,
                "message": "Internal server error",
            },
        )