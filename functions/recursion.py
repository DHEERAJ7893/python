# recursion functions
# n! = n*(n-1)!
# 6! = 6*(6-1)!
def cal_fact(a):
    if a in [1,0]:
        return 1
    else:
        return a*cal_fact(a-1)
print(cal_fact(8))