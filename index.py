from fastapi import FastAPI
from routes.exercise import exercise

app = FastAPI()
app.include_router(exercise)
