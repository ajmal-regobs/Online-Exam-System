from fastapi import FastAPI

from app.database import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Exam System", version="1.0.0")
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "Online Exam System"}
