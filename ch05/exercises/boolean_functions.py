def percentage_to_letter(score=0):
    if (score<60):
        return("F")
    elif(score>=60 and score <70):
        return("D")
    elif(score>=70 and score<80):
        return("C")
    elif(score>=80 and score<90):
        return("B")
    else:
        return("A")
    
def is_passing(letter=None):
    if letter in["C","B","A"]:
        return(True)
    else:
        return(False)

score= int(input("please enter your score: "))
Letter=percentage_to_letter(score)
#check if correct return
print(Letter)
passing= is_passing(Letter)
#check if correct return
print(passing)