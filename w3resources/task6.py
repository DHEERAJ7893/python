# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# list=['3', ' 5', ' 7', ' 23']
# tuple : ('3', ' 5', ' 7', ' 23')
# print(list)
# print(tuple)

values=input("enter the value:")
list=(values.split(","))
tuple=tuple(list)
print('list: ',list)
print('tuple: ',tuple)
