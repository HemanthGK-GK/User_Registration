#As a User need to enter a valid Last Name - Last name starts with Cap and has minimum 3 characters
import re

from User_Reg.phNum import validate

def validate(name):
    string="Your last Name is : <<username>>"
    pattern="^[A-Z]{1}[a-z]{2,}$"  
    if(re.match(pattern,name)):
        strg=re.sub("<<username>>",name,string)
        return strg
    else:
        return "Invalid Name.......Enter a Valid LastName"

    
lName=input("Enter Last Name : ")
print(validate(lName))