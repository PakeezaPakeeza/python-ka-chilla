# num=int(input("enter number you want the table of \n"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")
# l=["pakeeza", "zunaira", "Zeeshan", "saeed"]

# for name in l:
#     if(name.startswith("z" )):
#         print(f"welcome {name}")
i=1
number=int(input("enter number you want table of: \n"))
while(i<11):
    print(f"{number}X{i}={number*i}")
    i=i+1
num=int(input("enter number of your choice to see if number is prime or not: \n"))
for i in range(2, num):
    if(num%i) == 0:
        print("number is not prime beacuse number is not completely divided by 0")
        break
else:
    print("number is prime")
# num=0
# sum=0
# while(num<11):
#     sum=sum+1
#     num=num+1
# print(sum)
