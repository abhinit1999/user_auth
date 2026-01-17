from utils.db import user_collection
from models.user_model import user_schema
from utils.auth import create_jwt,verify_password

def register_user(username:str, password:str):

    # check if username already exists in DataBase
    check_existing_user = user_collection.find_one({"username":username})
    if not check_existing_user:   

        # inserting the user records     
        user_collection.insert_one(user_schema(username,password))
        return {"message":"User Created"}
    else:
        return {"message":"User already exists"}
    

def login_user(username:str, password:str):

    #Fetching user records from DataBase
    user = user_collection.find_one({"username":username})
    if not user:
        return {"error":"Invalid username"}
    #Verifying the user Plan-password and Bcrytpted password
    validating_paasword = verify_password(password,user['password'])
    
    if not validating_paasword:
        return {"error":"Password"}
    
    # creatring JWT token for authenticated user only
    token = create_jwt({"username":username})

    return {"token":token}
    
    
    


