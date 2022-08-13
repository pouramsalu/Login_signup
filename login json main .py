# import time
# username=input("enter your username")
# if username=="put your username here":
#     print("checking username")
#     time.sleep(0.5)
#     print("username is right")
#     password=input('type your password here')
#     if password=="put your password here":
#         time.sleep(0.5)
#     else:
#         exit()
# else:
#     exit()

# from unicodedata import name
# from click import option

granted=False
def grant():
    global granted
    granted=True
def login(name,password):
    success=False
    file=open("user_details.txt","r")
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        if (a==name and b==password):
            success=True
            break
        file.close()
        if (success):
            print("login successfully!!")
        else:
            print("wrong username or password")
def register(name,password):
    file=open("user_details.txt","a")
    file.write("/n"+name+","+password)
    file.close()
    grant()
def access(option):
    global name
    if(option=="login"):
        name=input("enter your name:")
        password=input("enter your password:")
        login(name,password)
    else:
        print("enter your name and password to register")
        name=input("enter your name:")
        password=input("enter your password:")
        register(name,password)
def begin():
    global option
    print("welcome to programing language")
    option=input("login or register(login,reg):")
    if(option!="login"and option!="reg"):
        begin()
begin()
access(option)
if(granted):
    print("welcome to programing language")
    print("user details")
    print("username:",name)