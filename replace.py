print("Replace with dollar")
a=input("Enter the word\n")
t=a[0]
for i in range(len(a)):
	if(a[i]==a[0]):
		x=(a.replace(a[i],"$"))
		break
print(t+x[1:])
