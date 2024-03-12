# tuples has only two methods
# print(dir(tuple))
# 1.count
# 2.index

# 1.tuple
tuple=(1,2,33,'java','python','codes',99,30)
print(tuple.index('java'))
print(tuple.index(99))

#2.count
tuple=(1,2,33,'java','python','codes','java',99,99,99,30)
print(tuple.count('java'))
print(tuple.count(99))
