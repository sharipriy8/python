class Rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def rectangle_area(self):
        return self.length*self.breadth
    def rectangle_perimeter(self):
        return 2*(self.length+self.breadth)
    def rectangle_compare(self):
        if x>y:
            print("Area of first is greatest")
        elif y>x:
            print("Area of second is greatest")
        else:
            print("Same area")
print("Enter first rectangle measures")
l1=int(input("Enter the length:"))
b1=int(input("Enter the breadth:"))
rectangle1=Rectangle(l1,b1)
print("Area of first rectangle")
print(rectangle1.rectangle_area())
print("Perimeter of first rectangle")
print(rectangle1.rectangle_perimeter())
print("Enter second rectangle measures")
l2=int(input("Enter the length:"))
b2=int(input("Enter the breadth:"))
rectangle2=Rectangle(l2,b2)
print("Area of second rectangle")
print(rectangle2.rectangle_area())
print("Perimeter of second rectangle")
print(rectangle2.rectangle_perimeter())
print("***Area comparison***")
x=l1*b1
y=l2*b2
compare=Rectangle(x,y)
compare.rectangle_compare()
