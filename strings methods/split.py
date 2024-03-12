#split()
str="python is a programming language"
print(str.split())
print(str.split('og'))
print(str.split('m'))

# email="dheerajreddy@gmail.com"
# print(email.split())
# print(email.split('@'))

email="dheeraj.reddy@gmail.com"
username=email.split("@")
print(username)
username=email.split("@")[0]
print(username)
name=username.split(".")
print(name)