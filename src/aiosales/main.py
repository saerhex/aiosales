from fastapi import FastAPI
import uvicorn  # type: ignore

from aiosales.containers import Container
from aiosales.endpoints import router


def create_app() -> FastAPI:
    container = Container()

    app = container.app()
    container.database()

    app.include_router(router=router)
    return app


app = create_app()


if __name__ == '__main__':
    uvicorn.run('aiosales.main:app', host='127.0.0.1', port=8080, reload=True)
