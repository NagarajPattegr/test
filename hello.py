# age = int(input("Enter age \n"))

# result = "child" if (age > 0 and age <=13) else "Teen" if(age > 13 and age <=20) else "adult" if(age > 20 and age <59) else "senior"

# day = False

# price = 8 if age > 0 and age<=18 else 12
# price = price - 2 if day else price

# print(price)

#02 #

# score = int(input("Enter a score \n"))
# exit()
# grade = "A" if score>=90 and score <=100 else "B" if score >=80 else "C" if score >=70 else "D" if score >=60 else "F"
# print(grade)

#password

# name  = "raghavendra"

# for i in name:
#     if(name.count(i) == 1):
#         print(name.count(i))
#         print(i)
#         break

num = 9
# fac = 1
# while num>0:
#     fac*=num
#     num-=1
# print(fac)

# if(num > 1):
#     for i in range(2,int(num/2)):
#         if((num%i) == 0):
#             print("Not Prime")
#             exit()
# print("prime")

def unique(li):
    unique  = set()
    for i in li:
        if( i in unique):
            print("Unique item ",i)
        else:
            unique.add(i)

unique(["Apple","Banana","Mango","Apple"])