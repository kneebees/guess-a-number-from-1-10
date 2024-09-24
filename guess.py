import random
num = random.randint(1, 10)
guesses = 3
print("Hello. This is a game where you guess a number from 1-10. Have fun. You have 3 guesses")
play = input("Would you like to start the game? ").strip().lower()
if play == "y" or "yes":
  while guesses > 0:
    guess = int(input("\nWhat do you think the number is? "))
    if guess == num:
      print("Congratulations. You got the number right.")
      break
    elif guess != num and guess <= 10 and guess >= 1:
      guesses -= 1
      if guesses < 1:
        print("You lose. The number was {}.".format(num))
      else:
        if guess > num:
          height = "too high"
        elif guess < num:
          height = "too low"
        print("No. You're wrong. Try again. Your guess was {}.".format(height))
    else: 
      print("That's not a number from 1-10.")
elif play == "n" or "no":
  print("That's sad.")
else:
    print("You were supposed to type 'y' or 'n.'")


