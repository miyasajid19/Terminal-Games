def main():
    provider()

def provider():
    secret_code = int(input("Enter the secret code: "))

    if 1000 <= secret_code <= 9999:
        print("Secret code is sent for validation")
        validation(secret_code)
    else:
        print("Invalid input!!!\nCode should be within the range of 1000 to 9999")
        provider()

def validation(number):
    print(f"{number} is under processing")
    list_of_number = list(str(number))
    set_of_number = set(str(number))
    
    if len(list_of_number) == len(set_of_number):
        print("The secret code is valid.")
        print("Your code is set. Now it's the second player's turn.")
        guess(number)
    else:
        print("The code you entered is not valid. Please re-enter the secret code.")
        provider()

def guess(actual_number):
    print("Now player 2, guess the number.")
    crack(actual_number)

def crack(actual_number):
    guessed_code = int(input("Guess the secret code: "))

    if 1000 <= guessed_code <= 9999:
        print("Guessed code is sent for validation")
        guessing_validation(guessed_code, actual_number)
    else:
        print("Invalid input!!!\nCode should be within the range of 1000 to 9999")
        crack(actual_number)

def guessing_validation(number, actual_number):
    print(f"{number} is under processing")
    list_of_number = list(str(number))
    set_of_number = set(str(actual_number))
    
    if len(list_of_number) == len(set_of_number):
        print("Your code is valid.")
        check(number, actual_number)
    else:
        print("The code you entered is not valid. Please re-enter the secret code.")
        crack(actual_number)

def check(number, actual_number):
    bull = 0
    cow = 0
    list_of_guessed_number = list(str(number))
    list_of_actual_number = list(str(actual_number))

    if number == actual_number:
        print("Congratulations! You cracked the code.")
    else:
        for i in range(len(list_of_actual_number)):
            if list_of_guessed_number[i] == list_of_actual_number[i]:
                bull += 1
            elif list_of_guessed_number[i] in list_of_actual_number:
                cow += 1

        print(f"There are {cow} cows and {bull} bulls.")
        print("You have to re-crack the code.")
        crack(actual_number)

main()
