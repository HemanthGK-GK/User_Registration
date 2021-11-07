#As a User need to enter a valid First Name
import unittest
import re

def chkName(name):
    string="Hello <<username>>, How are you"
    pattern="^[A-Z]{1}[a-z]{2,}$"  #Pattern for FirstName
    if(re.match(pattern,name)):#checking condition
        strg=re.sub("<<username>>",name,string) #replacing Name 
        return strg
    else:
        return "Invalid Name.......Enter a Valid FirstName"

class NewwTest(unittest.TestCase):

    def test_Fname(self):
        #Arrange 
        Fname="Hemanth"
        string="Hello Hemanth, How are you"
        #Act
        result=chkName(Fname)
        #Assert
        self.assertEqual(result,string,"TestCase Failed")

if __name__=="__main__":
    unittest.main()

        
Fname=input("Enter First Name : ")
chkName(Fname)

