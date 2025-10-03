from aiohttp import web

async def web_server():
    app = web.Application()

    # Health check route
    async def healthcheck(request):
        return web.Response(text="Swift Rename Bot is running ✅")

    app.router.add_get("/", healthcheck)  # <- Default route

    return app
