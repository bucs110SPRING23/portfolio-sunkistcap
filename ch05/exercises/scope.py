def multiply(num1,num2):
    result=0
    for _ in range (num2):
        result=num1+result
    return result

def exp(num1,num2):
    result=num1
    for _ in range (num2-1):
        result=num1*result
    return result

def square(num1):
    #for _ in range():
    result=exp(num1,2)
    return result

def main():
    num1= int(input("please input a number: "))
    num2= int(input("please input another number: "))
    activity = input("would you like to multiply,exponentiate, or square these numbers\n(M,E,S): ")
    act=activity.upper()
    if act=='M':
        mul=multiply(num1,num2)
        print(mul)
    elif act == 'E':
        ex=exp(num1,num2)
        print(ex)
    elif act =='S':
        sqa=square(num1)
        print(sqa)
    else:
        print("choose only the available options please")
        main()

if __name__=='__main__':
    main()