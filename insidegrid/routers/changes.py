from http import HTTPStatus

from fastapi import APIRouter, Depends, Request

from insidegrid.db import get_db
from insidegrid.schemas.schemas import ChangeInputSchema, ChangeOutputSchema, CommentInputSchema, CommentOutputSchema
from insidegrid.crud.change import get_changes, create_change, add_like_to_change, add_dislike_to_change, change_likes, change_subscribtions, change_dislikes
from insidegrid.crud.comment import create_comment, get_comments

router = APIRouter()

@router.get("/changes", status_code=HTTPStatus.OK, response_model=list[ChangeOutputSchema])
def get_all_changes(session=Depends(get_db)):
    all_changes = get_changes(session)
    return all_changes

@router.post("/change", status_code=HTTPStatus.CREATED)
def create_new_change(change: ChangeInputSchema, session=Depends(get_db)):
    return create_change(session, change)

@router.post("/changes/{change_id}/like", status_code=HTTPStatus.CREATED)
def like_change(change_id: int, user_id: int, session=Depends(get_db)):
    return add_like_to_change(session, change_id, user_id)

@router.post("/changes/{change_id}/dislike", status_code=HTTPStatus.CREATED)
def dislike_change(change_id: int, user_id: int, session=Depends(get_db)):
    return add_dislike_to_change(session, change_id, user_id)

@router.get("/changes/{change_id}/subscribtions", status_code=HTTPStatus.OK)
def get_change_subscribtions(change_id: int, session=Depends(get_db)):
    return change_subscribtions(session, change_id)

@router.get("/changes/{change_id}/likes", status_code=HTTPStatus.OK)
def get_change_likes(change_id: int, session=Depends(get_db)):
    return change_likes(session, change_id)

@router.get("/changes/{change_id}/dislikes", status_code=HTTPStatus.OK)
def get_change_dislikes(change_id: int, session=Depends(get_db)):
    return change_dislikes(session, change_id)


@router.get("/changes/{change_id}/comments", status_code=HTTPStatus.OK)
def get_change_comments(change_id: int, session=Depends(get_db)):
    return get_comments(session, change_id)

@router.post("/changes/{change_id}/comment", status_code=HTTPStatus.CREATED)
def create_change_comment(comment: CommentInputSchema, change_id: int, session=Depends(get_db)):
    return create_comment(session, change_id, comment)

