# As a User need to follow pre -defined Password rules.
#Rule2 – Should have at least 1 Upper Case
import re
def validate():
    num=input("Enter Password : ")
    string="Password is valid : <<password>>"
    #pattern="^[A-Za-z0-9]{8,}$"
    pattern="^(?=.*[A-Z])+[0-9a-zA-Z]{7,}$"
    if(re.match(pattern,num)):
        strg=re.sub("<<password>>",num,string)
        return strg
    else:
        return "Password must contain one Uppercase "


print(validate())