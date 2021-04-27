import json
def password(n):
    if ("a" in n or "b" in n or "c" in n or "d" in n or "e" in n or "f" in n or "g" in n or "h" in n or "i" in n or "j" in n or "k" in n or "l" in n or "m" in n or "n" in n or "o" in n or "p" in n or "q" in n or "r" in n or "s" in n or "t" in n or "u" in n or "v" in n or "w" in n or "x" in n or "y" in n or "z" in n) and ("A" in n or "B" in n or "C" in n or "D" in n or "E" in n or "D" in n or "E" in n or "F" in n or "G" in n or "H" in n or "I" in n or "J" in n or "K" in n or "L" in n or "M" in n or "N" in n or "O" in n or "P" in n or "Q" in n or "R" in n or "S" in n or "T" in n or "U" in n or "V" in n or "W" in n or "X" in n or "Y" in n or "Z" in n) and ("0" in n or "1" in n or "2" in n or "3" in n or "4" in n or "5" in n or "6" in n or "7" in n or "8" in n or "9" in n) and ("@" in n or "#" in n or "$" in n or "&" in n):
        return True
    else:
        return False
def read_json(filename,u_n):
    f=open(filename,"r")
    data=json.load(f)
    val=data["users"]
    for v in val:
        if u_n==v["name"]:
            return True
    return data
def write_json(filename,data):
    f=open(filename,"w")
    json.dumps(data)
    json.dump(data,f)
def user_exit(filename,u_n,p_w):
    f=open(filename,"r")
    data=json.load(f)
    val=data["users"]
    for v in val:
        if v["name"]==u_n and v["password"]==p_w:
            return True
def print_fun(d1):
    for i,j in d1.items():
        if i=="name":
            print(i,":",j)
        if i=="profile":
            v1=d1[i]
            for p,q in v1.items():
                print(p,":",q)
def l_s():
    a=input("enter login or signup:")
    if a=="signup":
        b=input("enter username:")
        n=input("enter the password:")
        p_w=password(n)
        if p_w==True:
            d=input("conform your password:")
            if n==d:
                d1={"name":b,"password":d}
                d_r=read_json("usersdata.json",b)
                if d_r==True:
                    print('already exist')
                else:
                    d_r["users"].append(d1)
                    print("succesfully signup")
                    d_w=write_json("usersdata.json",d_r)
                    des=input("enter ur discription:")
                    dob=input("enter ur dob:")
                    hob=input("enter ur hob")
                    gender=input("enter ur gender:")
                    d={"discription":des,"dob":dob,"hobbies":hob,"gender":gender}
                    d1.update({"profile":d})
                    d_w=write_json("usersdata.json",d_r)
                    print_fun(d1)
            else:
                print("enter strong password")
    elif a=="login":
        user_name=input("enter the user name:")
        paswrd=input("enter your password:")
        l_g=user_exit("usersdata.json",user_name,paswrd)
        if l_g==True:
            print(user_name,"sucessfully logged in")
        else:
            print("Invalid username and password")
l_s()