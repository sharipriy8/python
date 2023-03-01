print("Factorial using recursion")
n=int(input("Enter the number :"))
def fact(n):
	if(n==1):
		return 1
	else:
		return n*fact(n-1)
f=fact(n)
print(f)
