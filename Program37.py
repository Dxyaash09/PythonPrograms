n=int(input("Enter any mumber"))
fact=1
if(n<0):
    print("we cannot calculate the factorial")
elif(n==0):
    print(f"factorialof{n}is{fact}")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial is {fact}")
#fact*=i                 
