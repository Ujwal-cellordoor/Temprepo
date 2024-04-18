number = input("Enter any number: ")
num = int(number)
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


# *************************************************************************************


a = 50
for num in range(a):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
