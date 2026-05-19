from fastapi import FastAPI
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()

workout_database = [
    {
        "id": 1,
        "name": "Running",
        "duration_min": 30,
        "calories": 250,
        "date": "16.05.2026"
    },
    {
        "id": 2,
        "name": "Swimming",
        "duration_min": 30,
        "calories": 250,
        "date": "16.05.2026"
    },
    {
        "id": 3,
        "name": "Jogging",
        "duration_min": 30,
        "calories": 250,
        "date": "18.05.2026"
    },
    {
        "id": 4,
        "name": "Swimming",
        "duration_min": 30,
        "calories": 250,
        "date": "19.05.2026"
    }
]

# 
class Workout(BaseModel):
    name: str
    duration_min: int
    calories: int

@app.get("/")
def home():
    return {"message": "Welcome to Workout Tracker"}

@app.post("/workouts")
def add_workout(workout: Workout):
    # Creating ID by checking max and adding one
    new_id = len(workout_database) + 1

    # Changing data to JSON
    workout_with_date = workout.model_dump()
    # Adding date and number
    workout_with_date["date"] = datetime.today().strftime("%d.%m.%Y")
    workout_with_date["id"] = new_id

    # Saving to database
    workout_database.append(workout_with_date)
    return 

@app.get("/workouts")
def show_workouts():
    return workout_database

@app.get("/workouts/today")
def show_workouts_today():
    todays_workout = []

    today = datetime.today().strftime("%d.%m.%Y")

    for workout_id in workout_database:
        if workout_id["date"] == today:
            todays_workout.append(workout_id)

    return todays_workout

@app.get("/workouts/yesterday")
def show_workouts_yesterdayday():
    yesterdays_workout = []

    yesterday = (datetime.today() - timedelta(days = 1)).strftime("%d.%m.%Y")

    for workout_id in workout_database:
        if workout_id["date"] == yesterday:
            yesterdays_workout.append(workout_id)

    return yesterdays_workout

@app.delete("/workouts")
def delete_workout():
    return