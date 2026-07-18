from pydantic import BaseModel
from pydantic import 

class Post(BaseModel):
  title:str
  content:str
  published:bool = True
  rating:str | None = None