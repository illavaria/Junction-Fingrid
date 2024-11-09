from http import HTTPStatus

from fastapi import APIRouter, Depends, Request

from insidegrid.db import get_db
from insidegrid.schemas.schemas import ReleaseOutputSchema, ReleaseInputSchema
from insidegrid.crud.release import get_releases, create_release, add_like_to_release, add_dislike_to_release

router = APIRouter()

@router.get("/releases", response_model=list[ReleaseOutputSchema])
def get_all_releases(session=Depends(get_db)):
    all_releases = get_releases(session)
    return all_releases

@router.post("/release", status_code=HTTPStatus.CREATED)
def create_new_release(release: ReleaseInputSchema, session=Depends(get_db)):
    return create_release(session, release)

@router.post("/releases/{release_id}/like", status_code=HTTPStatus.CREATED)
def like_release(release_id: int, user_id: int, session=Depends(get_db)):
    return add_like_to_release(session, release_id, user_id)

@router.post("/releases/{release_id}/dislike", status_code=HTTPStatus.CREATED)
def dislike_release(release_id: int, user_id: int, session=Depends(get_db)):
    return add_dislike_to_release(session, release_id, user_id)

