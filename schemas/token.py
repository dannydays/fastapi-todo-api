from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, List



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    is_admin: Optional[bool] = None