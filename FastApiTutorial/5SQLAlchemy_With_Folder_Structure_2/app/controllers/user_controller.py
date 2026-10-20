from fastapi import APIRouter, Depends,Form,File,UploadFile
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.services import user_service
from app.models.user import User
from app.core.database import get_db
from typing import List,Optional,Dict
from app.utils.responses import success_response,error_response
from app.utils.exceptions import FileRelatedExceptions,NotFoundException
from app.utils.logger import logger
from app.middleware.auth_verify_middleware import get_current_user
from ..utils.file_storage_cloudinary import upload_profile_pic,delete_from_storage


router = APIRouter()


# Here we creating a new user:
@router.post("/register",response_model=user_schema.AuthResponse)
def register_user(user: user_schema.UserCreate,db: Session = Depends(get_db)):
    logger.info(f"Attempting to register user: {user.email}")
    user = user_service.create_user(db,user);
    return success_response(user,"User created successfully",200);

# Here we create a login user:
@router.post("/login",response_model=user_schema.AuthResponse)
def login_user(user:user_schema.UserLogin,db: Session = Depends(get_db)):
    logger.info(f"Attempting to login user: {user.email}")
    user = user_service.user_login(db,user);
    return success_response(user,"User logged in successfully",200);


# Here we generate the new passowrd:

@router.post("/request_change_password")
async def request_change_password(req:user_schema.RequestchangeModel,db: Session = Depends(get_db)):
    token = await user_service.request_change_password(db,req);
    logger.info(f"Password reset token created for {req.email}")
    return success_response({"reset_token": token}, "Reset link sent to email")

@router.post("/confirm_change_password")
def confirm_change_password(req: user_schema.PasswordResetConfirm,db: Session = Depends(get_db)):
    user_service.confirm_change_password(db,req);
    logger.info("Password reset successfully")
    return success_response({}, "Password changed successfully")


# Here we return the particular user details with authentication:

@router.get("/user",response_model = user_schema.UserResponse)
def get_user_details(user_details:Dict=Depends(get_current_user),db: Session=Depends(get_db)):
    user = user_service.get_user(db,user_details.get("user_id",""));
    return success_response(user,"User details sends successfully",200);


# Updated controller to change the bio image and user name:

ALLOWED_EXTENSIONS = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB

@router.put("/",response_model=user_schema.UserResponse)
async def update_user(file:UploadFile=File(default=None,alias="bio_img",description="Add your profile pic here."),user_name:str=Form(default=None,description="Enter you new Username here."),user_payload:Dict = Depends(get_current_user),db: Session = Depends(get_db)):
    user_id = user_payload.get("user_id","");
    
    # 1. Firstly check the user_id:
    existing_user = db.query(User).filter(User.id == user_id).first();
    
    if not existing_user:
        raise NotFoundException("User with id {user_id}");
    
    # 2. After that upload the image on cloud if present:
    img_url = None;
    
    if file:
        # 1. Check the file type:
        if file.content_type not in ALLOWED_EXTENSIONS:
            raise FileRelatedExceptions(f"Invalid file type. Allowed file types are: {ALLOWED_EXTENSIONS}")

        # 2. Check the file size:
        file_bytes = await file.read(); 
        
        if len(file_bytes) > MAX_FILE_SIZE:
            raise FileRelatedExceptions(f"File is too large.Max size is: {MAX_FILE_SIZE/1024/1024} MB");

        # 3. Store on cloudinary:
        img_url = upload_profile_pic(file_bytes,user_id);
    
    # Doing all the db process:
    res = user_service.update_user(db,existing_user,img_url,user_name);
    return success_response(res,"Details Updated Successfully",200);
    
        
        
