# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java


value=input("enter the file name:")
splits=(value.split("."))
print('the extended output is:' + splits[0])