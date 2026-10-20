from pydantic import BaseModel, EmailStr,Field
from typing import Annotated,Optional

# Basis User Models:
class UserBase(BaseModel):
    name: Annotated[str,Field(...,min_length=3,max_length=16,description="User name between 3 to 16 characters.")]
    email: Annotated[EmailStr,Field(...,description="User email address.")]

class UserBase2(BaseModel):
    password: Annotated[str,Field(...,min_length=6,max_length=10,description="User password between 6 to 10 characters.")]

# Model to create the user:
class UserCreate(UserBase,UserBase2):
    pass;
    
# Basic Model for the user response:
class UserResponse(UserBase):
    id: int
    bio_img: Annotated[Optional[str],Field(default=None)]

    class Config:
        from_attributes = True

# Model for login details:
class UserLogin(UserBase2):
    email: Annotated[EmailStr,Field(...,description="User email address.")]

# Model for the actual response:
class AuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    token_type: str = "bearer"
    
    class Config:
        from_attributes = True
    
# Model for confirm reset password request:

class RequestchangeModel(BaseModel):
    email: Annotated[EmailStr,Field(...,description="User email address.")]    

class PasswordResetConfirm(BaseModel):
    token: str
    new_password: Annotated[str, Field(..., min_length=6, max_length=10)]

# Note = 1. You only need to add below code in the response model not in the request model:
#   "class Config:
        # from_attributes = True""
