from app.utils.generate_jwt_token import verify_token
from app.utils.exceptions import InvalidTokenException
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# This oauth2_scheme is only used by the swagger UI, to identify them where is the login/register controller path.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Now you can inject this function as a dependencies in any router to protect them:
def get_current_user(token: str = Depends(oauth2_scheme)):
    print("token1: ",token)
    payload = verify_token(token,"auth")
    print("payload1: ",payload);
    if not payload:
        raise InvalidTokenException()
    return {"user_id": int(payload["sub"])}