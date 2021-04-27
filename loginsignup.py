def check_user(name):
    f=open("userdetails.json","r")
    f1=f.read()
    if name in f1:
        print("name already exist")
        signupwaala()
    else:
        print("valid username")
def check_login(name,password):
    import json
    with open("userdetails.json","r")as f:
        f1=json.load(f)
    for i in f1["user"]:
        if i["name"]==name and i["password"]:
            return "my name is :" ,i["name"]+i["profile"]["description"]+"dob"+i["profile"]["dob"]+"my hobbies"+i["my hobbies"]
    return "invalid user details"
# to chech password is strong or not
def valid_password(password,check_password):
    if '@' in password or '#'  in password:
        i=48
        while i<=57:
            num=chr(i)
            if password ==check_password:
                return "your password is set correct"
            i+1
        else:
            print("the password should contain number also")
            signupwaala()
    else:
        print("the password atleast one special character")
        signupwaala()

# input to dictionary

def dictionary(name,password,profile):
    info_dict={}
    info_dict["name"]=name
    info_dict["password"]=password
    info_dict["profile"]=profile
    return info_dict
# import json

def signupwaala():
    name=input("enter user name")
    password=input("enter password")
    check_password=input("enter password once again")
    valid_password(password,check_password)
    print("congrats",name,"signup is sucessfully")
    description=input("enter the description")
    dob=input("enter your date of birth")
    hobbies=input("enter your hobbies")
    gender=input("enter gender male or female")
    profile={}
    profile["description"]=description
    profile["dob"]=dob
    profile["hobbies"]=hobbies
    profile["gender"]=gender
    info=dictionary(name,password,profile)
    import json
    with open("userdetails.json","r")as f:
        main_dict=json.load(f)
    main_dict["user"].append(info)
    with open("userdetails.json","w")as f:
        json.dump(main_dict,f,indent=4)
    print("signup is done")
def login():
    name=input("enter name")
    password=input("enter password")
    json.dump(main_dict,f,indent=4)
    print(check_login(name,password))
user_wish=input("enter whether you want login or signup")
if user_wish=="signup":
    signupwaala()
else:
    login()