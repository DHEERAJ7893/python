# keyword positional arguments
def cred_trans(**trans):
    print(trans)
    amount = 0
    name = trans.pop('name')
    email = trans.pop('email')
    # print(trans)
    for ele in trans:
         amount = amount + trans[ele]
    # for ele in trans.values():
    #      amount = amount + ele
    print(f"Hi {name}, Your have done {len(trans)} transactions for an amount of {amount} an statement for the same has been sent to {email}")

cred_trans(jan=4343,feb=6747,mar=7484,name='sanjeeva',email='sanjeev@gmail.com')
cred_trans(jan=7484,mar=7484,april=8494,may=6465,name='sanjeeva',email='sanjeev@gmail.com')