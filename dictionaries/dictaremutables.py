# immutables
# accesing dictionaries
dict1={'name':'dheeraj','email':'dheerajreddy@gmail.com','mobile':'7989594939' ,'name':'sai','city':'kadapa'}
print(dict1)
dict1['state']='hyderabad'
print(dict1)
dict1['city']='kadapa'       #TypeError: 'dict' object is not callable
dict1(print)