"""A number-guessing game."""
#import random module
import random

# greeting player
print "Hello, welcome to the guessing game."
# ask player for name and save to variable
player_name = raw_input("What is your name? ")
# welcome player to game
print "Welcome, %s" % (player_name)
#generate random number (integer) using random module (between 1 and 100)
random_num = random.randint(1, 100)
# why is guess initially set to "None" and not 0 or something else?
# initialize guess variable

# start loop
while True:
    # get guess from player, convert to integer
    try:
        guess = int(raw_input("Your guess? "))
    except ValueError:
        print "You did not enter a number! Please try again."
    else:
        if guess > 100 or guess < 1:
            print "Your guess is out of bounds"
        elif guess > random_num:
            print "Too high"
        elif guess < random_num:
            print "Too low"
        else:
            print "Congratulations! That's correct!"
            break



# guess = None
# # start loop, while guess is not equal to random number
# while guess != random_num:
#     # get guess from player, convert to integer
#     guess = int(raw_input("Your guess? "))

#     if guess > random_num:
#         print "Too high"
#     elif guess < random_num:
#         print "Too low"
#     else:
#         print "Congratulations! That's correct!"




# if the guess does not equal the random number
    # if guess != random_num:
        # give hint, check if guess is greater than or less than random number
        # if guess > random_num:
            # print "Too high"
        # else:
    #         print "Too low"
    #     # else the guess equals the random number, congratulate player
    # else:
    #     print "Congratulations, that is correct!"

