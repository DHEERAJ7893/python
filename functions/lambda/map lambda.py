#  without map lambda 
print(lambda a:a+2,[3,4,5,6,7])
# map lambda 
print(list(map(lambda a:a+2,[3,4,5,6,7])))
# by the simple code without using lambda and map in the interna code running 
def sample(a):
    b=[]
    for ele in a:
        b.append(ele+2)
    return b 
print(sample([3,4,5,6,7]))
print([ele+2 for ele in [3,4,5,6,7]])