# return statements
def add(a,b,symbol):
    global c
    if symbol == "+":
        c = a+b
    elif symbol == "-":
        c = a - b
    else:
        c = "invalid expression"
    return c
    print("something")
print(add(1,4,'+'))
print(add(3,4,'-'))
print(add(3,4,'*'))