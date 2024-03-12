# keyword arguments
def emp(name,email,address,location="kadapa"):
    print(f"hi {name} and your email id is {email} and your home in {address} and your location is {location}")
emp(name="sai", address="kolkatta",location='hyd',email='sai@gmail.com')
emp(address="kolkatta",location='hyd',email='sai@gmail.com',name="sai")
emp("sai",address='kadapa',email='sai@email.com')
# emp(address="kolkatta",location='hyd',email='sai@gmail.com',name="sai",state="andhra")    #TypeError: emp() got an unexpected keyword argument 'state'
# emp(name="sai",'sai@gmail.com' ,address="kolkatta",location='hyd')          #SyntaxError: positional argument follows keyword argument
# emp("sai",address='kadapa',email='sai@email.com',address='vizag',name='dheeraj')  #SyntaxError: keyword argument repeated: address
emp(name="sai", address="kolkatta",location='hyd',email='sai@gmail.com')