print("Simple calculator")
a=int(input("Enter the no. a="))
b=int(input("Enter the no. b="))
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
choice=int(input("Enter your choice :"))
if(choice==1):
	print(a,"+",b,"=",a+b)
elif(choice==2):
	print(a,"-",b,"=",a-b)
elif(choice==3):
	print(a,"*",b,"=",a*b)
elif(choice==4):
	print(a,"/",b,"=",a/b)
else:
	print("Invalid choice")
