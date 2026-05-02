import disnake
from disnake.ext import commands

from dotenv import dotenv_values
from fastapi import FastAPI

from api import trigers

import asyncio
import uvicorn
import json
import os

# Load configurate file
with open("config.json", encoding="UTF-8") as fp: config = json.load(fp)
ENV = dotenv_values()

bot = commands.Bot (
    command_prefix=config["PREFIX"], 
    intents=disnake.Intents.all(), 
    activity= disnake.Activity(name="MPG", type= disnake.ActivityType.watching),
    reload=True, 
    help_command=None,
)
app_fastAPI = FastAPI()
app_fastAPI.include_router(trigers.router, prefix="/apibot.v1")
app_fastAPI.state.bot = bot

async def init_api():
    fp = uvicorn.Config(app_fastAPI, host="127.0.0.1", port=8080, loop="asyncio", lifespan="off")
    server = uvicorn.Server(fp)
    await server.serve()

async def main():
    BASEDIR = f"{os.getcwd()}\\"
    for item in os.listdir(BASEDIR + f"cogs\\"):
        try: bot.load_extension(f"cogs.{item.replace('.py', '')}")
        except: pass    

    bot_task = asyncio.create_task(bot.start(str(ENV["TOKEN"])))
    api_task = asyncio.create_task(init_api())
    
    print("\t\t BOT IS GOTTA RUN")
    await asyncio.gather(bot_task, api_task)  


if __name__ == "__main__":
    asyncio.run(main())