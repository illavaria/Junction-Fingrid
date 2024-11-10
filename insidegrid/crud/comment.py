from sqlalchemy.orm import Session
from starlette import status

from insidegrid.schemas.schemas import CommentInputSchema, CommentOutputSchema
from insidegrid.db import models

def create_comment(session: Session, change_id: int, comment: CommentInputSchema):
    comment_model = models.Comments(
        change_id=change_id,
        release_id=comment.release_id,
        author_id=comment.user_id,
        content=comment.content,
        date=comment.date,
        replied_to_comment_id=comment.replied_to_comment_id,
        likes=comment.likes,
        dislikes=comment.dislikes,
    )
    session.add(comment_model)
    session.flush()
    return comment_model

def get_comments(session: Session, change_id: int):
    return session.query(models.Comments).filter_by(change_id=change_id).all()

def like_comment(session: Session, comment_id: int):
    return session.query(models.Comments).filter(comment_id=comment_id).update(values={'likes': models.Comments.likes+1})

def dislike_comment(session: Session, comment_id: int):
    return session.query(models.Comments).filter(comment_id=comment_id).update(values={'dislikes': models.Comments.dislikes+1})
