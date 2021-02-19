# Question: Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
# Solution 1
def my_solution(x):
    for i in range(1, x):
        x *= i
    return x

# Solution 2
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

x = int(input("Number: "))
a = my_solution(x)
print("Solution 1: ", a)
b = fact(x)
print("Solution 2: ", b)