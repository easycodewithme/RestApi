from pydantic import BaseModel
class Exercise(BaseModel):
    name: str
    duration: int
    difficulty: str