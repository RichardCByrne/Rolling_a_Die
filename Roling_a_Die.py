import random
import time
min = int(1)
max = int(6)



def roll_a_die(min, max):
    roll_again = "Yes"
    while roll_again == "Yes":
        print("Rolling the die... ")
        time.sleep(1)
        print("\nThe value is " + str(random.randint(min, max)) + "!")

        roll_again = input("\nRoll again?\n").capitalize()


roll_a_die(min, max)