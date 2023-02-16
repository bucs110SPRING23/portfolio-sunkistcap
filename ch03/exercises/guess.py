#import muodule/ initialization
import random
#random number generator
ranNum=random.randint(1,10)
flag=False
print("the number is: ",ranNum)
#for range statement loop
for i in range(3):
    userNum=int(input("Please guess the RNG number from 1 - 10 inclusive: "))
    if (userNum==ranNum):
        print("Correct!\nyou got the right number in ",(i+1),"out of 3 guesses ")
        flag=True
        break
    if(userNum<ranNum):
        print("Too low,",(i+1),"out of 3 tries")
    if(userNum>ranNum):
        print("Too high,",(i+1),"out of 3 tries")
if(flag is False):
    print("The number was ",ranNum," better luck next time!")