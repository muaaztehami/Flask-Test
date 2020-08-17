from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1,'admin', 'admin123')
]
username_mapping = {u.username: u for u in users}
uid_mapping = {u.id: u for u in users}

def auth(username,password):
    user = username_mapping.get(username,None) #check if username exists 
    if user and safe_str_cmp(user.password,password): #check if user exist and pass matches
        return user 

#identity function to keep track of loggedin user
def identity(payload):
    user_id = payload['identity']
    return uid_mapping.get(user_id,None)
