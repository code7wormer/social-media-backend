from fastapi import FastAPI
from models import Post
app=FastAPI()

@app.get("/")
def get_posts():
   return {"message":"posts"}


@app.post("/create_post")
def create_post(new_post:Post):
   print(new_post)
   return {"data":new_post}