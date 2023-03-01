print("Power using recursion")
n=int(input("Enter the number :"))
p=int(input("Enter the power :"))
def power(n,p):
	if(p==1):
		return n
	else:
		return n*power(n,(p-1))
a=power(n,p)
print(n,"^",p,"=",a)
