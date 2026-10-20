from fastapi.responses import JSONResponse
from .logger import logger
from pydantic import BaseModel

def to_serializable(obj):
    """Recursively convert Pydantic models/lists/dicts into serializable data."""
    if isinstance(obj, BaseModel):
        return obj.model_dump()
    elif isinstance(obj, list):
        return [to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}
    else:
        return obj

def success_response(data=None, message: str = "Success", status_code: int = 200):
    # Generic function used to serialize any type of response data:
    serializable_data = to_serializable(data)

    logger.info(f"Success Response: {message} | Status: {status_code}")
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": serializable_data
        }
    )


# You can also use this function to send the error repsonse but we recommend to use the global error handler with custom exceptions.and this one is used for quick or error response.
def error_response(error: str, status_code: int = 400):
    logger.error(f"{error}");
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": error
        }
    )
