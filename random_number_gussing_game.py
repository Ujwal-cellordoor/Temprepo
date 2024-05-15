# import random
# random_number = random.randint(1, 100)

# guessed_time = 1
# while True:
#     user_input_guessed_num = int(input("Make a prediction: "))
#     if user_input_guessed_num == random_number:
#         print("Congrats you guessed successfully with try",
#               guessed_time, random_number)
#         break
#     elif user_input_guessed_num > random_number:
#         print("Hint: Just less than your input ")
#     else:
#         print("Hint: Just above tahn your input ")

#     guessed_time = guessed_time + 1


random_number = input("random no: ")
guessed_time = 1
while True:
    user_input_guessed_num = int(input("Make a prediction: "))
    if user_input_guessed_num == random_number:
        print("Congrats you guessed successfully with try",
              guessed_time, random_number)
        break
    elif user_input_guessed_num > random_number:
        print("Hint: Just less than your input ")
    else:
        print("Hint: Just above tahn your input ")

    guessed_time = guessed_time + 1
