from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from models.models import User, XPTransaction
from schemas.schemas import UserResponse, XPTransactionResponse
from utils.auth import get_current_active_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.get("/xp", response_model=int)
async def get_user_xp(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get the total XP for the current user"""
    total_xp = db.query(XPTransaction).filter(
        XPTransaction.user_id == current_user.id
    ).with_entities(
        XPTransaction.amount
    ).all()
    
    return sum([xp[0] for xp in total_xp]) if total_xp else 0

@router.get("/xp/history", response_model=List[XPTransactionResponse])
async def get_xp_history(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get the XP transaction history for the current user"""
    transactions = db.query(XPTransaction).filter(
        XPTransaction.user_id == current_user.id
    ).order_by(
        XPTransaction.created_at.desc()
    ).all()
    
    return transactions
