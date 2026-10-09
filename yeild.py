def generateEvenNumbers(limit):
 for i in range(0,limit+1,2):
    yield i

res = generateEvenNumbers(10)
li = [i for i in res]
# i = iter(res)
# print(i is res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

def factorial(number):
  if(number == 1):return 1
  return number * factorial(number - 1)

print(factorial(5))
print(li)