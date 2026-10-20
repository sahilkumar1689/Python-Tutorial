import uvicorn
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.core.database import Base, engine
from app.api.v1.routes import api_router
from app.utils.exceptions import *
from app.middleware.logging_middleware import LoggingMiddleware
from app.utils.logger import logger
from fastapi.middleware.cors import CORSMiddleware
import traceback



# Create tables
Base.metadata.create_all(bind=engine)

# Create the app reference:
app = FastAPI(title="Blog API")


# CORS handling:
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add logging middleware for request/response:
app.add_middleware(LoggingMiddleware);


# Add versioning register routes:
app.include_router(api_router, prefix="/api/v1")



# Global Error handler:
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"Error at {request.method} {request.url} | {repr(exc)}",
        exc_info=True  # <-- full stack trace
    )
    # Handle custom exceptions (already subclasses of HTTPException)
    if isinstance(exc, (UserAlreadyExistsException, InvalidCredentialsException, NotFoundException,InvalidTokenException)):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail}
        )

    # Unexpected server errors
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "details": str(exc)}
    )

# Default router:
@app.get("/")
def root():
    return {"message": "Welcome to Blog API 🚀"}

