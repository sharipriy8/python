print("Display a number is prime or not")
n=int(input("Enter the number :"))
flag=0
if(n>1):
	for i in range(2,n):
		if(n%i==0):
			flag=1
		break
if(flag==1):
	print(n,"is not prime number")
else:
	print(n,"is prime number")
