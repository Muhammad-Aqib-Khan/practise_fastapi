from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

students = [{
    "id": 1,
    "name": "aqib",
    "age": 25,
}]

@app.get("/students")
def get_students():
    print("Following students are available")
    return students

@app.post("/students")
def add_students(id: int, name: str, age: int):
    students.append({"id": id, "name": name, "age": age})
    return students

@app.delete("/students")
def remove_student(id: Optional[int] = None, name: Optional[str] = None):
    global students
    students = [student for student in students if not (
        (id is not None and student["id"] == id) or
        (name is not None and student["name"] == name) 
    )]
    return students

@app.put("/students")
def update_student(id: int, name: str, age: int):
    global students
    students = [student for student in students if student["id"]!= id]
    students.append({"id": id, "name": name, "age": age})
    return students

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
