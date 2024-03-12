count = 0
while count<=2:
    pin = int(input("Enter Pin"))
    if pin == 1234:
        account_type = input("Enter account type:")
        if account_type == 'saving':
            amount = input("Enter amount:")
            print(amount+" has been debited from your account....")
            break
        else:
            print("Acount type missed matched!,Try Again")
            count+=1
    else:
        print("Invalid Pin,Try agin")
        count+=1
else:
    print("Account Blocked for 24 hours")
# if count == 3:
#     print("Account Blocked for 24 hours")