from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions.errors import AppException
import traceback


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        ...

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        ...

    @app.exception_handler(SQLAlchemyError)
    async def database_exception_handler(request: Request, exc: SQLAlchemyError):
        traceback.print_exc()     # <-- ONLY ADD THIS LINE

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "status": 500,
                "message": "Database error",
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        traceback.print_exc()     # <-- ONLY ADD THIS LINE

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "status": 500,
                "message": "Internal server error",
            },
        )