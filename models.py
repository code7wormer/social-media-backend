from pydantic import BaseModel, Field

class Post(BaseModel):
  title:str
  content:str
  published:bool = True
  rating:int | None = Field(default=None, ge=0, le=10)