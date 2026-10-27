from fastapi import FastAPI, HTTPException
from courses_service import courses



app = FastAPI()

@app.get("/welcome")
def welcome_msg():
    return{
        "message": "Welcome to Past-API",
    }

@app.get("/greeting")
def greet_msg():
    return{
        "message": "Hello World",
    }

@app.get("/courses")
def get_courses():
    return courses


# path parameter method
@app.get("/courses/{course_id}")
def course_by_id(course_id:int):
    #input
    course = courses.get(course_id)
    if course is None:
        raise HTTPException(
            status_code=400,
            detail="Course not found"
        )
    return course


#query parameter method
@app.get("/courses")
def course_by_id(course_id:int):
    #input
    course = courses.get(course_id)
    if course is None:
        raise HTTPException(
            status_code=400,
            detail="Course not found"
        )
    return course





