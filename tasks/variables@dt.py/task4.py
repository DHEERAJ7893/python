# Write a Python program to calculate the sum of the digits in an integer.
def sum_of_digits(n):
    num_str = str(n)
    digit_sum = 0
    for char in num_str:
        digit_sum += int(char)
    return digit_sum
    
example = 123456789
print("the number is", example, "is:", sum_of_digits(example))




# def sum_of_digits(n):
#     # Initialize sum
#     digit_sum = 0
    
#     # Iterate through each digit in the number
#     while n > 0:
#         # Add the last digit to the sum
#         digit_sum += n % 10
        
#         # Remove the last digit from the number
#         n = n // 10
    
#     return digit_sum

# # Test the function with an example integer
# example_integer = 1234577777
# print("Sum of digits in", example_integer, "is:", sum_of_digits(example_integer))
