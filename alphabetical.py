print("Alphabetical name list")
data = []
a=int(input("Enter the no. of inputs :"))
for i in range (a):
	name=input("Enter the name :")
	data.append(name)
	data.sort()
print(data)
