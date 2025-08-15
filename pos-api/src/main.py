from fastapi import FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import JSONResponse
from core.http import PosException
from persistence import create_db_and_tables, get_session_deps
from routers import article, internal, order, table, category, basket


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    # Clean up the ML models and release the resources


def app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(internal.router)
    app.include_router(basket.router)
    app.include_router(order.router)
    app.include_router(category.router)
    app.include_router(article.router)
    app.include_router(table.router)


    @app.exception_handler(PosException)
    async def unicorn_exception_handler(
        request: Request, exc: PosException
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.code,
            content={"error": exc.name, "message": exc.message, "code": exc.code},
        )

    @app.get("/")
    async def root():
        return {"message": "Welcome to KMPOS"}

    return app
