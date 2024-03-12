# altering methods
list=[12,13,14,12,88,35,6]
list1=list
print(list)
print(list1)
list1.append(3)     #without using copy() method
print(list)
print(list1)


#with using copy() method

list=[12,13,14,12,88,35,6]
list1=list.copy()
# print(list)
# print(list1)
list1.append(3)    
list1.append('java')  
print(list)
print(list1)