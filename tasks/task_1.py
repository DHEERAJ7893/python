pin=int(input("enter atm pin:"))
if pin==7989:
    account=input("enter account type:")
    if account=="savings":
        amount=int(input("enter amount:"))
        if amount>5000:
            print(amount,"has been debited from your account")
        elif amount<5000:
            print("insufficient balance")
        else:
            print("check your balance")
    elif account!="savings":
        print("account not found")
    else:
        ("enetr correct account")
elif pin!=7989:
    print("pin is incorrect")