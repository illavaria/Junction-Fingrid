from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from http import HTTPStatus

from insidegrid.db import get_db
from insidegrid.db.models import Users
from insidegrid.schemas.schemas import UserInputSchema, UserOutputSchema, UserLoginInputSchema, ChangeOutputSchema, ReleaseOutputSchema, ReleaseInputSchema
from insidegrid.crud.user import create_user
from insidegrid.crud.change import get_users_changes, get_subscribed_changes, get_liked_changes, get_disliked_changes
from insidegrid.crud.release import get_liked_releases, get_disliked_releases

router = APIRouter()

@router.post("/user", status_code=HTTPStatus.CREATED, response_model=UserOutputSchema)
def create_new_user(user: UserInputSchema, session: Session = Depends(get_db)):
    return create_user(session, user)

@router.get("/user/{user_id}/changes", status_code=HTTPStatus.OK, response_model=list[ChangeOutputSchema])
def get_user_changes(user_id: int, session: Session = Depends(get_db)):
    return get_users_changes(session, user_id)

@router.get("/user/{user_id}/subscribed_changes", status_code=HTTPStatus.OK, response_model=list[ChangeOutputSchema])
def get_users_subscribed_changes(user_id: int, session: Session = Depends(get_db)):
    return get_subscribed_changes(session, user_id)

@router.get("/user/{user_id}/liked_changes", status_code=HTTPStatus.OK, response_model=list[ChangeOutputSchema])
def get_users_liked_changes(user_id: int, session: Session = Depends(get_db)):
    return get_liked_changes(session, user_id)

@router.get("/user/{user_id}/disliked_changes", status_code=HTTPStatus.OK, response_model=list[ChangeOutputSchema])
def get_users_disliked_changes(user_id: int, session: Session = Depends(get_db)):
    return get_disliked_changes(session, user_id)

@router.get("/user/{user_id}/liked_releases", status_code=HTTPStatus.OK, response_model=list[ReleaseOutputSchema])
def get_users_liked_changes(user_id: int, session: Session = Depends(get_db)):
    return get_liked_releases(session, user_id)

@router.get("/user/{user_id}/disliked_releases", status_code=HTTPStatus.OK, response_model=list[ReleaseOutputSchema])
def get_users_disliked_changes(user_id: int, session: Session = Depends(get_db)):
    return get_disliked_releases(session, user_id)
