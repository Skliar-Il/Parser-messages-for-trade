from pydantic import BaseModel

class Schema_Check_Text(BaseModel):
    securities: str
    cut: int
    type: str
    change: float
    error: str | None = None