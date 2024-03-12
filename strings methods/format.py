# message=("use this otp 657687 for your website amazon.com for an amount rs.678/- only")
# print(message)
# message=("use this otp {} for your website {} for an amount rs.{}/- only").format(745677,'flipkart.com',676)
# print(message)

otp=input("enter the otp:")
website=input("enter the website:")
amount=input("enter the amount:")
message=("use this otp {} for your website {} for an amount rs.{}/- only").format(otp,website,amount)
print(message)
message=("use this otp {otp} for your website {website} for an amount rs.{amount}/- only").format(otp=otp,website=website,amount=amount)
print(message)
message=f'use this otp {otp} for your website {website} for an amount rs.{amount}/- only'
print(message)