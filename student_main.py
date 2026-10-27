#uvicorn student_main:app --reload


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import student_repo
app = FastAPI()

base_path = "/api"

@app.get(f"{base_path}/students/")
def get_all_students():
    return student_repo.get_student()


class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    course: str = Field(..., min_length=3, max_length=20)
    fee: float = Field(..., gt=0)

@app.get(f"{base_path}/students/")
def get_all_students():
    return student_repo.get_student()

@app.post(f"{base_path}/students/, status_code=201)")
def create_student(student: Student):
    return student_repo.insert_student(student)
