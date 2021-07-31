from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])
    
runner = web.AppRunner(app)


async def run_app(port: int):
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', port)
    await site.start()


async def stop_app():
    await runner.cleanup()
