# As a User need to follow pre -defined Password rules.
#Rule4 – Has exactly 1 Special Character
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
        return "Password must contain one Special symbol Value"


print(validate())