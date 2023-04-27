import discord
from discord.ext import commands

import os
import aiohttp

from .config import settings, guilds


class Client(commands.Bot):
    def __init__(self, **options):
        super().__init__(
            command_prefix=settings['prefix'],
            intents=discord.Intents.all(),
            application_id=settings['id'])
        self.session = None

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        print('--------------------------')
        print('Cogs:')
        for name in os.listdir("./cogs"):
            if name.endswith('.py'):
                print(f'\t{name}')
                await self.load_extension(f'cogs.{name[:-3]}')
        print('--------------------------')

        for guild in guilds:
            await self.tree.sync(guild=guild)

    async def close(self):
        await super().close()
        await self.session.close

    async def on_ready(self):
        print('--------------------------')
        print('Bot connected')
        print(f'Bot name: {self.user}')
        print(f'Bot ID: {self.user.id}')
        print('--------------------------')
        await self.change_presence(status=discord.Status.dnd, activity=discord.Game('себя'))
