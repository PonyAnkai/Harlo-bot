import disnake
from disnake.ext import commands

import requests

class ADMIN(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="mpg-reg-delete")
    async def mpg_registrations_deleter_user(self, ctx: commands.Context):
        if ctx.author.id != 374061361606688788: return

        req = requests.post(f"https://ponyglory.ru/api.v1/get-link/{ctx.author.id}")
        if req.status_code == 200:
            await ctx.send("Игрок удалён из зарегистрированных")
        elif req.status_code == 400:
            await ctx.send("Система не нашла такого пользователя.")
        else:
            await ctx.send("Внештатная ошибка, проверь логи.")

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(ADMIN(bot))