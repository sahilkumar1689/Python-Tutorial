from sqlalchemy.orm import Session
from app.schemas.post import *
from app.models.post import *
from app.models.user import *
from app.utils.exceptions import *

# Here we create a post:
def create_post(db: Session, post: PostCreate, user_id: int):
    with db.begin():
        # Validate the user_id:
        existed_user = db.query(User).filter(User.id == user_id).first();
        
        if not existed_user:
            raise NotFoundException(f"User with id {user_id}");
        
        # Simply create the post:
        db_post = Post(title=post.title, content=post.content, owner_id=user_id,owner=existed_user)
        db.add(db_post)

    return PostResponse.model_validate(db_post);

# Here we create a restore post services:
def restore_post(db:Session,post_id:int,user_id:int):
    with db.begin():
        # Validate the user_id:
        existed_user = db.query(User).filter(User.id == user_id).first();
            
        if not existed_user:
            raise NotFoundException(f"User with id {user_id}");  
        
        # Validate the post_id:
        existed_post = db.query(Post).filter(Post.id == post_id,Post.is_deleted==True).first();
        
        if not existed_post:
            raise NotFoundException(f"Post with id {post_id}");
        
        # Ownership check:
        
        if existed_post.owner_id != existed_user.id:
            raise InvalidTokenException("You are not authorized to delete this post.")
        
        # Soft delete:
        existed_post.is_deleted = False;
    
    return {"post_id":int(post_id),"status":"Restored"}


# Here we get all posts of a particular user either trashed or not trashed:
def get_posts(db: Session,user_id:int,trashed:bool,skip: int = 0, limit: int = 10):
    
    # Validate the user_id:
    existed_user = db.query(User).filter(User.id == user_id).first();
        
    if not existed_user:
        raise NotFoundException(f"User with id {user_id}");    
    
    if trashed:
        # Get all soft deleted post by that particular user:
        post_Arr = db.query(Post).filter(Post.owner_id == user_id,Post.is_deleted==True).offset(skip).limit(limit).all();
    elif not trashed:
        # Get all post added by that particular user:
        post_Arr = db.query(Post).filter(Post.owner_id == user_id,Post.is_deleted==False).offset(skip).limit(limit).all();
        
    return [PostResponse.model_validate(post) for post in post_Arr]




# Here we updated the post:

def update_post(db:Session,post_id:int,user_id:int,update_body:PostUpdate):
    with db.begin():
        # Validate the user_id:
        existed_user = db.query(User).filter(User.id == user_id).first();
            
        if not existed_user:
            raise NotFoundException(f"User with id {user_id}");  

        # Validate the post_id and owner_id:
        existed_post = db.query(Post).filter(Post.id == post_id,Post.owner_id == user_id,Post.is_deleted == False).first();
        
        if not existed_post:
            raise NotFoundException(f"Post with id {post_id} not found for user {user_id}")
        
        # Serialize the updated_model:
        update_obj = update_body.model_dump(exclude_unset=True);
        
        # Update the existed_post:
        for key, value in update_obj.items():
            setattr(existed_post, key, value);
        
        db.flush();
        db.refresh(existed_post);
    return PostResponse.model_validate(existed_post);
        



# Here we delete the post:

def delete_post(db:Session,post_id:int,user_id:int):
    with db.begin():
        # Validate the user_id:
        existed_user = db.query(User).filter(User.id == user_id).first();
            
        if not existed_user:
            raise NotFoundException(f"User with id {user_id}");  
        
        # Validate the post_id:
        existed_post = db.query(Post).filter(Post.id == post_id,Post.is_deleted==False).first();
        
        if not existed_post:
            raise NotFoundException(f"Post with id {post_id}");
        
        # Ownership check:
        
        if existed_post.owner_id != existed_user.id:
            raise InvalidTokenException("You are not authorized to delete this post.")
        
        # Soft delete:
        existed_post.is_deleted = True;
    
    return {"post_id":int(post_id),"status":"Soft Deleted"}
        
        
# Permanent Delete Trashed Post:

def trash_post(db:Session,post_id:int,user_id:int):
    with db.begin():
        # Validate the user_id:
        existed_user= db.query(User).filter(User.id == user_id).first();
        
        if not existed_user:
            raise NotFoundException(f"User with this id {user_id}");
        
        # Validate post id:
        existed_post = db.query(Post).filter(Post.id == post_id,Post.is_deleted==True,Post.owner_id == user_id).first();
        
        if not existed_post:
            raise NotFoundException(f"Post with id {post_id} for user id {user_id}");
        
        # Delete it permanently:
        
        db.delete(existed_post);
        
        
    return {"post_id":post_id,"status":"Deleted"}
        
        



# Note = 1. Don’t call add() for updates to existing objects — SQLAlchemy is already tracking them.

# 2. Use add() only when you create new objects.

# 3. Use flush() + refresh() only when you need the DB-confirmed updated state before commit.
        
    
    
