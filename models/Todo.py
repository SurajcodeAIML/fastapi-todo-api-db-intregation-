from sqlmodel import SQLModel, Field
from datetime import datetime
from models.TodoBase import TodoBase

class Todo(TodoBase,table=True):        #replace SQLModel to TodoBase & table= true meaning is: jaba create huncha table than sabai todobase ko field create huncha as a column.
    id: int | None = Field(primary_key=True, default=None)
    # title: str = Field(min_length=2, max_length=10, nullable=False)
    # description: str = Field(min_length=5, max_length=50, nullable=True)    #removing this 3 later
    # priority: int = Field(le=5, ge=1, default=1)
    # is_completed: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now(), nullable=False)

    #so yai ho ek model Todo class kako jaha hamile sabai properties lai
    # define garyau and yo sab properties as a column create huncha database ma.
