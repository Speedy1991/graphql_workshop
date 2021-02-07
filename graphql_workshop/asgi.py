import os
import django
from django.core.handlers.asgi import ASGIHandler
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from django.urls import resolve
from starlette.websockets import WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphql_workshop.settings')


async def application(scope, receive, send):
    django.setup(set_prefix=False)
    app = ASGIStaticFilesHandler(ASGIHandler())
    if scope["type"] == "lifespan":
        return
    if scope["type"] == "websocket" and scope['raw_path'] and scope['raw_path'] == '/graphqlws/':
        match = resolve(scope["raw_path"])
        await match.func(WebSocket(scope, receive, send), *match.args, **match.kwargs)
        return
    return await app(scope, receive, send)
