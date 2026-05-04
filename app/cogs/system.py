import disnake
from disnake.ext import commands
from disnake import TextChannel, NewsChannel

from typing import Literal

import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class SYSTEM(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def log_data(self, lvl:Literal["TEMP_LOGGER", "INFO", "WARNING", "ERROR"], data: dict):
        
        if lvl == "TEMP_LOGGER":
            guild = await self.bot.fetch_guild(1199488197885968515)
            channel = await guild.fetch_channel(1460806945865863336)
            
            user = await self.bot.fetch_user(int(data["user_uid"]))
            await user.send("Ваша анкета была принята для участия в игре. Ожидайте начала 5-го сезона.")
            
            file_path = BASE_DIR / "data" / "reg-data.json"
            with open(file_path, mode="r", encoding="utf-8") as fp:
                static_data = json.load(fp)


            shop = ""
            for item in data['shop_item']:
                if data['shop_item'][item] != 0:
                    shop += f"• {static_data['shop_item'][str(data['shop_item'][item][0])][str(data['shop_item'][item][1])]['name']}\n" 

            embed = disnake.Embed(title="Тестирование", )
            embed.description = ""
            embed.description += ""
            embed.description = f"""
                Пользователь: {user.global_name}\n
                Выбранная раса: {data['race']['name']}
                Сложность: {data['difficulty']}
                Название: {data['country_name']}
                Население: {data['population']}
                Геном расы: {static_data['genomes'][data['genome']]['name'] if data['genome'] else 'Нет'}
                Первый слот хорошей особенности: {static_data['traits'][str(data['good_traits']['1'])]['good']['name'] if data['good_traits']['1'] != 0 else 'Пусто'}
                Второй слот хорошей особенности: {static_data['traits'][str(data['good_traits']['2'])]['good']['name'] if data['good_traits']['2'] != 0 else 'Пусто'}
                Первый слот плохой особенности: {static_data['traits'][str(data['bad_traits']['1'])]['bad']['name'] if data['bad_traits']['1'] != 0 else 'Пусто'}
                Второй слот плохой особенности: {static_data['traits'][str(data['bad_traits']['2'])]['bad']['name'] if data['bad_traits']['2'] != 0 else 'Пусто'}
                Магазинные предметы:
                {shop}
            """

            if isinstance(channel, (TextChannel, NewsChannel)):
                return await channel.send(f"Игрок {user.global_name} прошел регистрацию")
            user_pony = await self.bot.fetch_user(374061361606688788)
            await user_pony.send(embed=embed)                

    @commands.command(name="ping")
    async def ping(self, ctx):
        return await ctx.send("Pong")

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(SYSTEM(bot))