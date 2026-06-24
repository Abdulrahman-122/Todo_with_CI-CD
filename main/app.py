from fastapi import FastAPI
from main.database import Base
from main.database import engine
from main.apis import router
from main.auth import router1
from main.serve_html import router2
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


# build any tables that you assigned to your engine into database
Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI(title="Devops engine")
app.include_router(router1)
app.include_router(router)
app.include_router(router2)
templates = Jinja2Templates(directory="main/templates")
app.mount("/static", StaticFiles(directory="main/static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#api for smoke test

@app.get('/health')
def check_health():
    return {"status":"I am Healthy"}