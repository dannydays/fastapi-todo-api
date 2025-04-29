from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from JWTtoken import verify_token
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado. Faça login novamente.",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    try:
        return verify_token(data, credentials_exception)
    except JWTError:
        raise credentials_exception