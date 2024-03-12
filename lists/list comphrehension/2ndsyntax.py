# looping
list1=[12,34,5,6,66,78,12,70]
list2=[]
for ele in list1:
    if ele%2==0:
     list2.append(ele+2)
print(list2) 

# comphrehension
list3=[ele+2 for ele in list1 if ele%2==0]
print(list3)