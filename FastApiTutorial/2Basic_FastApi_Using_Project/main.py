from fastapi import FastAPI,Path,Query,HTTPException;
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json;
import uvicorn;

app = FastAPI();


# Function to load data:

def loadData():
    data = None;
    with open("Patients.json","r") as file:
        data = json.load(file);

    return data;

def save_data(data):
    try:

        with open("./Patients.json",'w') as file:
            json.dump(data,file);

    except Exception as e:
        raise HTTPException(status_code=500,detail="Server Error While storing data!Try Again Later.")


@app.get("/")
async def default():
    return {"message:":"Server Starts Serving."}


# 1. Send the patients data:
@app.get("/view")
def view():
    data = loadData();

    return data;

# 2. Send custom patient using path parameters:

# Creating custom error exceptions:
@app.exception_handler(HTTPException)
def custom_Error(request:Request,exc:HTTPException):
    return JSONResponse(status_code=exc.status_code,content={
        "success":False,
        "error":{
            "status_code":exc.status_code,
            "err_message":exc.detail
        }
    })

# Path() = It is a special function in fastapi which is used to provide the metadata,data validation rules in our path parameters like ...,Title,Description,Examples,Min_length,ge,gt,etc.

# Enum = Enum is nothing but a class which inherit from (str,Enum) and it help us to provide the strict value checking for the path and the query parameters as well.It is generally used when you want to accept static or fixed set of values.
from enum import Enum;
class customEnum(str,Enum):
    P001 = "P001"
    P002 = "P002"
    P003 = "P003"
    P004 = "P004"
    P005 = "P005"
    P006 = "P006"
    P007 = "P007"
    P008 = "P008"
    P009 = "P009"
    P0010 = "P0010"

@app.get("/patient/{patient_id}")
def customPatient(patient_id:customEnum = Path(...,Title="Enter patient id",Description="Enter id of the patient you wanna to fetch details:",Examples="P001",Min_length=4,Max_length=4)):
    patients_data = loadData();

    if patient_id in patients_data.keys():
        return JSONResponse(status_code=200,content={
            "success":True,
            "data":patients_data.get(patient_id,"")
        })  

    # It will automatically call the above custome exception function , so that error send in a fixed format always.
    raise HTTPException(status_code=404,detail="Patient not found.");


# 3. Query Parameters= These are the optional or additional key value pair data that are append at the end of the api.

class queryEnum(str,Enum):
    height="height"
    weight="weight"
    bmi="bmi"

@app.get("/sort_patient")
def sort_patient(sort_by:queryEnum = Query(...,title="enter height,weight or bmi"),order:str = Query(default="asc",title="Enter the sorting order.",examples="asc or desc")):
    try:
        data = loadData();
        sortedData = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=True if order == "asc" else False)

        return JSONResponse(status_code=200,content={
            "success":True,
            "data":sortedData
        })
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e));


# 4. Create a new patient and add it:

# Create a pydantic model:
class Patient_Model(BaseModel):
    id:Annotated[str,Field(...,description="Enter unique patient id",examples=["P001"],min_length=4)]
    name:Annotated[str,Field(...,description="Enter patient name",min_length=3,max_length=16)]
    city:Annotated[str,Field(...,description="Enter patient city")]
    age:Annotated[int,Field(...,description="Enter patient age",ge=1)]
    gender:Annotated[Literal['Male','Female','Other'],Field(...,description="Enter patient Gender")]
    height:Annotated[float,Field(...,description="Enter patient height in cm",ge=100)]
    weight:Annotated[float,Field(...,description="Enter patient weight",ge=3)]

    @computed_field
    @property
    def bmi(self)->float:
        return (self.weight/(self.height**2));

    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        

@app.post("/create_patient")
def create_patient(patient:Patient_Model):
    # load old patient:
    data = loadData();

    # Checking the patient:
    if patient.id in data.keys():
        raise HTTPException(status_code=400,detail="Patient already exists.");

    # Storing new patient:
    data[patient.id] = patient.model_dump(exclude=['id']) # serialize the data from pydantic model to python dictonary.

    # Add in the json file:
    save_data(data);

    return JSONResponse(status_code=200,content={
        "success":True,
        "message":"Patient Created Successfully."
    })


# 5. Update the patient data:

class updated_model(BaseModel):
    name:Annotated[str,Field(default=None)]
    city:Annotated[str,Field(default=None)]
    age:Annotated[int,Field(default=None,ge=1)]
    gender:Annotated[Literal['Male','Female','Other'],Field(default=None)]
    height:Annotated[float,Field(default=None,ge=100)]
    weight:Annotated[float,Field(default=None,ge=3)]

@app.put("/patient_update/{patient_id}")
def patient_update(update_data:updated_model, patient_id:str=Path(...,Description="Enter patient id",Min_length=4)):
    # Load existing Data:
    data = loadData()

    # Checking for patient in existing data:
    if patient_id not in data.keys():
        raise HTTPException(status_code=404,detail="Patient not found.")
    
    # fetch the data to be updated:
    oldData = data[patient_id]
    newUpdateData = update_data.model_dump(exclude_unset=True); # here we convert the pydantic model into simple dictionary with only valued field.

    # Just updated the data:
    for key,value in newUpdateData.items():
        oldData[key] = value

    # Pass that updated data to the pydantic model in order to recomputed the field:
    oldData['id'] = patient_id
    updated_pydantic_obj = Patient_Model(**oldData);

    # Serialize the updated pydantic model:
    stored_data=updated_pydantic_obj.model_dump(exclude='id')

    # Store it in the original data set:
    data[patient_id] = stored_data;

    # Just save in the file:
    save_data(data);

    return JSONResponse(status_code=200,content={
        "success":True,
        "message":"Patient Updated Successfully."
    })


# 6. Delete the patient:

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:str=Path(...,Description="Enter patient id",Min_length=4)):
    data = loadData();

    if patient_id not in data.keys():
        raise HTTPException(status_code=404,detail="Patient not found.")
    
    del data[patient_id]

    save_data(data);

    return JSONResponse(status_code=200,content={
        "success":True,
        "message":"Patient Deleted Successfully."
    })


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True);