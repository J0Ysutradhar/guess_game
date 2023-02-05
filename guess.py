import random
n = random.randrange(1,20)
guess = int(input("Guess Any Number Between 20  : "))
while n!= guess:
    if guess < n:
        print("Too low ")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("Hurrah !!! You guessed it right!!")