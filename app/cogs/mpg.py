import disnake
from disnake.ext import commands
from disnake import TextChannel, NewsChannel

import requests
import asyncio
import json
import io

class MPG(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="registration", aliases=["mreg"])
    async def mpg_registrations(self, ctx: commands.Context):

        return await ctx.send("Регистрация была завершена.")

        if ctx.guild != None: return await ctx.send("Для приватности команда работает только в лс")

        req = requests.get(f"https://ponyglory.ru/api/v1/public/link/{ctx.author.id}")
        if req.status_code == 200:
            responce = json.loads(req.content.decode("utf-8"))

            await ctx.send(f"Ваша ссылка регистрации: {responce['one_time_link']}\n-# УЧТИТЕ! Ссылка однаразовая и если вы потеряли или использовали текущую, но не закончили регистрацию, вы сможете зарегистрировать новую, но если вы закончили регистрацию, вы больше не сможете зарегистрироваться.")
            user_pony = await self.bot.fetch_user(374061361606688788)
            await user_pony.send(f"🟨 Игрок {ctx.author.global_name} запросил ссылку регистрации")
        elif req.status_code == 400:
            await ctx.send(f"Вы уже зарегистрированны в системе.\n-# Если вы этого не делали, но получили такой ответ, обратитесь к администратору.")
        else:
            await ctx.send(f"Сайт вернул код ошибки: {req.status_code}")

    @commands.command(name="mybase", aliases=["mb"])
    async def user_base_anket(self, ctx: commands.Context):
        user_uid = ctx.author.id

        req = requests.get(f"http://127.0.0.1:8090/api/v1/private/base-ankets/{user_uid}")
        if req.status_code == 200:
            responce = json.loads(req.content.decode("utf-8"))

            json_text = json.dumps(responce, ensure_ascii=False, indent=2)

            await ctx.send(f"```json\n{json_text}\n```")
        else:
            await ctx.send("Возможно вас нет в базе, либо вы не участник GARM.")

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(MPG(bot))