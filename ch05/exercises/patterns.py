def star_pyramid():
    rows=int(input("Please enter the number of rows for the pyramid: "))
    for i in range(rows+1):
        srow=i*"*"
        print(srow)
def rstar_pyramid():
    rows=int(input("Please enter the number of rows for the pyramid: "))
    for i in range(rows+1):
        srow=(rows-i)*"*"
        print(srow)
star_pyramid()
rstar_pyramid()