#import muodule/ initialization
import random
#random number generator
x = 0
userNum= -1
ranNum=random.randint(1,1000)
flag=False
low=0
high=0
print("the number is: ",ranNum)
#while loop
while(userNum!=ranNum):
    userNum=int(input("Please guess the RNG number from 1 - 1000 inclusive: "))
    x+=1
    if (userNum==ranNum):
        print("Correct!\nyou got the right number in",(x),"guesses ")
        flag=True
        break
    if(userNum<ranNum):
        print("Too low, try again")
    if(userNum>ranNum):
        print("Too high, try again")

# original thought for bonus question
for i in range(1,1000):
    if(ranNum==i):
       print("It should take a maximum of",(i),"guesses to get the random number")

#experiemtal thought for bonus question
x=1
if(ranNum<500):
    for i in range(1,500):
        x+=1
        if(i==ranNum):
            print("It should take a maximum of",(x),"guesses to get the random number")
elif(ranNum>500):
        for i in range(500,1000):
            x+=1
            if(i==ranNum):
                print("It should take a maximum of",(x),"guesses to get the random number")
else:
    print("it should take 500 guesses to get the random number")