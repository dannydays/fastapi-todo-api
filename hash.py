from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def verify(password: str, real: str, ):
        return pwd_cxt.verify(password, real)
    def bcrypt(password):
        return pwd_cxt.hash(password)
