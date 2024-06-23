# counter=0
# while (counter<27):
#     print(counter)
#     counter +=1

    #now make list
class_students= ["julia", "kunwal", "ali"]
test_score=[1,80,50]

#print(f"here is the result :{class_students[1]}, {test_score[1]}")

# automate
user_input=int(input("which student do you want choose from 0 to 2 \n"))
print(f"here is the result :{class_students[user_input]}, {test_score[user_input]}")

#for x in class_students:
#    print(x)
#for y in test_score:
  #  print(y)
for x , y in zip(class_students,test_score):
    print(x,y)