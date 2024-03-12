pin = int(input("Enter Pin"))
if pin == 1234:
    account_type = input("Enter account type:")
    if account_type == 'saving':
        amount = input("Enter amount:")
        print(amount+" has been debited from your account....")
    else:
        print("Acount type missed matched!")
else:
    print("Invalid Pin")