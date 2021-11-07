# As a User need to follow pre -defined Password rules.
#Rule1– minimum 8 Characters
import re

def validate():
    num=input("Enter Password : ")
    string="Password is valid : <<password>>"
    #pattern="^[A-Za-z0-9]{8,}$"
    #pattern="^(?=.*[A-Z])+[0-9a-zA-Z]{7,}$"
    #pattern="^(?=.*[A-Z])(?=.*[0-9])[0-9a-zA-Z]{8,}$"
    pattern="^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-])[0-9a-zA-Z]{8,}$"
    if(re.match(pattern,num)):
        strg=re.sub("<<password>>",num,string)
        return strg
    else:
        return "Password must contain 8 character \nPassword must contain one Uppercase \nPassword must contain one numeric \nPassword must contain one special case"


print(validate())