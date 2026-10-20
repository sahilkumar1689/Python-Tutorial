from fastapi import APIRouter, Depends,Path,Body,Query
from sqlalchemy.orm import Session
from app.schemas import post as post_schema
from app.services import post_service
from app.core.database import get_db
from typing import List,Optional,Dict
from app.middleware.auth_verify_middleware import get_current_user
from app.utils.responses import success_response

router = APIRouter()


########## All get endpoints ##########

# Get all user posts with soft delete or withoutsoft delete:
@router.get("/all/{trashed}",response_model=List[post_schema.PostResponse])
def get_posts(trashed:bool=Path(...,description="Enter false for not trashed posts and true for trashed posts."),skip:Optional[int]=None,limit:Optional[int]=None,userpayload:Dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = userpayload.get("user_id",0);
    if skip or limit:
        postArr = post_service.get_posts(db,user_id,trashed,skip or 0,limit or 10,)
    else:
        postArr = post_service.get_posts(db,user_id,trashed)
    
    return success_response(postArr,"Posts send successfully",200)



########## All post endpoints ##########

# Create a post:
@router.post("/create",response_model=post_schema.PostResponse)
def create_post(post:post_schema.PostCreate,userpayload:Dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = userpayload.get("user_id",0);
    post_obj = post_service.create_post(db,post,user_id);
    return success_response(post_obj,"Post Created Successfully",201)


# Restore trashed post:
@router.post("/restore/{post_id}")
def restore_post(post_id:int=Path(...,description="Enter unique post id to restore it."),userpayload:Dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = userpayload.get("user_id",0);
    res = post_service.restore_post(db,post_id,user_id);
    return success_response(res,"Post Restore Successfully",200);
    


########## All put/patch endpoints ##########


# Update a post:
@router.put("/{post_id}",response_model=post_schema.PostResponse)
def update_post(post_id:int=Path(...,description="Enter a unique post id to update"),updated_body:post_schema.PostUpdate=Body(...,embed=False),userpayload:Dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = userpayload.get("user_id",0);
    res = post_service.update_post(db,post_id,user_id,updated_body);
    
    return success_response(res,"Post Updated successfully",200);
    


########## All delete endpoints ##########


# Delete a post:
@router.delete("/{post_id}")
def delete_post(post_id:int=Path(...,description="Enter a unique post id to delete"),userpayload:Dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = userpayload.get("user_id",0);
    res_obj = post_service.delete_post(db,post_id,user_id);
    return success_response(res_obj,"Post Deleted Successfully",200);

# Hard delete a Trash post:

@router.delete("/trash/{post_id}")
def trash_delete(post_id:int=Path(...,description="Enter you unique id to permanent delete the trash."),userpayload:Dict=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = userpayload.get("user_id");
    res_obj = post_service.trash_post(db,post_id,user_id);
    return success_response(res_obj,"Trash Deleted Successfully",200);

