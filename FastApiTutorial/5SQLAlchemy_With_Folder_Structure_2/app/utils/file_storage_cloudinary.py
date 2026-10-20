import cloudinary
import cloudinary.uploader
import re
import os
from app.core.config import getenv

cloudinary.config(
    cloud_name=getenv.CLOUDINARY_CLOUD_NAME,
    api_key=getenv.CLOUDINARY_API_KEY,
    api_secret=getenv.CLOUDINARY_API_SECRET,
    secure=True
)

# 1. Helper function to upload any image to cloudinary:
def upload_profile_pic(file_bytes: bytes,user_id: int) -> str:
    result = cloudinary.uploader.upload(file_bytes, folder=f"user_profiles/{user_id}")
    return result["secure_url"]

def extract_public_id(file_url: str) -> str:
    """
    Extracts public_id from a full Cloudinary URL.
    e.g. https://res.cloudinary.com/<cloud_name>/image/upload/v1737891234/folder/filename.jpg
    -> folder/filename
    """
    try:
        # Remove query params if any
        clean_url = file_url.split('?')[0]
        # Remove everything before 'upload/'
        parts = re.split(r'/upload/', clean_url)
        if len(parts) < 2:
            raise ValueError("Invalid Cloudinary URL")
        
        # Remove version prefix like v1737891234/
        public_path = re.sub(r'^v\d+/', '', parts[1])

        # Remove file extension (.jpg, .png, etc.)
        public_id = '.'.join(public_path.split('.')[:-1])
        return public_id
    except Exception as e:
        raise ValueError(f"Cannot extract public_id from URL: {file_url}") from e


def delete_from_storage(file_url: str) -> dict:
    """
    Deletes a file from Cloudinary using its public_id.
    """
    public_id = extract_public_id(file_url)
    result = cloudinary.uploader.destroy(public_id)

    # Cloudinary returns a dict like {'result': 'ok'}
    if result.get("result") != "ok":
        raise RuntimeError(f"Failed to delete image: {result}")

    return result
