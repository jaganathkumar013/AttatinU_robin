"""1) Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

2) Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
Print average and product of all numbers.

3) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

4) Write a Python function that takes a number as a parameter and check the number is prime or not."""

s=(input("Enter the numbers & press q to quit "))

if(s!='q'):
    
   # x = [int(x) for x in s.split()]
    x=list(map(int,s.split())) 
    print('average of',x,' entered numbers is',sum(x)/len(x))
    a,b,c=1,1,0
    while(c<=len(x)):
        while(a<=x[c]):
            b=b*a
            a+=1
            print(b)
        x[c]==b
        c=+1 

        
else:
    print('terminated successfully')
