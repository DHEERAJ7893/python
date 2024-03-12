class Parent:
    name="mahesh"
    acres = 15

    def check(self,data):
        self.acres = self.acres+data
        return self.acres
    
class Child1(Parent):
    name = "suresh"
    # acres = 6

class Child2(Parent):
    name = "Venkat"
    acres = 3


obj1 = Child1()

print(obj1.name)


obj2 = Child2()

print(obj2.name)
print(obj1.check(5))

obj2.acres = obj1.acres

print(obj2.check(7))