from fastapi import FastAPI

from meal_plan.containers import Container

from .endpoints import router


def create_app() -> FastAPI:
    # Instantiate the container which will wire it
    Container()

    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()
