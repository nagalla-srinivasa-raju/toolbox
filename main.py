from fastapi import FastAPI
import models
from database import engine
from routers import VocabularyPillRouters

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(VocabularyPillRouters.router)