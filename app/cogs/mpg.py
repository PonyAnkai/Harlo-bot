import disnake
from disnake.ext import commands

import requests
import asyncio
import json

class MPG(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.command(name="mpg-reg")
    async def mpg_registrations(self, ctx):

        if ctx.guild != None: return await ctx.send("Для приватности команда работает только в лс")

        req = requests.get(f"https://ponyglory.ru/api.v1/get-link/{ctx.author.id}")
        if req.status_code == 200:
            responce = json.loads(req.content.decode("utf-8"))

            await ctx.send(f"Ваша ссылка регистрации: {responce['one_time_link']}\n-# УЧТИТЕ! Ссылка однаразовая и если вы потеряли или использовали текущую, но не закончили регистрацию, вы сможете зарегистрировать новую, но если вы закончили регистрацию, вы больше не сможете зарегистрироваться.")
        elif req.status_code == 400:
            await ctx.send(f"Вы уже зарегистрированны в системе.\n-# Если вы этого не делали, но получили такой ответ, обратитесь к администратору.")
        else:
            await ctx.send(f"Сайт вернул код ошибки: {req.status_code}")

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(MPG(bot))