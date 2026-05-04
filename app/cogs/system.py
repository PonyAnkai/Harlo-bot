import disnake
from disnake.ext import commands
from disnake import TextChannel, NewsChannel

from typing import Literal

import json

from pathlib import Path
from io import BytesIO

BASE_DIR = Path(__file__).resolve().parent

class SYSTEM(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def log_data(self, lvl:Literal["TEMP_LOGGER", "INFO", "WARNING", "ERROR"], data: dict):
        
        if lvl == "TEMP_LOGGER":
            guild = await self.bot.fetch_guild(1199488197885968515)
            channel = await guild.fetch_channel(1460806945865863336)
            
            user = await self.bot.fetch_user(int(data["user_uid"]))
            user_pony = await self.bot.fetch_user(374061361606688788)
            await user.send("Ваша анкета была принята для участия в игре. Ожидайте начала 5-го сезона.")
            
            json_bytes = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            fp = BytesIO(json_bytes)
            fp.seek(0)
            await user_pony.send(file=disnake.File(fp, "data.json"))
            if isinstance(channel, (TextChannel, NewsChannel)):
                await channel.send(f"Игрок {user.global_name} прошел регистрацию")      

    @commands.command(name="ping")
    async def ping(self, ctx):
        return await ctx.send("Pong")

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(SYSTEM(bot))