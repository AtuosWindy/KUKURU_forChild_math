from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates

from routers import home, problem, result, ranking

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="kukuru-secret"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home.router)
app.include_router(problem.router)
app.include_router(result.router)
app.include_router(ranking.router)

templates = Jinja2Templates(directory="templates")