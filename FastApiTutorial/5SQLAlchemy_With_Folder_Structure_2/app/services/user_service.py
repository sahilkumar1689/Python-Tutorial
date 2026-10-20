from sqlalchemy.orm import Session
from app.schemas.user import *
from app.models.user import *
from app.utils.hash_password import hash_password,verify_password
from app.utils.exceptions import UserAlreadyExistsException,NotFoundException,InvalidCredentialsException,InvalidTokenException
from app.utils.logger import logger
from app.utils.generate_jwt_token import create_token,verify_token
from app.utils.fastapi_mail import send_reset_email
from ..utils.file_storage_cloudinary import delete_from_storage


# Register User Services:
def create_user(db: Session, user: UserCreate):
    # begin() function is used to handle the rollback or commit automatically, at the end of "with" block if anything happens wrong then it automatically rollback, if not commit.
    with db.begin():
        # Here we check if user exist or not:
        old_user = db.query(User).filter(User.email == user.email).first()
        if old_user:
            raise UserAlreadyExistsException(user.email)
            
        # Simply hash the password before store:
        hashed_password = hash_password(user.password)
        db_user = User(name=user.name, email=user.email,password=hashed_password)
        db.add(db_user)
        db.flush(); # it stores your data temprarely from the sqlAlchemy to db.It make sure that you can easily used any db generated field like primary key,foreign key,etc.After that if any think happens the db.begin() rollback it automatically. 
        # Note = rollback only revert the uncommited changes.
        
        # Simple create the jwt token:
        # 1 day = 24 hours * 60 minutes = 1440 minutes
        jwt_token = create_token({"sub": str(db_user.id)}, 1440, "auth")
    
    return AuthResponse(
        user=UserResponse.model_validate(db_user),
        access_token=jwt_token
    )

# Login User Services:
def user_login(db:Session,user:UserLogin):
    # Now we are check user present or not:
    old_user = db.query(User).filter(User.email == user.email).first();
    if not old_user:
        raise NotFoundException(user.email);
    
    # Now check the password:
    if not verify_password(user.password,old_user.password):
        raise InvalidCredentialsException()
    
    # Now we create the jwt token:
    jwt_token = create_token({"sub":str(old_user.id)},1440,"auth");
    
    return AuthResponse(
        user=UserResponse.model_validate(old_user),
        access_token=jwt_token
    )

# Change Password/forget Password Services:

async def request_change_password(db: Session,req:UserBase2):
    # Find the user:
    existed_user = db.query(User).filter(User.email == req.email).first();
    
    # If not found:
    if not existed_user:
        raise NotFoundException(req.email);

    # Generate random token:
    jwt_token = create_token({"sub":req.email},5,"reset");
    
    # Send link to the email:
    await send_reset_email(req.email,jwt_token); # It is recommended to use background process in order to send the email notification.
    
    # return response:
    return jwt_token;
    
def confirm_change_password(db: Session,req:PasswordResetConfirm):
    with db.begin():
        # Verify the token:
        payload = verify_token(req.token,"reset");
        
        if not payload or not payload["sub"]:
            raise InvalidTokenException("Invalid or expired reset token")

        # Verify the email:
        user = db.query(User).filter(User.email == payload["sub"]).first()
        if not user:
            raise NotFoundException("User not found")

        # Hash the new password:
        user.password = hash_password(req.new_password)

    return user
    
# Sent the particular user details:
def get_user(db: Session,user_id:str):
    if not user_id:
        raise InvalidTokenException();
    
    user_obj = db.query(User).filter(User.id == user_id).first();
    
    if not user_obj:
        raise InvalidTokenException();
    
    return UserResponse.model_validate(user_obj);


# Update the user details:

def update_user(db: Session,user:User,img_url:Optional[str],user_name:Optional[str]):
    # Update the image user if present:
    if img_url:
            
        # delete the previous image from cloud if present:
        if user.bio_img:
            delete_from_storage(user.bio_img);
                
        user.bio_img = img_url;
        
    # Update the user name if present:
    if user_name:
        user.name = user_name;
        
    db.commit()
    db.refresh(user);
    return UserResponse.model_validate(user);

