x=list(input("Enter binary number:"))
value=0
for i in range(len(x)):
	digit=x.pop()
	if digit=='1':
		value=value+pow(2,i)
print("Decimal value is :",value)

