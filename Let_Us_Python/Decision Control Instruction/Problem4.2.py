# Suppose there are four flags variables w,x,y,z. Write a program to check in multiple ways whether one of them is true.

w,x,y,z = 1,0,1,0

if w==1 or x == 1 or y == 1 or z == 1:
    print("True")

if w or x or y or z:
    print("True")

if any((w,x,y,z)):
    print("True")

if 1 in (w,x,y,z):
    print("True")