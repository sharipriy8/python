x=int(input("Enter the number :"))
s=0
for i in range(1,x):
	if x%i==0:
		s=s+i
if s==x:
	print(x,"is perfect number")
else:
	print(x,"is not perfect number")
