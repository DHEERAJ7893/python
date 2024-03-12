# looping
list1=[12,34,5,6,66,78,12,70]
list2=[]
for ele in list1:
    if ele%2==0:
     list2.append(ele+2)
    else:
        list2.append(ele+3)
print(list2) 

# # comphrehension
# list3=[ele+2 if ele%2==0 else ele+3 for ele in list1]
# print(list3) 