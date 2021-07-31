from aiohttp import web


async def test(_request):
    return web.Response(text="test")


def route_app(app: web.Application):
    app.add_routes([
        web.get("/", test)
    ])
