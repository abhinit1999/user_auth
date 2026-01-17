from utils.auth import hash_password

class user_schema:
    def __init__(self,username:str,password:str):
        self.username=username
        self.password=hash_password(password)
       
    
    #converting object to MongoDB ready document
    def convert_to_dictionary(self):
        return {
            "username":self.username, # this username is from constructo (which is already been initialized)
            "password":self.password
        }
    





