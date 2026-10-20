# FastApi = It is a modern , high performance web framework for building API's with python.It automatically provide the data validation , serialization and documentation.
# It internally used two python libraries:
# 1. Starlette = It is a lightweight ASGI protocol library.It manages how your api receive request and sends back responses.
# 2. Pydantic = It is used to check if the data coming into your api is in correct format or not.

# SGI = It stands for the server gateway interface.It is nothing but a standard protocol used by the python to communicate between the wen server and the python we application.
# Types:
# 1. WSGI = Stands for web server gateway interface.It is the old protocol used to create the synchronous apps in flask/django.Generally known for its stability.But because it is synchronous it is very difficult to use websocket.
# 2. ASGI = Stands for asynchronous server gateway interface.It is modern protocol used to create the asynchronous and synchronous application.Generally known for its high performance and because it is asynchronous we can also implement the websocket.

# Web server used in python= Python generally used two servers:
# 1. Gunicorn = It is a synchronous server implemented with the WSGI protocols.
# 2. Uvicorn = It is a asynchronous server implemented with the ASGI protocols.

# Note = 1. In python we use starlette for ASGI and werkzuke for WSGI protocol implementation.
# 2. WorkFlow in fastApi is = webserver/Uvicorn -> Starlette/ASGI -> python Code



# e.g. = Create a basic server with default endpoint:
from fastapi import FastAPI;
import uvicorn;

# Create an app instance by using which we can create all the endpoint:
app = FastAPI();


# Use app instance as a decorator in order to with "get" method.
@app.get("/")
async def default():
    return {"message:":"Server Starts Serving."}



# If you wannt you can run server like this, it will automatically starts the server when any one run this file. Or either you can run this command in the terminal "uvicorn main:app --reload"
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True);

