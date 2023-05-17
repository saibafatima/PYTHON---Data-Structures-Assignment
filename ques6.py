# Q6. What is a complex number in mathematics, and how is it represented in Python?

# Creating a complex number
z = 2 + 3j

# Accessing real and imaginary parts
real_part = z.real
imaginary_part = z.imag

print(real_part)         # Output: 2.0
print(imaginary_part)    # Output: 3.0

# Performing complex arithmetic
w = 1 - 2j
sum_result = z + w
product_result = z * w

print(sum_result)        # Output: (3+1j)
print(product_result)    # Output: (8-1j)
