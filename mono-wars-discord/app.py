from aiohttp import web
from routing import route_app


class App(web.Application):
    def __init__(self):
        self.discord = None
        self.runner = web.AppRunner(self)
        super().__init__()
        
    async def run_async(self, port: int):
        await self.runner.setup()
        site = web.TCPSite(self.runner, 'localhost', port)
        await site.start()
  
    async def stop_async(self):
        await self.runner.cleanup()


app = App()
route_app(app)
