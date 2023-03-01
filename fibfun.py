print("Fibonacci series using recursion")
n=int(input("Enter the limit :"))
a=0
b=1
c=0
print(a)
print(b)
def fib(a,b,c,n):
	if(n>0):
		c=a+b
		print(c)
		a=b
		b=c
		n=n-1
		fib(a,b,c,n)
	else:
		return
fib(a,b,c,(n-2))
