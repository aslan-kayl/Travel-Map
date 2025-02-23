from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Banner(BaseModel):
    id: int
    title: str
    image: str
    created_at: datetime
    is_main: Optional[bool]


class CreateBanner(BaseModel):
    title: str
    image: str


class CreateQuestion(BaseModel):
    question: str


class Question(BaseModel):
    id: int
    question: str


class Answer(BaseModel):
    id: int
    answer: str
    question_id: Optional[int]


class CreateAnswer(BaseModel):
    answer: str
    question_id: int


class CreateInfo(BaseModel):
    icon: str
    description: str
    position: Optional[int]


class Info(BaseModel):
    id: int
    icon: str
    description: str
    position: int