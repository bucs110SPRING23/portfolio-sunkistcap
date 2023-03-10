# user etners upper limit
limit=(int(input("please enter an upper limit: ")))
#range to check through all numbers up to limit
for i in range(limit+1):
    print("number: ", i)
    if (i%3==0 and i%5==0):
        print ("fizzbuzz")
    elif (i%3==0):
        print("fizz")
    elif (i%5==0):
        print("buzz")