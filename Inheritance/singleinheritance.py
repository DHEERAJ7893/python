class Father:
    name = "mahesh"
    acres = 13

    def info(self):
        return f"Hi {self.name}, You have {self.acres} acres of land."
    

class Child(Father):
    name = "Suresh"
    # acres = 5
    
    # class Child:
    # name = "Suresh"
    # acres = 5

    def info(self):
        return f"{self.acres} acres of land is registered with your name Mr.{self.name}"

obj1 = Child()

print(obj1.name)
print(obj1.acres)

print(obj1.info())