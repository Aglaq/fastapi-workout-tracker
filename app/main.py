from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
from app.database import connection, cursor

app = FastAPI()
 
class Workout(BaseModel):
    name: str
    duration_min: int
    calories: int

@app.get("/")
def home():
    return {"message": "Welcome to Workout Tracker"}

@app.get("/workouts")
def show_workouts():

    cursor.execute("SELECT * FROM workouts")

    rows = cursor.fetchall()
    return rows

@app.post("/workouts")
def add_workout(workout: Workout):

    today = datetime.today().strftime("%d.%m.%Y")

    cursor.execute("""
            INSERT INTO workouts
            (name, duration_min, calories, date)
            VALUES (?, ?, ?, ?)
            """,
            (
                workout.name,
                workout.duration_min,
                workout.calories,
                today
            )
    )
    connection.commit()

    return {"message": "Workout added"}

# @app.get("/workouts/today")
# def show_workouts_today():

#     today = datetime.today().strftime("%d.%m.%Y")
#     cursor.execute("SELECT * FROM workouts WHERE")

#     rows = cursor.fetchall()
#     return rows

# @app.get("/workouts/yesterday")
# def show_workouts_yesterdayday():
#     yesterdays_workout = []

#     yesterday = (datetime.today() - timedelta(days = 1)).strftime("%d.%m.%Y")

#     for workout_id in workout_database:
#         if workout_id["date"] == yesterday:
#             yesterdays_workout.append(workout_id)

#     return yesterdays_workout

# @app.delete("/workouts/{id}")
# def delete_workout():
#     return
