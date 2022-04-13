import random 
print("Guess the right number and win the game!")
number= random.randint(1,9)
print("Guess a number between 1 and 9: ")
chances=0

while chances<5:
    guess=int(input("Enter your guess: "))

    if guess == number:
        print ("You have won the game! Great job!")
        break 
    elif guess<number:
        print("Your guess was too low: Try guessing a number higher ", guess) 
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    
    chances +=1

    if not chances <5:
        print("You LOSE!! The number is",number)
