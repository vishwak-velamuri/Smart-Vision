from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def auth_middleware(request: Request):
    token = request.headers.get("Authorization")
    if token is None:
        raise HTTPException(status_code=401, detail="Authorization token missing")
    
    # Here you would normally verify the token
    if token != "your_secret_token":  # Replace with actual token verification
        raise HTTPException(status_code=403, detail="Invalid authentication credentials")