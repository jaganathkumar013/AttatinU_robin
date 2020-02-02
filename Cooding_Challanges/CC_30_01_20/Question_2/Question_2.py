

"""s=(input("Enter the numbers & press q to quit"))

if(s!='q'):

    x = [int(x) for x in s.split()] 
   
    print('average of entered numbers is',sum(x)/len(x))
else:
    print('terminated successfully')"""

"""value=int(input("Enter the value for checking product"))
a,b=1,1
while(a<=value):
    b=b*a
    a+=1
    
#print(b)"""
s=(input("Enter the numbers & press q to quit "))

if(s!='q'):
    x=list(map(int,s.split())) 
    print('average of',x,' entered numbers is',sum(x)/len(x))
    a,b,=1,1
    c=0
    
    while(c <=(len(x))):
        print(x)
    c+=1

    


        
            
            
else:
    print('terminated successfully')


    """while(c<=len(x)):
        x[c]=b
        c+=1
    print(x)
    
    
    
    while(a<=x[c]):
    b=b*a
            a+=1
        x[c]=b
        c+=1
    print(x)


    while(c <=len(x)):
        while(a<=x[c]):
            b=b*a
            b+=1
        x[c]=b
        c+=1
    print(x)
    """