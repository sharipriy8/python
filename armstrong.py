print("Armstrong number")
n=int (input("Enter the number :"))
s=0
t=n
while(n>0):
	a=n%10
	s=s+a**3
	n=int(n/10)
if(t==s):
	print(t,"is armstrong number")
else:
	print(t,"is not armstrong number")
