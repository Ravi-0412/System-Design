class PasswordGenerator:
    def generatePassword(self, password_type= 'mix'):
        if password_type== 'numeric':
            return "12345678"
        elif password_type== "mix":
            return "abcd1234"
        else:
            return  "abcdefghh"
    
if __name__ == '__main__':
    pg= PasswordGenerator()
    password= pg.generatePassword('complex')
    print("Generated password:- ", password)


# suppose we want to add some more password type then we have to modify the curr function.
# but it is not a good way since for new requirement we will have to modify the curr function always.