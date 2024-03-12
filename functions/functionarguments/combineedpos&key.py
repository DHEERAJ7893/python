# combined both positional and keyword arguments
def cred_trans(*trans,**info):
    # print(trans)
    # print(info)
    amount = 0
    for ele in trans:
        amount += ele
    print(f"Hi {info['name']}, Your have done {len(trans)} transactions for an amount of {amount} an statement for the same has been sent to {info['email']}")
cred_trans(7473,7484,5363,name='sai',email='sai@gmail.com')
cred_trans(5464,744,6337,7383,name='dheeraj',email='dheeraj@gmail.com')