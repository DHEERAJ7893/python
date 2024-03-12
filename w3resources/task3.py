# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime
new_date='2014-07-05 14:34:14'
converted=datetime.strptime(new_date,"%Y-%m-%d %H:%M:%S")
print(converted)