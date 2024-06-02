from fastapi import APIRouter
from config.db import conn
from models.exercise import Exercise
from schemas.exercise import ExerciseEntity, ExercisesEntity
from bson import ObjectId

exercise = APIRouter() 

@exercise.get('/')
async def find_all_exercises():
    return ExercisesEntity(conn.local.exercise.find())

@exercise.get('/{id}')
async def find_one_exercise(id):
    return ExerciseEntity(conn.local.exercise.find_one({"_id": ObjectId(id)}))

@exercise.post('/')
async def add_excercise(exercise: Exercise):
    conn.local.exercise.insert_one(dict(exercise))
    return ExercisesEntity(conn.local.exercise.find())

@exercise.post('/{id}')
async def update_exercise(id, exercise: Exercise):
    conn.local.exercise.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(exercise)})
    return ExerciseEntity(conn.local.exercise.find_one({"_id": ObjectId(id)}))

@exercise.delete('/{id}')
async def delete_exercise(id):
    return ExerciseEntity(conn.local.exercise.find_one_and_delete({"_id": ObjectId(id)}))
