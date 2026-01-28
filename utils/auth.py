from datetime import datetime, timezone

import jwt
import time
# Removed unused import
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


# print(int(time.time()+(60*60)))
from datetime import datetime, timezone

def create_jwt(data):
    current_time = int(datetime.now(timezone.utc).timestamp())
    exp_time = current_time + 60

    payload = {
        "data": data,
        "exp": exp_time
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)



def verify_jwt(token):
    try:
        decoded_jwt = jwt.decode(token,SECRET_KEY,ALGORITHM)
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}


# Hashing the password
from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

#encrypting the pass
def hash_password(password:str):
    return password_context.hash(password)

# veryfing Pass
def verify_password(plan_password:str,hashed_password):
    return password_context.verify(plan_password,hashed_password)





# steps to create userAuth System
# 1. User Registration (Sign UP) - userId,password (with validation) - Password would be hashed
# 2. User Login (Sign In) - UserId, password (JWT + sessionID)
# 3. Protected Routes - user can only access the API/page only if he is logged in

