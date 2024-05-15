# # def doNothingwithValue(value):
# #     return 897


# # a = 9
# # a = doNothingwithValue(a)
# # print(a)


# # sts1 = input("Enter first student name: ")
# # sts1_eng_marks = int(input("Enter " + sts1 + " english marks: "))
# # sts1_math_marks = int(input("Enter  " + sts1 + "math marks: "))
# # sts1_total = sts1_eng_marks + sts1_math_marks

# # sts2 = input("Enter second student name: ")
# # sts2_eng_marks = int(input("Enter "+sts2+"'s english marks: "))
# # sts2_math_marks = int(input("Enter"+sts2 + "math marks: "))
# # sts2_total = sts2_eng_marks + sts2_math_marks

# # sts3 = input("Enter third student name: ")
# # sts3_eng_marks = int(input("Enter"+sts3 + "'s english marks: "))
# # sts3_math_marks = int(input("Enter"+sts3 + "math marks: "))
# # sts3_total = sts3_eng_marks + sts3_math_marks

# # sts4 = input("Enter fourth student name: ")
# # sts4_eng_marks = int(input("Enter" + sts4 + "english marks: "))
# # sts4_math_marks = int(input("Enter" + sts4 + "math marks: "))
# # sts4_total = sts4_eng_marks + sts4_math_marks

# # sts5 = input("Enter fifth student name: ")
# # sts5_eng_marks = int(input("Enter" + sts5 + "english marks: "))
# # sts5_math_marks = int(input("Enter" + sts5 + "math marks: "))
# # sts5_total = sts5_eng_marks + sts5_math_marks


# # sts_list = [{
# #     "name": sts1,
# #     "English marks": sts1_eng_marks,
# #     "Math marks": sts1_math_marks,
# #     "Total": sts1_total
# # },
# #     {
# #     "name": sts2,
# #     "English marks": sts2_eng_marks,
# #     "Math marks": sts2_math_marks,
# #     "Total": sts2_total
# # },
# #     {
# #     "name": sts3,
# #     "English marks": sts3_eng_marks,
# #     "Math marks": sts3_math_marks,
# #     "Total": sts3_total
# # },
# #     {
# #     "name": sts4,
# #     "English marks": sts4_eng_marks,
# #     "Math marks": sts4_math_marks,
# #     "Total": sts4_total
# # },
# #     {
# #     "name": sts5,
# #     "English marks": sts5_eng_marks,
# #     "Math marks": sts5_math_marks,
# #     "Total": sts5_total
# # }]

# # print(sts_list)


# def sts_list1():

#     sts_list = []

#     for i in range(2):
#         sts = input("Enter first student name: ")
#         sts_eng_marks = int(input("Enter " + sts + " english marks: "))
#         sts_math_marks = int(input("Enter  " + sts + " math marks: "))
#         sts_total = sts_eng_marks + sts_math_marks

#         item = {"name": sts,
#                 "Eng marks": sts_eng_marks,
#                 "Math marks": sts_math_marks,
#                 "Total": sts_total
#                 }

#         # for item in sts_list:
#         #     sts_list = sts_list.append(item)

#         sts_list.append(item)

#     return sts_list


# data = sts_list1()
# print(data)


# def sts_list1():
#     sts_list = []
#     for i in range(2):
#         sts = input("Enter first student name: ")
#         sts_eng_marks = int(input("Enter " + sts + " english marks: "))
#         sts_math_marks = int(input("Enter  " + sts + " math marks: "))
#         sts_total = sts_eng_marks + sts_math_marks

#         item = {
#             "name": sts,
#             "Eng marks": sts_eng_marks,
#             "Math marks": sts_math_marks,
#             "Total": sts_total
#         }
#         sts_list.append(item)

#     return sts_list


# data = sts_list1()

# # for item in data:
# print(data)


# # Initialize an empty list to store dictionary items
# # list_of_items = []

# # # Loop through each dictionary in the list_of_dicts
# # for dictionary in list_of_dicts:
# #     # Loop through key-value pairs in the dictionary
# #     for key, value in dictionary.items():
# #         # Append the key-value pair as a tuple to the list_of_items
# #         list_of_items.append((key, value))

# # # Print the list of dictionary items
# # print("List of dictionary items:")
# # for item in list_of_items:
# #     print(item)

# # user_dict = {}

# # num_entries = int(input("Enter the number of entries you want to add: "))

# # for i in range(num_entries):
# #     key = input("name: ", "Eng marks: ", "Math marks: ", "Total: ")
# #     value = input("Enter value: ")
# #     user_dict[key] = value

# # print("Dictionary after adding user input:", user_dict)


# # P = int(input("Please enter value for P: "))
# # Q = int(input("Please enter value for Q: "))

# # # To swap the value of two variables
# # # we will user third variable which is a temporary variable
# # temp_1 = P
# # P = Q
# # Q = temp_1

# # print("The Value of P after swapping: ", P)
# # print("The Value of Q after swapping: ", Q)

# ****************************variable swap without temporary variable**************************************************
# #
# a = 9
# b = 6
# a, b = b, a
# print(a)


# ***********************************************Variable swap with temporary variable***************************************
# # P = int(input("Enter the value of P: "))
# # Q = int(input("Enter the value of Q: "))

# # temp_1 = P
# # P = Q
# # Q = temp_1


# # print("The swapped variable P gives the swapped value " + str(P))
# # print("The swapped variable q gives the swapped value " + str(Q))


# list_words = ["hello", world]

# ************************faboncci sequence***********************************************************

# first_num = 0
# sec_num = 1
# count = 0
# while count <= 10:
#     print(first_num)
#     third_num = first_num+sec_num
#     first_num = sec_num
#     sec_num = third_num
#     count = count+1


# *********************************************Area of rectangle*****************************************


# length = int(input("Enter length of rectangle to find its area: "))
# breadth = int(input("Enter breadth of rectangle to find its area: "))
# area = length * breadth
# print("The area of rectangle with length " + str(length) +
#       " and breadth " + str(breadth) + " is " + str((area)))

# ************************************************Average of number**************************************

# num1 = int(input("Enter first number: "))
# num2 = int(input("ENter second number: "))
# average = (num1+num2)/2

# print("The average of "+str(num1)+" and "+str(num2) + " is " + str(average))


# **********************Program to find maximum and minimum in list***************************************
def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


data = [46, 2, 90, 55, 34, 23, 88]

insertionSort(data)
print(data)
# ***************************************************************************


# ********************************************Program to find largest and lowest in a list****************************************************************

# list1 = [46, 2, 90, 55, 34, 23, 88]

# a = max(list1)
# b = min(list1)

# print("the max num is " + str(a)+" and the min num is "+str(b))


# ********************************Program to find pass/fail exam score**********************************************

# pass_marks = 40
# full_marks = 100
# for i in range(1):
#     eng_marks = int(input("Enter your english marks: "))
#     math_marks = int(input("Enter your math marks: "))
#     science_marks = int(input("Enter your science marks: "))
#     social_marks = int(input("Enter your social marks: "))

#     if i < pass_marks:
#         print("You fail")
#     elif i > pass_marks:
#         print("you pass")
#     elif i > 100:
#         print("Enter valid marks.")

# ******************************************Leap year program*************************************************


# ************************************ a program to determine the largest of three numbers using nested if-else statements***************

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# d = [a, b, c]

# d.sort()
# print(d[-1])


# *****************************************


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Greatest number: " + str(a))
# elif b >= c and b >= a:
#     print("Greatest number: " + str(b))
# else:
#     print("Greatest number: " + str(c))
# *************************************vowel or consonent***********************************************************************


# d = input("Enter a letter: ")
# b = ["a", "e", "i", "o", "u"]

# for i in b:
#     if d == i:
#         print("It is a vowel letter.")
#         break
#     else:
#         print("It is a consonent.")
#         break

# *******************************************Table*****************************************************

# givenNumber = int(
#     input("Enter any number to print its multiplication table: "))

# for i in range(1, 11):
#     table = str(givenNumber) + "*" + str(i) + "=" + str(givenNumber * i)
#     print(table)

# *************************************Fabonacci sequence***********************************

# first_num = 0
# sec_num = 1
# count = 0
# while count <= 10:
#     print(first_num)
#     third_num = first_num+sec_num
#     first_num = sec_num
#     sec_num = third_num
#     count = count+1

# ***************************************factorial*********************************************************


# n = int(input("Enter any number to find its factorial: "))

# if n == 0 or n == 1:
#     print(1)
# else:
#     result = 1
#     while n > 1:
#         result = result*n
#         n = n-1
#     print(result)

# *********************************Sum of even numbers**************************************************
# a = []
# total = 0
# for i in range(101):
#     if i % 2 == 0:
#         a.append(i)
# for i in a:
#     total = total + i
# print(total)

# # ***************************************************2nd largest number in list**************************


# largest = 0
# second_largest = 0
# data = [46, 2, 90, 55, 34, 88, 23]
# for i in data:
#     if i > largest:
#         second_largest = largest
#         largest = i

# print()


# ***************************************************************************


# largest = 0
# second_largest = 0

# numbers = [1, 88, 99, 3, 23, 45, 2, 23]

# for n in numbers:
#     if n > largest:
#         second_largest = largest
#         largest = n

# print("largest_number: ", largest, " second_largest_number : ", second_largest)

# # sort the above list (sort) #assignment
