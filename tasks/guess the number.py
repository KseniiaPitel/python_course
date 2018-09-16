import random

number = random.randint (0,11)

while True:
    answer = input("Enter your number: ")
    if not answer or answer == "exit":
        break
    if not answer.isdigit():
        print("Enter digit, not letters")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Your number greater than my")

    elif user_answer < number:
        print("Your number less than my")
    else:
        print("Exactly!")
        break


