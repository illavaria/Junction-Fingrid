from http.client import HTTPException

from sqlalchemy.orm import Session
from starlette import status

from insidegrid.schemas.schemas import ReleaseInputSchema, ReleaseOutputSchema
from insidegrid.db import models


def get_releases(session: Session) -> list[models.Releases]:
    return session.query(models.Releases).filter().all()


def create_release(session: Session, release: ReleaseInputSchema) -> models.Releases:

    release_model = models.Releases(
        release_id=release.release_id,
        name=release.name,
        release_date=release.release_date,
        release_source=release.release_source,
        release_documents=release.release_documents,
        tags=release.tags,
        type=release.type,
        description=release.description,
    )

    session.add(release_model)
    session.flush()
    return release_model

def get_subscribed_releases(session: Session, user_id: int) -> list[models.Releases]:
    return (session.query(models.Releases)
            .join(models.Subscriptions)
            .filter(models.Subscriptions.user_id == user_id)
            .all())


def get_liked_releases(session: Session, user_id: int) -> list[models.Releases]:
    return (session.query(models.Releases)
            .join(models.LikedReleases)
            .filter(models.LikedReleases.user_id == user_id)
            .all())

def get_disliked_releases(session: Session, user_id: int) -> list[models.Releases]:
    return (session.query(models.Releases)
            .join(models.DislikedReleases)
            .filter(models.DislikedReleases.user_id == user_id)
            .all())


def add_like_to_release(session: Session, release_id: int, user_id: int):
    existing_like = session.query(models.LikedReleases).filter(
        models.LikedReleases.release_id == release_id,
        models.LikedReleases.user_id == user_id
    ).first()

    if existing_like:
        raise Exception("You already liked this release")

    new_like = models.LikedReleases(release_id=release_id, user_id=user_id)
    session.add(new_like)
    session.commit()
    return {"message": "Like added successfully"}


def add_dislike_to_release(session: Session, release_id: int, user_id: int):
    existing_dislike = session.query(models.DislikedReleases).filter(
        models.DislikedReleases.release_id == release_id,
        models.DislikedReleases.user_id == user_id
    ).first()

    if existing_dislike:
        raise Exception("You already disliked this release")

    new_dislike = models.DislikedReleases(release_id=release_id, user_id=user_id)
    session.add(new_dislike)
    session.commit()
    return {"message": "Dislike added successfully"}

