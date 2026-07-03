from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.offer import (
    OfferCreate,
    OfferResponse,
    OfferUpdate,
)
from app.services.offer_service import OfferService

router = APIRouter(
    prefix="/offers",
    tags=["Offers"],
)


@router.post(
    "",
    response_model=OfferResponse,
)
def create_offer(
    request: OfferCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    try:
        offer = OfferService.create(
            db,
            request,
        )

        if offer is None:
            raise HTTPException(
                status_code=404,
                detail="Interview not found",
            )

        return offer

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[OfferResponse],
)
def get_offers(
    db: Session = Depends(get_db),
):
    return OfferService.get_all(db)


@router.get(
    "/interview/{interview_id}",
    response_model=OfferResponse,
)
def get_offer(
    interview_id: UUID,
    db: Session = Depends(get_db),
):
    offer = OfferService.get_by_interview(
        db,
        interview_id,
    )

    if offer is None:
        raise HTTPException(
            status_code=404,
            detail="Offer not found",
        )

    return offer


@router.put(
    "/{offer_id}",
    response_model=OfferResponse,
)
def update_offer(
    offer_id: UUID,
    request: OfferUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    offer = OfferService.update(
        db,
        offer_id,
        request,
    )

    if offer is None:
        raise HTTPException(
            status_code=404,
            detail="Offer not found",
        )

    return offer


@router.delete(
    "/{offer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_offer(
    offer_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    deleted = OfferService.delete(
        db,
        offer_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Offer not found",
        )

    return None