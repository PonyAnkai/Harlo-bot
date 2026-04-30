from fastapi import APIRouter
from fastapi import Request
from fastapi import status

from cogs import system


router = APIRouter()

@router.post("/data-logged")
async def logged(request: Request):
    data = await request.json()

    await system.SYSTEM(request.app.state.bot).log_data(lvl="TEMP_LOGGER", data=data)
    return status.HTTP_200_OK