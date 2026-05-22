sum=0
for k in range(20,1, -1):	
	if(k%2==0):
		#print(f"even no is={k}")
		continue
	print(f"odd no is={k}")
	sum=sum+k
print("sum=",sum)
