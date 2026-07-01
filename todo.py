from typing import Annotated
from fastapi import Depends, FastAPI, status
from sqlmodel import Session
from models.Todo import Todo
from database.db import create_table, get_session, SessionDependency
from request_model.TodoRequest import TodoRequest
from response_model.TodoResponse import TodoResponse

#you can remove unnecessary import statement from above you don't need that.

app = FastAPI(
    title="TechAxis FastAPI Tutorial",
    version="0.0.1",
    description="How to connect with database"
)

@app.on_event("startup")
def on_startup():
    create_table()

@app.get("/")           # >>here get is the end point
async def hello():
    return "Hello world"

@app.post("/todo/create", response_model=TodoResponse,status_code=status.HTTP_201_CREATED)
async def create_todo(todoReq: TodoRequest, session: SessionDependency):
    todo = Todo.model_validate(todoReq)
    session.add(todo)
    session.commit()             #it will save on database
    session.refresh(todo)          # hamilai database ma jana pardaina and get garnu pardaina if hamile refresh garyo bhane, so that it will automaticall refresh in session
                                 #database ma jani, todo ko pheri lyaunu and return garni, yo kura kehi garnu pardaina, jaba hamile ya refresh garchau than todo internally refresh huncha and return huncha.
    return todo

#now i will do sudden changes here, jun hamro get session chaa, db.py ma, teslai thorai improve garnu parni cha
# so k improve garnu parcha bhanda, jaba hami kunai operation garchau todo.py ma than tya hami return garchau so return
# garnu agi session lai hamile close pani garnu parcha. or if yaha commit pachi or during commit kunai error bhayo
# so to commit lai hamile rollback ni garnu parcha.So, roll back kasari garni ta ?
#now go to db.py >> and do some changes there and finally close session and do some extra changes there.


#Fetch Data from Database with SQLModel & FastAPI (In Hindi) | Ch 3 Episode 5

@app.get("/todo/all", response_model=[TodoResponse])
def get_all():
    pass
















