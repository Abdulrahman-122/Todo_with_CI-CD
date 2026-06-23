from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router2 = APIRouter()
templates = Jinja2Templates(directory="main/templates")


@router2.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router2.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router2.get("/todos-page")
def todos_page(request: Request):
    return templates.TemplateResponse("todos.html", {"request": request, "user": True})


@router2.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@router2.get("/settings")
def settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})
