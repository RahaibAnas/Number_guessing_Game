import random as rd

rand_num = rd.randint(0,100)
user_input = None

print("======== Number Guessing Game =========")

while(user_input != rand_num):
    try:
        user_input = int(input("Enter any number between 1 to 100: "))
        if user_input >= 1 and user_input <= 100 :
            if user_input > rand_num:
                print("TOO! High")
            elif user_input < rand_num:
                print("TOO! Low")
            else:
                print(f"your number is {user_input}")
                print(f"computers number is {rand_num}")
                break
        else:
            print("Please! Enter the Value Between 1 to 100")
    except ValueError:
        print("❗ Invalid input! Please enter a number only.")

print("Congrants! You Guess the Right Number")
print("======= Game is End =======")
