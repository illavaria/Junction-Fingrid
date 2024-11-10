
from sqlalchemy.orm import Session
from starlette import status

from insidegrid.schemas.schemas import ChangeInputSchema, ChangeOutputSchema
from insidegrid.db import models


def get_changes(session: Session) -> list[models.Changes]:
    return session.query(models.Changes).filter().all()

def create_change(session: Session, change: ChangeInputSchema) -> models.Changes:
    change_model = models.Changes(
        status=change.status,
        name=change.name,
        creator_user_id=change.user_id,
        description=change.description,
        parent_id=change.parent_id,
        tags=change.tags,
    )

    session.add(change_model)
    session.flush()
    return change_model

def get_users_changes(session: Session, user_id: int) -> list[models.Changes] :
    return (session.query(models.Changes)
            .filter(models.Changes.creator_user_id == user_id)
            .all())

def get_subscribed_changes(session: Session, user_id: int) -> list[models.Changes]:
    return (session.query(models.Changes)
            .join(models.Subscriptions)
            .filter(models.Subscriptions.user_id == user_id)
            .all())


def get_liked_changes(session: Session, user_id: int) -> list[models.Changes]:
    return (session.query(models.Changes)
            .join(models.LikedChanges)
            .filter(models.LikedChanges.user_id == user_id)
            .all())

def get_disliked_changes(session: Session, user_id: int) -> list[models.Changes]:
    return (session.query(models.Changes)
            .join(models.DislikedChanges)
            .filter(models.DislikedChanges.user_id == user_id)
            .all())


def change_subscribtions(session: Session, change_id:int) -> list[models.Users]:
    return (session.query(models.Users)
            .join(models.Subscriptions)
            .filter(models.Subscriptions.change_id == change_id)
            .all())

def change_likes(session: Session, change_id:int) -> list[models.Users]:
    return (session.query(models.Users)
            .join(models.LikedChanges)
            .filter(models.LikedChanges.change_id == change_id)
            .all())

def change_dislikes(session: Session, change_id:int) -> list[models.Users]:
    return (session.query(models.Users)
            .join(models.DislikedChanges)
            .filter(models.DislikedChanges.change_id == change_id)
            .all())

def add_like_to_change(session: Session, change_id: int, user_id: int):
    existing_like = session.query(models.LikedChanges).filter(
        models.LikedChanges.change_id == change_id,
        models.LikedChanges.user_id == user_id
    ).first()

    if existing_like:
        raise Exception("You already liked this change")

    new_like = models.LikedChanges(change_id=change_id, user_id=user_id)
    session.add(new_like)
    session.commit()
    return {"message": "Like added successfully"}


def add_dislike_to_change(session: Session, change_id: int, user_id: int):
    existing_dislike = session.query(models.DislikedChanges).filter(
        models.DislikedChanges.change_id == change_id,
        models.DislikedChanges.user_id == user_id
    ).first()

    if existing_dislike:
        raise Exception("You already disliked this change")

    new_dislike = models.DislikedChanges(change_id=change_id, user_id=user_id)
    session.add(new_dislike)
    session.commit()
    return {"message": "Dislike added successfully"}

def subscribe_to_change(session: Session, user_id: int, change_id: int):
    new_subscription = models.Subscriptions(user_id=user_id, change_id=change_id)
    session.add(new_subscription)
    session.commit()
    session.refresh(new_subscription)
    return {"message": "Successfully subscribed to the change"}
