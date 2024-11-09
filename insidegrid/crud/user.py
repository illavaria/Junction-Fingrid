from sqlalchemy.orm import Session
from insidegrid.db import models
from insidegrid.schemas.schemas import UserInputSchema


def create_user(session: Session, user: UserInputSchema) -> models.Users:
    new_user = models.Users(
        username=user.username,
        account_email=user.account_email,
        password=user.password,
        role=user.role
    )
    session.add(new_user)
    session.flush()
    return new_user

