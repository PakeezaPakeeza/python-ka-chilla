a=int(input("enter num 1: "))
b=int(input("enter num 2: "))
c=int(input("enter num 3: "))
d=int(input("enter num 4: "))
if(a>b and a>c and a>d):
    print("Greatest number is a:",a)
elif(b>a and b>c and b>d):
    print("Greatest number is b:",b)
elif(c>b and c>a and c>d):
    print("Greatest number is c:",c)
elif(d>b and d>c and d>a):
    print("Greatest number is d:",d)