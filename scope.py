# username = "Nagaraj"

# def fun():
#     username = "Nagz"
#     print(username)

# fun()
# print(username)

# def fun1():
#     x = 99
#     def fun2():
#         print(x)
#     return fun2

# x = fun1()
# x()

def chaicoder(num):
    def actual(x):
        return x**num
    return actual

res = chaicoder(3)
print(res(4))
