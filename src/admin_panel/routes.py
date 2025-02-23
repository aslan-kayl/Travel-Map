from http.client import HTTPException

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.con.main import get_session
from typing import List
from .services import AdminPanelService
from .schemas import (
    Banner,
    CreateBanner,
    CreateQuestion,
    Question,
    Answer,
    CreateAnswer,
    Info,
    CreateInfo
)

banner_router = APIRouter()
info_router = APIRouter()
answer_router = APIRouter()
question_router = APIRouter()
admin_panel_service = AdminPanelService()


@banner_router.get("/", response_model=List[Banner])
async def get_all_banners(session: AsyncSession = Depends(get_session)):
    banners = await admin_panel_service.get_all_banners(session)
    return banners


@banner_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Banner)
async def create_banner(banner_data: CreateBanner, session: AsyncSession = Depends(get_session)):
    new_banner = await admin_panel_service.create_banner(session, banner_data)
    return new_banner


@banner_router.get("/{banner_id}", response_model=CreateBanner)
async def get_banner(banner_id: int, session: AsyncSession = Depends(get_session)):
    banner = await admin_panel_service.get_banner(session, banner_id)
    if banner:
        return banner
    else:
        raise HTTPException(status_code=404, detail="Banner not found")


@banner_router.patch("/{banner_id}", response_model=CreateBanner)
async def update_banner(banner_id: int, banner_update_data: CreateBanner, session: AsyncSession = Depends(get_session)):
    update_to_banner = await admin_panel_service.update_banner(banner_id, banner_update_data, session)
    if update_to_banner is None:
        raise HTTPException(status_code=404, detail="Banner not found")
    else:
        return update_banner


@banner_router.delete("/{banner_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_banner(banner_id: int, session: AsyncSession = Depends(get_session)):
    banner_to_delete = await admin_panel_service.delete_banner(banner_id, session)
    if banner_to_delete is None:
        raise HTTPException(status_code=404, detail="Banner not found")
    else:
        return {}


@info_router.get("/", response_model=List[Info])
async def get_all_infos(session: AsyncSession = Depends(get_session)):
    infos = await admin_panel_service.get_all_info(session)
    return infos


@info_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Info)
async def create_info(info_data: CreateInfo, session: AsyncSession = Depends(get_session)):
    new_info = await admin_panel_service.create_info(session, info_data)
    return new_info


@info_router.get("/{info_id}", response_model=CreateInfo)
async def get_info(info_id: int, session: AsyncSession = Depends(get_session)):
    info = await admin_panel_service.get_info(session, info_id)
    if info:
        return info
    else:
        raise HTTPException(status_code=404, detail="Info not found")

@info_router.patch("/{info_id}", response_model=Info)
async def update_info(info_id: int, info_update_data: Info, session:AsyncSession = Depends(get_session)):
    update_to_info = await admin_panel_service.update_info(info_id, session, info_update_data)
    if update_to_info is None:
        raise HTTPException(status_code=404, detail="Info not found")
    else:
        return update_info

@info_router.delete("/{info_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_info(info_id: int, session: AsyncSession = Depends(get_session)):
    info_to_delete = await admin_panel_service.delete_info(info_id, session)
    if info_to_delete is None:
        raise HTTPException(status_code=404, detail="Info not found")
    else:
        return {}


@question_router.get("/", response_model=List[Question])
async def get_all_questions(session: AsyncSession = Depends(get_session)):
    questions = await admin_panel_service.get_all_question(session)
    return questions

@question_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Question)
async def create_question(question_data: CreateQuestion, session: AsyncSession = Depends(get_session)):
    new_question = await admin_panel_service.create_question(session, question_data)
    return new_question

@question_router.get("/{question_id}", response_model=Question)
async def get_question(question_id: int, session: AsyncSession = Depends(get_session)):
    question = await admin_panel_service.get_question(session, question_id)
    if question:
        return question
    else:
        raise HTTPException(status_code=404, detail="Question not found")

@question_router.patch("/{question_id}", response_model=Question)
async def update_question(question_id: int, question_update_data: Question, session:AsyncSession = Depends(get_session)):
    update_to_question = await admin_panel_service.update_question(question_id, session, question_update_data)
    if update_to_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    else:
        return update_to_question

@question_router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question(question_id: int, session: AsyncSession = Depends(get_session)):
    question_to_delete = await admin_panel_service.delete_question(question_id, session)
    if question_to_delete is None:
        raise HTTPException(status_code=404, detail="Question not found")
    else:
        return {}

@answer_router.get("/", response_model=List[Answer])
async def get_all_answers(session: AsyncSession = Depends(get_session)):
    answers = await admin_panel_service.get_all_answers(session)
    return answers

@answer_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Answer)
async def create_answer(answer_data: CreateAnswer, session: AsyncSession = Depends(get_session)):
    new_answer = await admin_panel_service.create_answer(session, answer_data)
    return new_answer


@answer_router.get("/{answer_id}", response_model=Answer)
async def get_answer(answer_id: int, session: AsyncSession = Depends(get_session)):
    answer = await admin_panel_service.get_answer(session, answer_id)
    if answer:
        return answer
    else:
        raise HTTPException(status_code=404, detail="Answer not found")

@answer_router.patch("/{answer_id}", response_model=Answer)
async def update_answer(answer_id:int, answer_update_data: Answer, session: AsyncSession = Depends(get_session)):
    update_to_answer = await admin_panel_service.update_answer(answer_id, session, answer_update_data)
    if update_to_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    else:
        return update_to_answer

@answer_router.delete("/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer(answer_id: int, session: AsyncSession = Depends(get_session)):
    answer_to_delete = await admin_panel_service.delete_answer(answer_id, session)
    if answer_to_delete is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    else:
        return {}
