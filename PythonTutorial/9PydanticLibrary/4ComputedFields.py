# 1. Computed Fields = These are those fields which cannot come from the input data, but we can calculate it dynamically on the basis of other fields values.And also use them as normal fields.

from pydantic import BaseModel,computed_field

class Rectangle(BaseModel):
    height:float
    width:float
    
    @computed_field
    @property
    def area(self)->float: # important to tell the return type
        return self.height * self.width;

rec1 = Rectangle(height=10,width=20);

print(rec1.model_dump());

