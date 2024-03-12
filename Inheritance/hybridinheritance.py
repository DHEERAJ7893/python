class GrandFather:
    name = "Vishnu"
    acres = 10

    def info(self):
        return f"Hi {self.name}, You have {self.acres} acres of agricultural land."

class Father(GrandFather):
    # name = "mahesh"
    acres = 13

    def info(self):
        return f"Hi {self.name}, You have {self.acres} acres of land."
    
class Mother:
    name = "Rama"
    acres = 8

    def info(self):
        return f"Hi {self.name} please register you {self.acres} of land."

class Child(Father,Mother):
    # name = "Suresh"
    acres = 5

    def info(self):
        return f"{self.acres} acres of land is registered with your name Mr.{self.name}"

obj1 = Child()

print(obj1.name)
print(obj1.acres)

print(obj1.info())
