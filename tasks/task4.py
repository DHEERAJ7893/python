dict1={}

while True:
    name=input("enter name:")
    mobile=input("enter mobile:")
    if name in dict1:
        print(f"this user already exist do you want update or add for{name}")
        option=input("enter yes to update, no to stop:")
        
        if option=='yes':
            dict1[name].append(mobile)
        else:
            break
        
    else:
        dict1[name]=[mobile]
    print(dict1)    