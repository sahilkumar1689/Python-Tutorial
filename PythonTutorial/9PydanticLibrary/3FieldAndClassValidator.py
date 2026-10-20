# 1. Field_Validator = It is used to add some custom validation on a particular field of a class.We can also change the value of that field.It is by default run after the type coersion mode ,but we can change that mode by before.

from pydantic import BaseModel, field_validator,model_validator
from typing import Optional
# class UserDeatils(BaseModel):
#     name:str
#     email:str
    
#     @field_validator("name",mode="after")
#     def toggleCase(cls,value):
#         return value.upper();
        
#     @field_validator("email",mode="after")
#     def validateEmail(cls,value):
#         val = value.split("@")[-1];
#         if val != "gmail.com":
#             raise Exception("Invalid Email.");
        
#         return value;

# def print_user_info(user1:UserDeatils):
#     print(f"Name: {user1.name}");
#     print(f"Email: {user1.email}");

# user1 = UserDeatils(name="Askhay",email="akshay@gmail.com");

# print_user_info(user1);


# 2. Class_validator() = It is used to validate the entire model at ones.It is useful when the custom validation depends on more that one fields.

class UserDeatils(BaseModel):
    name:str
    age:int
    email:str
    phoneNo:str
    emergencyNo:Optional[str] = None
    
    @model_validator(mode="after")
    # def customModel(cls,data):  # you can use this if the mode = "before"
    def customModel(self):
        if self.age >=80:
            if self.emergencyNo == None:
                raise Exception("Emergency Number Required.");
        
        return self;
            
        

def print_user_info(user1:UserDeatils):
    print(f"Name: {user1.name}");
    print(f"Email: {user1.email}");

user1 = UserDeatils(name="Askhay",email="akshay@gmail.com",age=80,phoneNo='123456789',emergencyNo='987654321');

print_user_info(user1);

# Note = Mode attribute only tells that whether we need to do that custom validation before or after the type coersion.