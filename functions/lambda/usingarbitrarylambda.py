# using arbitrary argument lambda
data = lambda *a,**b:a+(b,)
print(data((4,5,6),b=7))
# print((lambda a,b:a+b)(3,4))
# print(data(3,4))
# print(data(5,6))
print(data((4,5,6),b=7))