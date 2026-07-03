from fastapi import APIRouter
from fastapi import Request
from fastapi import status

from app.cogs import loggers


router = APIRouter()

@router.post("/data-logged")
async def logged(request: Request):
    data = await request.json()

    await loggers.GARM(request.app.state.bot).log_data(lvl="TEMP_LOGGER", data=data)
    return status.HTTP_200_OK

@router.post("/auto-log")
async def AutoLoger(request: Request):
    data = await request.json()

    await loggers.SYSTEM(request.app.state.bot).site_loger(data=data)
    return status.HTTP_200_OK