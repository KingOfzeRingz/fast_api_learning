from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post('')
async def addTask(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.get_all_tasks()
    return {'tasks': tasks}
