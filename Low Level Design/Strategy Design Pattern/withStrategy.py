from abc import ABC, abstractmethod

# strategy interface
class PasswordStrategy(ABC):
    @abstractmethod
    def generate(self):   # override this function in each class
        pass

# create class for every possible password inheritng the password strategy class.
class AlphaPasswordStrategy(PasswordStrategy):
    def generate(self):
        return  "abcdefghij"

class NumericPasswordStrategy(PasswordStrategy):
    def generate(self):
        return  "123456789"

class AlphaNumericPasswordStrategy(PasswordStrategy):
    def generate(self):
        return  "abcde12345"
    
class ComplexPasswordStrategy(PasswordStrategy):
    def generate(self):
        return  "abcd_1234@"

class DefaultPasswordStrategy(PasswordStrategy):
    def generate(self):
        return  "abcd123"

# main class
class PasswordGenerator:
    def generatePassword(self, password_gen: PasswordStrategy):   # pass the password strategy you want to use
        return password_gen.generate()   # will call the generate function of 'PasswordStrategy' class that we will pass in the parameter

if __name__ == '__main__':
    pg= PasswordGenerator()
    # password= pg.generatePassword(ComplexPasswordStrategy())   # pass the class name with bracse '()'.
    password= pg.generatePassword(AlphaPasswordStrategy())   # pass the class name with bracse '()'.
    print("Generated Password:-", password)



