class LargerError(Exception):
    pass

class SmallerError(Exception):
    pass

import random
num1 = random.randint(100,600)
while True:
    try:
        num2 = int(input("Enter your value:"))
        if num2 > num1 : 
            raise LargerError
        elif num2 < num1:
            raise SmallerError
        else:
            print("Number guessed!")
            break
    except LargerError:
        print("Entered value is larger try will smaller value")
    except SmallerError:
        print("Entered value is smaller try will larger value")
    except:
        print("Invalid value, please pass correct values.")
        break
