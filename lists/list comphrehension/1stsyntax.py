# looping
list1=[12,34,443,22,443,222,566,6778,98]
list2=[]
for ele in list1:
     list2.append(ele+2)
print(list2)


# comprehension
list1=[12,34,443,22,443,222,566,6778,98]
# list2=[]
list2=[ele+2 for ele in list1]
print(list2)