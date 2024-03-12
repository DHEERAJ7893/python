# return statements
def add(a,b,symbol):
    if symbol == "+":
        return a+b
    elif symbol == "-":
        return a-b
    else:
        return "invalid expression"
    print("something")
print(add(1,4,'+'))
print(add(3,4,'-'))
print(add(3,4,'*'))