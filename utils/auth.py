import jwt
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SECRETE_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


# print(int(time.time()+(60*60)))
def create_jwt(data):
    current_time= int(time.time())
    exp_time = current_time+(60*5)
    
    playload = {
        "data":data,
        "exp_time":exp_time
    }

    return jwt.encode(playload,SECRETE_KEY,ALGORITHM)

def verify_jwt(token):
    decoded_jwt = jwt.decode(token,SECRETE_KEY,ALGORITHM)
    return decoded_jwt


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

