"""A number-guessing game."""
import random

# Put your code here
print "Hello, welcome to the guessing game."
player_name = raw_input("What is your name? ")
print "Welcome, %s" % (player_name)

random_num = random.randint(1, 100)
# why is guess initially set to "None" and not 0 or something else?
guess = None

while guess != random_num:
    guess = int(raw_input("Your guess? "))

    if guess != random_num:
        if guess > random_num:
            print "Too high"
        else:
            print "Too low"
    else:
        print "Congratulations, that is correct!"

        