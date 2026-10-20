from pydantic import BaseModel,Field
from typing import Annotated,List

class PostBase(BaseModel):
    title: Annotated[str,Field(...,min_length=3,max_length=55,description="Enter your post title.")]
    content: Annotated[str,Field(...,min_length=10,max_length=256,description="Enter your post content.")]

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
        
class PostUpdate(BaseModel):
    title:Annotated[str,Field(default=None)];
    content:Annotated[str,Field(default=None)];

class GetResponse(BaseModel):
    posts:List[PostResponse]
    
    class Config:
        from_attributes = True
