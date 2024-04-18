# # # a = 5
# # # b = 9
# # # print(a == b)


# # # name = "True"
# # # name_2 = "True"

# # # print(name and name_2)

# # # ****************************************

# # # a = input("Enter the number: ")

# # # b = int(a)
# # # if b < 10:
# # #     print("The number is less than 10")
# # # else:
# # #     print("The number is invalid")

# # # ******************************************

# # # a = input("Enter the number: ")

# # # b = int(a)

# # # if b < 10:
# # #     print ("It is smaller than 10")
# # # else:
# # #     print("The number is greater than 10")


# # # *****************************************

# # # a = input("Enter the number: ")

# # # b = int(a)

# # # if b == 10:
# # #     print("It is equal to 10")
# # # elif b < 10:
# # #     print("It is less than 10")
# # # else:
# # #     print("It is greater than 10")


# # a = input("Enter the number: ")

# # b = int(a)

# # if type(a) ==
# #     print("string")
# # else:
# #     print("integer")


# system = input("Enter your age: ")
# age = int(system)
# if age < 18:
#     print("You can not vote!")
# elif age >= 18:
#     print("You can vote!")


# age = int(input("Enter your age: "))

# if age <= 12:
#     print("You are in childhood!")
# elif age > 12 and age <= 20:
#     print("You are teenager!")
# elif age > 20 and age <= 50:
#     print("You are an adult!")
# elif age > 50:
#     print("You are old")


# system = input("Enter number less than 20: ")
# b = int(system)
# if b % 2 == 0 and b < 20:
#     print("The number " + str(b) + " is an even number.")
# elif b % 2 != 0 and b < 20:
#     print("The number " + str(b) + " is odd number.")
# elif b > 20:
#     print("Enter number less than 20.")

number = input("Enter any number: ")
num = int(number)
# res = True
if num == 1:
    print(num, "is not a prime number.")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
        else:
            print(num, " is a prime number.")
            break
else:
    print(num, "is not a prime number.")

# num = int(input("Enter any number: "))
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num//i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
# else:
    # print(num, "is not a prime number")
