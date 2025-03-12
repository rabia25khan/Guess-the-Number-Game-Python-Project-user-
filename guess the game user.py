import random

number = random.randint(1, 100)

print("🎯 Guess the Number (1-100)")
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("⬆️ Too low! Try again.")
        elif guess > number:
            print("⬇️ Too high! Try again.")
        else:
            print("🎉 Congratulations! You guessed it right!")
            break
    except ValueError:
        print("❌ Please enter a valid number.")
