def percentage_to_letter(score):
    """
    This is a function that returns a letter grade based on a percentage
    args: percent (int)
    return: letter (str)
    """
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

def is_passing(letter):
    """
    This is a function that returns a boolean based on the letter grade
    args: letter (str)
    retturn: passing (boolean)
    """
    return letter in "ABC"

def main():
    score= int(input("please enter your score: "))
    letter=percentage_to_letter(score)
    #displays letter grade
    print(f"you got a, '{letter}' as your letter grade.")
    #check if passing
    if is_passing(letter):
        print("that means you passed!")
    else:
        print("unfortunately that means you did not pass")

main()