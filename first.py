
print("Enter length and breadth of a square or reactangle to get its area , perimeter and diagonal")
a= int((input("Enter length : "))) #to enter a value after running a code we use input()
b= int((input("Enter breadth : "))) #to turn the vale from string to integer use int()
ar= (a*b)
p= (2*(a+b))
d= (((a**2)+(b**2))**0.5)
print("Area: ",ar)
print("Perimeter: ",p)
print("Diagonal: ",d)
