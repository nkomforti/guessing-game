"""A number-guessing game."""
#import random module
import random

# greeting player
print "Hello, welcome to the guessing game."
# ask player for name and save to variable
player_name = raw_input("What is your name? ")
# welcome player to game
print "Welcome, %s" % (player_name)

best_score = None

while True:
    #generate random number (integer) using random module (between 1 and 100)
    random_num = random.randint(1, 100)
    #set number of guesses to 0 each time outer loop is run
    number_of_guesses = 0
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
                number_of_guesses += 1
            elif guess > random_num:
                print "Too high"
                number_of_guesses += 1
            elif guess < random_num:
                print "Too low"
                number_of_guesses += 1
            else:
                number_of_guesses += 1
                print "Congratulations! That's correct! You guessed the right number in %d tries." % (number_of_guesses)
                #first time played through, best score is None, so needs to be set to number of guesses
                if best_score is None:
                    best_score = number_of_guesses
                elif number_of_guesses < best_score:
                    best_score = number_of_guesses
                    print "New high score! %d tries" % (best_score)
                break

    play_again = (raw_input("Would you like to play again? Y/N? ")).upper()
    # play_again = play_again.upper()
    if play_again == "Y":
        continue
    else:
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

