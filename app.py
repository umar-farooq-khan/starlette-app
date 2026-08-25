from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def hello_world(request):
    return PlainTextResponse("Hello, world!")


async def hello_name(request):
    name = request.path_params["name"]
    return PlainTextResponse(f"Hello, {name}!")


app = Starlette(routes=[
    Route("/", hello_world),
    Route("/hello/{name}", hello_name),
])
