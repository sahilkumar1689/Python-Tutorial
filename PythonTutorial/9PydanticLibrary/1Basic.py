# Pydantic = It is a very populary python library , particularly used for data type checking , data validation and serializability.
# Bascially we know that python is a dynamic typed language , it means type checking occur at run time so its very difficult to key the data validation and type checking. So in order to solve this problem we use pydantic:
# 1. In which we create the pydantic models which are nothing but the python classes that inherit the "BaseModel" from the pydantic library and inside that model what we simply uses the python type hints to define the shape of the data.
# 2. After that we simply create the instance of that pydantic model and pass data to it. After that pydantic automatically validate the input data,convert into the compatible type and also raises error if data is incorrect.

# e.g. = 1. Simple type checking in pydantic models:
 
 
from pydantic import BaseModel,AnyUrl,EmailStr;
from pydantic_settings import BaseSettings;
from typing import List,Dict,Optional,Union,Literal;

# 1. Create the model:
class PatientData(BaseModel):
    name:str
    age:Union[int,str]            # It is used to take any one of the data type
    weight:float
    height:float
    email:EmailStr                # Special data type used for emails
    linkedin_Url:AnyUrl           # Special data type used for urls
    gender:Optional[str]=None     # here we make any field optional but we need to gave default value to it
    phone_no:str 
    allergies:Optional[List[str]] = list
    other_Details:Optional[Dict[str,str]] = dict
    # mode:Literal["success","false"]       # literal is used to create the fixe choice 
    
def get_patient_Info(patient:PatientData):
    print(f"name: {patient.name}");
    print(f"Age: {patient.age}");
    print(f"Weight: {patient.weight}");
    print(f"Height: {patient.height}");
    print(f"Email: {patient.email}");
    print(f"LinkedIn: {patient.linkedin_Url}");
    print(f"Gender: {patient.gender}");
    print(f"Phone: {patient.phone_no}");
    print(f"Allergies: {patient.allergies}");
    print(f"Other_Info: {patient.other_Details}");

# 2. Create the instance:
data_info = {"name":"Akshay","age":24,"weight":65.5,"height":180,"email":"akshay@gmail.com","linkedin_Url":"https://linkedin.com/123","phone_no":"123456789","allergies":["one","two"]}
patient = PatientData(**data_info) # always remember pydantic model only contains the keyword arguments.
    
get_patient_Info(patient);
    
    
    
# e.g. = 2. BaseSettings model = It is used to create the settings model that automatically load all the environment variable from the env file.
    
    
class settings(BaseSettings):
    PORT:int
    URL:str
    
    class Config:
        env_file = ".env"
    

settings = settings();

print(settings.PORT);
print(settings.URL);
    
    