# first practice
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left>0:
  guess = int(raw_input("Your guess is (1~10)?"))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose. The correct number is %s" % (random_number)
  
  
# second practice
import random
random_num = random.randint(1,10)
print random_num 

guess_count = 0
while guess_count<=5:
    guess = int(raw_input("what you guess?"))
    if random_num == guess:
        print "you win"
        break
    guess_count += 1
else:
    print "you lose and number =" + str(random_num)

