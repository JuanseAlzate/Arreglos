from pydantic import BaseModel
from typing import List

class Req (BaseModel):
    list: List[int]