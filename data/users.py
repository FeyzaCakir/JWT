import bcrypt

class User:
    def __init__(self,user_id,email,password):
        self.id=user_id
        self.email=email
        self.password=password #düz metin

users=[]

def add_user(email,password):
    if find_user_by_email(email):
        return None
    new_id=len(users)+1
    
    hashed_password=bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    
    user=User(new_id,email,hashed_password)
    users.append(user)
    return user

   
def find_user_by_id(user_id):
    for user in users:
        if user.id==user_id:
            return user
    return None
    
def find_user_by_email(email):
    for user in users:
        if user.email==email:
            return user
    return None

add_user("lala@gmail.com","1234")
print(users)