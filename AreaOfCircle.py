#TASK 1: write a Python program which accepts the radius of a circle from the user and computes area.
#Radius Input
r=float(input("Enter radius of the circle "))

#Area of circle
import math
a=math.pi*(r**2)
print("Area of circle is "+str(a))

#TASK 2:Your second task now is to write a Python program to accept a filename from
#the user and print the extension of that.
file=input("Input filename: ")
FileEx=file.split(".")
print("The extenstion of the the file is: "+repr(FileEx[-1]))
