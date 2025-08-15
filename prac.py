l=float(input("Length of the cuboid:"))
b=float(input("Breadth ofthe cuboid:"))
h=float(input("Height of the cuboid:"))

TSA = 2*(l*b + b*h + l*h)
v=l*b*h
print("Total Surface Area of cuboid =",TSA)
print("Volume of cuboid =",v)