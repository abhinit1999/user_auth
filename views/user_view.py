from fastapi import APIRouter,Request,Response, Depends
from controllers.user_controller import register_user,login_user
from utils.auth import verify_jwt


router = APIRouter()

# auth Dependency - This is to get the current user (returns true or false)
def get_current_user(request:Request):

    # Get JWT token From browser cookies
    token = request.cookies.get("session")

    # if token not found
    if not token:
        return {"error":"User Not logged In"}
    
    #Verifying JWT
    user_data = verify_jwt(token)

    # if token is invalid or expired
    if not user_data:
        return {"error":"invalida or expired token"}
    return user_data

# from fastapi import Request, HTTPException, status

# def get_current_user(request: Request):
#     # Get JWT token from browser cookies
#     token = request.cookies.get("session")

#     # if token not found
#     if not token:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="User not logged in"
#         )
    
#     # Verifying JWT
#     user_data = verify_jwt(token)

#     # if token is invalid or expired
#     if not user_data:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token"
#         )

#     return user_data


# this is for user login and creating the Cookies/session

@router.post("/login")
def login(username:str,password:str,response:Response):
    result = login_user(username,password)
    if "error" in result:
        return result
    # save JWT token in HTTP only cookie
    response.set_cookie(
        key="session",
        value=result["token"],
        httponly=True

    )
    
    return {"message":"LoggedIn Successfully"}

# this is to inserting/creating the new user record
@router.post("/register")
def register(username:str,password:str):
    return register_user(username,password)


#protected Route
@router.get("/profile")
def user_profile(user = Depends(get_current_user)):
    print(f"current User: {user}")
    if "error" in user:
        return user
    print(f"error")
    return {"message":f"welcome to the profile {user}"}

# @router.get("/profile")
# def user_profile(user = Depends(get_current_user)):
#     print(f"current User: {user}")
#     return {"message": f"welcome to the profile {user}"}

    

# this is to logging out the user 
@router.post("/logout")
def logout(response:Response):
    response.delete_cookie("session")
    return {"message":"logged Out Successfully"}



