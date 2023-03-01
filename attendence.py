n=int(input("how many records"))
d={}
for i in range(n):
 name=input("Enter name: ") 
 attendence=int(input("Enter attendence: "))
 d[name]=[attendence]  
print(sorted(d.values()))  
