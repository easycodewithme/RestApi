def ExerciseEntity(item) -> dict:
     return {
        "id":str(item["_id"]),
        "name":item["name"],
        "duration":item["duration"],
        "difficulty":item["difficulty"]
    }

def ExercisesEntity(entity) -> list:
    return [ExerciseEntity(item) for item in entity]