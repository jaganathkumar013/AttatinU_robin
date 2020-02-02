#1) Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a) 

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
print("gcd(", a , "," , b, ") = ", gcd(a, b))