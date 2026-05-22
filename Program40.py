# Fibcnacci Series
n=int(input("Enter number:"))
a=0
b=1
count=0
print(a,end=" ")
print(b,end=" ")
while count<n:
    result=a+b
    print(result,end=" ")
    a=b
    b=result
    count=count+1
