# return statements by using return in multiple returns
def add(a,b,symbol):
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