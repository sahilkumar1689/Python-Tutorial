from fastapi import FastAPI
from app.db.session import Base, engine
from app.api.v1.endpoints import user, post

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API")

# Register routers
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def root():
    return {"message": "Welcome to Blog API 🚀"}



    
    
    
    
    



    
