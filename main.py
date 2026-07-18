from fastapi import FastAPI,HTTPException,status
from models import Post
app=FastAPI()

@app.get("/posts")
def get_posts():
   return {"message":"posts"}


@app.post("/posts")
def create_post(new_post:Post):
   print(new_post)
   return {"data":new_post}

@app.get("/posts/{id}")
def get_post(id:int):
   #perform db searcg operation
   if not row:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} couldn't be found")
   return {"data":"dummy single post data"}

@app.put("/posts/{id}")
def update_post(id:int):
   #update row in db
   return { "data":"return updated post dta/ success code"}

@app.delete("/posts/{id}",status_code=204)
def delete_post():
   #delete row 
   return   
