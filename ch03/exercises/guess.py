#import muodule/ initialization
import random
#random number generator
ranNum=random.randint(1,10)
flag=False
#user input nunmber
userNum=int(input("Please guess the RNG number from 1 - 10 inclusive: "))
#if statement loop
for i in range(3):
    if (userNum==ranNum):
        print(f"Correct!", "you got the right number in "+[i]+" tries",
        sep="\n")
        flag=True
        break
    if(userNum<ranNum):
        print(f"Too low,"+[i]+" more guesses")
    if(userNum>ranNum):
        print(f"Too high,"+[i]+" more tries")
if(flag is False):
    print(f"The number was "+[ranNum]+" Better luck next time!")
