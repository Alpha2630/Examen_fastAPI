from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONRespons

@app.get("/hello")
def hello_world():
    return JSONResponse(content="Hello world", status_code=200 OK)

@app.get("/welcome")
def welcome_user(name: str):
    
    return JSONResponse(content="Welcome {name}", status_code=200 OK)


@app.post("/students")
class students(student):
    Reference : str
    FirstName : str
    LastName : str
    Age : int
memorise_students: List[students] = []
def memories():
    return ([memo.model_dump() for memo in memorise_students], status_code = CREATED)

@app.get("/students")
def stud():
    return ({"students" : memories()}, status_code = 200 OK)


@app.put("/students")
def student_new(Reference: List[students]: id):
    memorise_students.extend(Reference)
    return {"events": memories()}
    



@app.get("/students-authorized")
class students(student):
    Reference : str
    FirstName : str
    LastName : str
    Age : int
    Autorisation : str
memorise_students: List[students] = []
def students_authorized(students_authorized: List[students]):
    for students in students_authorized:
        for i, existing in enumerate(memorise_students):
            if Autorisation is none:
                
                return JSONResponse(content="N'est pas autoriser")
                break
        else if(Autorisation != "bon courrage"):
            return JSONResponse(content="Vous n'etes pas autohorisé ")