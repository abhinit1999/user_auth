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

