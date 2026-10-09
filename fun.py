#1
# def square(number):
#      square_number = number ** 2
#      return square_number , square_number**2

# square2 = lambda number:number**2

# res = square2(10)
# print(res)

# print(square(5))


#

def n(**args):
    print(args)
def keyWord(**kwargs):
    print(kwargs)


keyWord(name="Rajesha",age=78)
n(1,2,3,4,5,6,7,8,9)