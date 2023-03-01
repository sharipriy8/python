print("first and last exchanged")
def swap(a):
	s=a[0]
	e=a[-1]
	x=e+a[1:-1]+s
	print(x)
a=input("Enter the string\n")
swap(a)
