from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from http import HTTPStatus

from insidegrid.db import get_db
from insidegrid.crud.comment import like_comment, dislike_comment

router = APIRouter()

@router.post("comments/{comment_id}/like_comment", status_code=HTTPStatus.OK)
def add_like_to_comment(comment_id: int, db: Session = Depends(get_db)):
    return like_comment(db, comment_id)
@router.get("user/{user_id}/dislike_comment", status_code=HTTPStatus.OK)
def add_dislike_comment(comment_id: int, db: Session = Depends(get_db)):
    return dislike_comment(db, comment_id)