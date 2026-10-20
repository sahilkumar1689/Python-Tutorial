# Nested Models = It is a model in which one pydantic field in itself has another pydantic model in a hierarchical fashion.
# It is very usefull in order to create the schema design where data are connected with each other.

from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int

class Cart(BaseModel):
    cart_id: str
    products: List[Product]  # ✅ list of nested models

class User(BaseModel):
    user_id: str
    name: str
    email: str
    cart: Cart  # ✅ nested model
    

pr1 = Product(product_id="12",name='laptop',price=100000,quantity=1);

crt1 = Cart(cart_id='1',products=[pr1]);

user1 = User(user_id='1',name='Akshay',email='akshay@gmail.com',cart=crt1);

print(user1.model_dump());

