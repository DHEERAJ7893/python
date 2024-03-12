class Employee:

    __name = "ramesh"

    def __init__(self,mobile,email):
        self.__email = email 
        self.mobile = mobile
    
    def info(self):
        return f"Hi {self.name}, your contact info is {self.email} and {self.mobile}"

    def info1(self):
        return f"Hi {self.__name}, your contact info is {self.__email} and {self.mobile}"

    def __info2(self):
        return f"Hi {self.__name}, your contact info is {self.__email} and {self.mobile}"


    def info3(self):
        return self.__info2()

obj = Employee("8383892832","ramesh@gmail.com")

# print(obj.name)
# print(obj.email)
# print(obj.mobile)

# print(obj.info())

# print(obj.__name)
# print(obj.__email)

# print(obj.info1())

# print(obj.__name)

# print(obj.__info2())

# print(obj.info3())

# objname._classname__attributename

print(obj._Employee__info2())

print(obj._Employee__name)