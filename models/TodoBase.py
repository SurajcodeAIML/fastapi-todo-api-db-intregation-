from sqlmodel import SQLModel, Field
from datetime import datetime

class TodoBase(SQLModel):
    title: str = Field(min_length=2, max_length=10, nullable=False)
    # id: int | None = Field(primary_key=True, default=None)
    # created_at: datetime = Field(default=datetime.now(), nullable=False)
    description: str = Field(min_length=5, max_length=50, nullable=True)
    priority: int = Field(le=5, ge=1, default=1)
    is_completed: bool = Field(default=False)

#yesko meaning k ho bhane, todobase jun extend bhairakocha todo bata, yesko meaning k ho bhane, jun jun propterties haru todobase ma cha tyo sabai properties
# available huncha todo ma.


