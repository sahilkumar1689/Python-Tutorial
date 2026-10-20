# In order to validate the data in pydantic model we use two thinks:
# 1. Field() = It is a method comes in the pydantic and used to add the data validation and also the metadata with the field.
# 2. Annotated[] = It is used to combine the type checking and the metadata.Comes with the typing library.And the most preferred way to implement the data validation.

# e.g. = 1. Example of fields method:

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Annotated,Optional

# class PatientData(BaseModel):
#     # ... = It tells that , that particular field is compulsary not optional.If that field is optional then you can set the default value at that point.
#     name:str = Field(...,min_length=3,max_length=16,title="Enter Your Name",description="Patient need to enter thier full name in this field.")
#     age:int = Field(...,gt=0,lt=120,title='enter age',description='age need to be positive')
#     weight:float= Field(...,gt=0,lt=120,title='enter weight',description='weight need to be positive')
#     height:float= Field(...,gt=0,lt=250,title='enter height',description='height need to be positive')
#     email:EmailStr = Field(...,title='enter email',description='email need to be positive')          
#     linkedin_Url:AnyUrl = Field(...,title='enter linkedIn url',description='Enter valid linkedIn url.')
#     gender:Optional[str]= Field(default=None,title='enter gender',description='Enter valid gender.')
#     phone_no:str = Field(...,max_length=10,title='enter phone number',description='Enter valid phone number.')
#     allergies:Optional[List[str]] = Field(default=list,title='enter your allergies',description='Enter your all valid allergies you have in present or past.')
#     other_Details:Optional[Dict[str,str]] = Field(default=dict,title='enter your other inforamtion',description='Enter your all additional information.')


# def get_patient_Info(patient:PatientData):
#     print(f"name: {patient.name}");
#     print(f"Age: {patient.age}");
#     print(f"Weight: {patient.weight}");
#     print(f"Height: {patient.height}");
#     print(f"Email: {patient.email}");
#     print(f"LinkedIn: {patient.linkedin_Url}");
#     print(f"Gender: {patient.gender}");
#     print(f"Phone: {patient.phone_no}");
#     print(f"Allergies: {patient.allergies}");
#     print(f"Other_Info: {patient.other_Details}");

# # 2. Create the instance:
# data_info = {"name":"Akshay","age":24,"weight":65.5,"height":180,"email":"akshay@gmail.com","linkedin_Url":"https://linkedin.com/123","phone_no":"1234567890","allergies":["one","two"]}
# patient = PatientData(**data_info)
    
# get_patient_Info(patient);



# 2. Above Example using Annotated:

class PatientData(BaseModel):
    # ... = It tells that , that particular field is compulsary not optional.If that field is optional then you can set the default value at that point.
    name:Annotated[str,Field(...,min_length=3,max_length=16,title="Enter Your Name",description="Patient need to enter thier full name in this field.")]
    age:Annotated[int, Field(...,gt=0,lt=120,title='enter age',description='age need to be positive')]
    weight:Annotated[float, Field(...,gt=0,lt=120,title='enter weight',description='weight need to be positive')]
    height:Annotated[float, Field(...,gt=0,lt=250,title='enter height',description='height need to be positive')]
    email:Annotated[EmailStr, Field(...,title='enter email',description='email need to be positive')]  
    linkedin_Url:Annotated[AnyUrl, Field(...,title='enter linkedIn url',description='Enter valid linkedIn url.')]
    gender:Annotated[Optional[str], Field(default=None,title='enter gender',description='Enter valid gender.')]
    phone_no:Annotated[str, Field(...,max_length=10,title='enter phone number',description='Enter valid phone number.')]
    allergies:Annotated[Optional[List[str]], Field(default=list,title='enter your allergies',description='Enter your all valid allergies you have in present or past.')]
    other_Details:Annotated[Optional[Dict[str,str]], Field(default=dict,title='enter your other inforamtion',description='Enter your all additional information.')]


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
data_info = {"name":"Akshay","age":24,"weight":65.5,"height":180,"email":"akshay@gmail.com","linkedin_Url":"https://linkedin.com/123","phone_no":"1234567890","allergies":["one","two"]}
patient = PatientData(**data_info)
    
get_patient_Info(patient);

