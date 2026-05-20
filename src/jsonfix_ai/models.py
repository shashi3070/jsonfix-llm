from pydantic import BaseModel


class RepairResult(BaseModel):
    fixed: str
    was_repaired: bool
    fixes: list[str] = []
    error_count: int = 0
    errors: list[str] = []
