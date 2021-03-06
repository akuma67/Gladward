import discord
import random
from discord.ext import commands

class Secret:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Secret Commands Cog was loaded successfully!")

    @commands.command()
    async def despacito(self, ctx, despaversion):
        if despaversion == '2':
            await ctx.send("Dammit {}..\n https://www.youtube.com/watch?v=W3GrSMYbkBE".format(ctx.message.author.mention))

    @despacito.error
    async def despacito_handler(self, ctx, error):
        if error.param.name == 'despaversion':
            await ctx.send("Dammit {}..\n https://www.youtube.com/watch?v=kJQP7kiw5Fk".format(ctx.message.author.mention))



def setup(bot):
    bot.add_cog(Secret(bot))