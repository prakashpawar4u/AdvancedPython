import aiohttp

import asyncio
from aiohttp import web

async def handle(request):
    await asyncio.sleep(1)
    return web.Response(text="Hello, World!")

async def init():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    return app

web.run_app(init())