# arbitrary positional arguments
def payment(*trans):
    #  print(trans)
     amount=0
     for ele in trans:
         amount=amount+ele
     print(f"hi sai you done {len(trans)} transations for amount has {amount}")
payment(12,34,56,78)
payment(12,34,56,78,39,3888)
payment(12,34,56,78,2222,333333,22222)