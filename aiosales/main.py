import uvicorn
from fastapi import FastAPI


def create_app():
    # container = Container()

    app = FastAPI()
    app.include_router()


def start():
    """Start FastAPI application via uvicorn."""
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=2)
