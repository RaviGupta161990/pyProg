import random
name = input('Hello, what is your name:')
secretNumber = random.randint(1, 20)

print(f'Well {name}, I was thinking of a number between 1 and 20')

for guesstaken in range(1,7):
    guess = int(input("Take a guess."))

    if guess < secretNumber:
        print('your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print(f'Good job {name} ! You guessed my number {guesstaken} guesses.')
else:
    print(f'Nope, The number I was thinking of was {secretNumber} ')