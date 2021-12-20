import asyncio

from fastapi import FastAPI
import uvicorn

from aiosales.containers import Container
from aiosales.endpoints import router

from tortoise.contrib.fastapi import register_tortoise


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()

    app.container = container
    app.include_router(router=router)

    return app


app = create_app()
register_tortoise(
        app,
        db_url='sqlite://test.db',
        modules={
            'models': [
                'aiosales.models'
            ]
        }
    )