# As a User need to enter a valid Phone number
import re

def validate():
    num=input("Enter Phone nummber : ")
    string="Your Email is valid : <<email>> "
    pattern="^[9]{1}[1]{1}[ ]{1}[0-9]{10}$"
    if(re.match(pattern,num)):
        strg=re.sub("<<email>>",num,string)
        return strg
    else:
        return "Invalid Name.......Enter a Valid LastName"


print(validate())