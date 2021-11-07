# As a User need to enter a valid email
import re

def validate(email):
    string="Your Email is valid : <<email>> "
    pattern="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if(re.match(pattern,email)):
        strg=re.sub("<<email>>",email,string)
        return strg
    else:
        return "Invalid Name.......Enter a Valid Email"

    
email=input("Enter Email : ")
print(validate(email))
