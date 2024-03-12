# # Python: Calculate the sum of three given numbers, if the values are equal then return thrice of their sum

# def sum1(x,y,z):
#     sum=x+y+z
#     if x==y==z:
#         sum=sum*3
#     return sum
# print(sum1(3,2,4))

# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
# Return the string unchanged if the given string already begins with "Is".

def string(text):
    if  len(text)<=2 and text[:2]=="Is":
        return text
    else:
       return "is"+text
print(string("array"))
