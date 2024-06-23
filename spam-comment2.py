p1="make a lot of money"
p2="buy now"
p3="subscribe this channel"
p4="click this"
message=input("enter your comment  ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("spam message: ")
else:
    print("this is not spam:")
username=input("enter username :")
if(len(username)<10):
    print("your username is less tha 10 char")
else:
    print("all is well")
newlist=["pakeeza","zeeshan","usama","jilna"]
name=input("enter your nice name: \n")
if(name in newlist):
    print("you belong to group")
else:
    print("your name is not in the list")