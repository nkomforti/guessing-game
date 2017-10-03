"""A number-guessing game."""
import random

# Put your code here
print "Hello, welcome to the guessing game."
player_name = raw_input("What is your name? ")
print "Welcome, %s" % (player_name)

random_num = random.randint(1, 100)
