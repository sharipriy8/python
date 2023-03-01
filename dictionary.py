n=int(input("how many records"))
d={}
for i in range(n):
 name=input("Enter name: ") 
 marks=int(input("Enter marks: "))
 rank=int(input("enter the rank"))
 d[rank]=[marks,name] 
print("Descending order") 
print(sorted(d.values(), reverse=True)) 
print("Ascending order") 
print(sorted(d.values()))

