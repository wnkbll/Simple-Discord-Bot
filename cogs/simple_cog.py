import discord
from discord.ext import commands
from discord import app_commands

from src.config import guilds


class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.rename()
    @app_commands.describe()
    async def simple_command_from_cog(self, interaction: discord.Interaction):
        return await interaction.response.send_message('Hello, World!')


async def setup(bot: commands.Bot):
    await bot.add_cog(SimpleCog(bot), guilds=guilds)
