# Question: Write a program that calculates and prints the value according to the given formula: 
# Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18,22,24
import math

class Formula():
    # Global variables
    C = 50
    H = 30
    def __init__(self):
        self.d = input()
        
    def split_d(self):
        x = []
        a = self.d.split(",")
        for i in range(len(a)):
            x.append(int(a[i]))
        return x
    
    def calculate(self, x):
        Q = math.sqrt(2 * self.C * x / self.H)
        return Q
    
    def printAnswer(self):
        l = []
        x = self.split_d()
        for i in x:
            l.append(str(round(self.calculate(i))))
        print(",".join(l))

obj = Formula()
obj.printAnswer()