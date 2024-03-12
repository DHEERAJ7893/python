# without using filter
print(lambda a:a%2==0,[3,4,5,6,7])
# filter lambda
print(list(filter(lambda a:a%2==0,[3,4,5,6,7])))
# by the simple code without using lambda and map in the interna code running 
def sample(a):
    b=[]
    for ele in a:
        if ele%2 == 0:
            b.append(ele+2)
    return b 
print(sample([3,4,5,6,7]))
print([ele+2 for ele in [3,4,5,6,7] if ele%2==0])