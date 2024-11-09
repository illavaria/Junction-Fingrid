from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class UserInputSchema(BaseModel):
    username: str
    account_email: str = Field(..., max_length=250)
    password: str = Field(..., max_length=16)
    role: str = Field(..., max_length=40)

class UserLoginInputSchema(BaseModel):
    username: str
    password: str

class UserOutputSchema(BaseModel):
    id: int
    account_email: str
    role: str

    class Config:
        orm_mode = True

# Changes Schemas
class ChangeInputSchema(BaseModel):
    name: str
    status: Optional[str] = None
    creator_user_id: int
    description: str
    parent_id: Optional[int] = None
    tags: Optional[List[str]] = None

class ChangeOutputSchema(BaseModel):
    id: int
    name: str
    status: str
    creator_user_id: int
    description: str
    parent_id: Optional[int]
    tags: Optional[List[str]]

    class Config:
        orm_mode = True

# Releases Schemas
class ReleaseInputSchema(BaseModel):
    change_id: int
    name: str
    description: str
    release_date: datetime
    release_source: str
    release_documents: Optional[List[str]] = []
    type: Optional[str]
    tags: Optional[List[str]] = None

class ReleaseOutputSchema(BaseModel):
    id: int
    change_id: int
    name: str
    description: str
    release_date: datetime
    release_source: str
    release_documents: Optional[List[str]] = []
    tags: Optional[List[str]]

    class Config:
        orm_mode = True

class LikedChangeInputSchema(BaseModel):
    user_id: int
    change_id: int

class LikedChangeOutputSchema(BaseModel):
    id: int
    user_id: int
    change_id: int

    class Config:
        orm_mode = True

class DislikedChangeInputSchema(BaseModel):
    user_id: int
    change_id: int

class DislikedChangeOutputSchema(BaseModel):
    id: int
    user_id: int
    change_id: int

    class Config:
        orm_mode = True

class SubscriptionInputSchema(BaseModel):
    user_id: int
    change_id: int

class SubscriptionOutputSchema(BaseModel):
    id: int
    user_id: int
    change_id: int

    class Config:
        orm_mode = True

class LikedReleaseInputSchema(BaseModel):
    user_id: int
    release_id: int

class LikedReleaseOutputSchema(BaseModel):
    id: int
    user_id: int
    release_id: int

    class Config:
        orm_mode = True

class DislikedReleaseInputSchema(BaseModel):
    user_id: int
    release_id: int

class DislikedReleaseOutputSchema(BaseModel):
    id: int
    user_id: int
    release_id: int

    class Config:
        orm_mode = True

class HistoryInputSchema(BaseModel):
    author_id: int
    date: datetime
    change_id: Optional[int] = None
    difference: dict

class HistoryOutputSchema(BaseModel):
    id: int
    author_id: int
    date: datetime
    change_id: Optional[int]
    difference: dict

    class Config:
        orm_mode = True

class CommentInputSchema(BaseModel):
    change_id: Optional[int] = None
    release_id: Optional[int] = None
    author_id: int
    date: datetime
    replied_to_comment_id: Optional[int] = None
    likes: Optional[int] = 0
    dislikes: Optional[int] = 0

class CommentOutputSchema(BaseModel):
    id: int
    change_id: Optional[int]
    release_id: Optional[int]
    author_id: int
    date: datetime
    replied_to_comment_id: Optional[int]
    likes: int
    dislikes: int

    class Config:
        orm_mode = True
