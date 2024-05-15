# class Math1:

#     def __init__(self, num):
#         self.num = num

#     def is_odd_number(self):
#         if user_input % 2 != 0:
#             print(f"{self.num} is odd")

#     def is_even_number(self):
#         if user_input % 2 == 0:
#             print(f"{self.num} is even")


# user_input = int(input("Enter any number: "))


# mathObject = Math1(user_input)

# oddNumber = mathObject.is_odd_number()
# EvenNumber = mathObject.is_even_number()


class MaxNumber:
    def __init__(self, numbers):
        self.numbers = numbers

    def maxNumber1(self):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key

        a = max(array)
        return a


array = [5, 99, 3, 8]
maxNumberObj = MaxNumber(array)
greatest_num = maxNumberObj.maxNumber1()
print(greatest_num)
