# 13. Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print("""
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)



#  14) Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# from datetime import date
# f_date = date(2024,8,2)
# l_date=date(2014,7,11)
# n_nate=(f_date-l_date)
# print(n_nate)


# # Write a Python program to calculate the difference between a given number and 17. 
# # If the number is greater than 17, return twice the absolute difference

# def difference (n):
#     if n<=17:
#         return 17-n
#     elif n==18:
#         return 17+n
#     else:
#         return(n-17)*2
    
# print(difference(19))



# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000
def difference(n):
    return((abs(1000-n)<=100) or(abs(2000-n)<=100))
print (difference(9989))
