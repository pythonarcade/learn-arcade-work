# import statements
import random


# natives move up function
def natives_move_up(): return random.randrange(0, 14)


# full speed function
def full_speed(): return random.randrange(10, 20)


# moderate speed function
def moderate_speed(): return random.randrange(5, 12)


# defining main function
def main():

    #variables
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    drink = 3

    print(natives_move_up())

    # Initial statement
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    # starting while loop
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print("")
        user_choice = input("What is your choice? ")
        print("")

        # quit statement
        if user_choice.upper() == "Q":
            print("Y: yes")
            print("N: no")
            print("")
            user_quit_choice = input("What is your choice? ")

            # quit check
            if user_quit_choice.upper() == "Y":
                print("You have excited the game")
                done = True

        # status_check
        elif user_choice == "e":
            print("Miles traveled:", miles_traveled)
            print("Drinks left in canteen:", drink)
            print("The natives are", miles_traveled - natives_traveled, "miles behind you!")
            print("")

        # stop_for_the_night
        elif user_choice == "d":
            camel_tiredness = 0
            natives_traveled = natives_traveled + natives_move_up()
            print("The camel is happy! The natives move up", natives_traveled, "miles.")
            print("")

        # full_speed
        elif user_choice == "c":
            print("You have traveled", full_speed, "miles.")
            miles_traveled = miles_traveled + full_speed
            natives_traveled = natives_traveled + natives_move_up
            thirst = thirst + 1
            camel_tiredness = random.randrange(1, 3)
            print("camel tiredness:", camel_tiredness)
            print("The natives move up", natives_move_up, "miles.")
            print("")

        # moderate_speed
        elif user_choice == "b":
            print("you have traveled %d miles" % (moderate_speed,))
            miles_traveled += full_speed
            natives_traveled += natives_move_up
            thirst += 1
            camel_tired = camel_tired + random.randrange(1, 3)
            print("camel tiredness %d" % (camel_tired,))
            print("move the natives up to %d miles" % (natives_move_up,))
            print("")

        # drink_to_canteen
        elif user_choice == "a":
            print("you drink from your canteen")
            drink = drink - 1
            thirst = 0
            print("")

        print(natives_move_up)

# calling the main function
main()
