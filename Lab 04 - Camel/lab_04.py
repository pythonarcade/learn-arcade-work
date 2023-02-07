# import statements
import random


# natives move up function
def natives_move_up(): return random.randrange(0, 14)


# full speed function
def full_speed(): return random.randrange(10, 20)


# moderate speed function
def moderate_speed(): return random.randrange(5, 12)


# camel tiredness function
def camel_tiredness_function(): return random.randrange(1, 3)


# oasis chance function
def oasis_chance(): return random.randrange(1, 20)


# defining main function
def main():
    # variables
    done = False
    miles_traveled = 190
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    canteen = 3
    oasis = random.randrange(1, 20)

    # Initial statement
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    print("")

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
            print("Y: Yes")
            print("N: No")
            print("")
            user_quit_choice = input("What is your choice? ")

            # quit check
            if user_quit_choice.upper() == "Y":
                print("You have exited the game")
                done = True

        # status check
        elif user_choice.upper() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks left in canteen:", canteen)
            print("The natives are", miles_traveled - natives_traveled, "miles behind you!")
            print("")

        # stop for the night
        elif user_choice.upper() == "D":
            camel_tiredness = 0
            natives_move = natives_move_up()
            natives_traveled = natives_traveled + natives_move
            print("The camel is happy! The natives move up", natives_move, "miles.")
            print("")

        # full speed
        elif user_choice.upper() == "C":
            full_speed_user = full_speed()
            full_speed_natives = natives_move_up()
            miles_traveled = miles_traveled + full_speed_user
            natives_traveled = natives_traveled + full_speed_natives
            camel_tiredness = camel_tiredness + camel_tiredness_function()
            thirst = thirst + 1
            full_speed_oasis = oasis_chance()
            print("You have traveled", full_speed_user, "miles.")
            print("Camel tiredness:", camel_tiredness)
            print("The natives move up", full_speed_natives, "miles.")
            if oasis == full_speed_oasis:
                canteen = 3
                thirst = 0
                camel_tiredness = 0
                print("You found an oasis!")
                print("Drinks left in canteen:", canteen)
                print("Thirst:", thirst)
                print("Camel tiredness:", camel_tiredness)
                print("")
            else:
                print("")

        # moderate speed
        elif user_choice.upper() == "B":
            moderate_speed_user = moderate_speed()
            moderate_speed_natives = natives_move_up()
            miles_traveled = miles_traveled + moderate_speed_user
            natives_traveled = natives_traveled + moderate_speed_natives
            camel_tiredness = camel_tiredness + 1
            thirst = thirst + 1
            moderate_speed_oasis = oasis_chance()
            print("You have traveled", moderate_speed_user, "miles.")
            print("Camel tiredness:", camel_tiredness)
            print("The natives move up", moderate_speed_natives, "miles.")
            if oasis == moderate_speed_oasis:
                canteen = 3
                thirst = 0
                camel_tiredness = 0
                print("You found an oasis!")
                print("Drinks left in canteen:", canteen)
                print("Thirst:", thirst)
                print("Camel tiredness:", camel_tiredness)
                print("")
            else:
                print("")

        # Drink from canteen
        elif user_choice.upper() == "A":
            if canteen != 0:
                print("You take a drink from your canteen.")
                canteen = canteen - 1
                thirst = 0
                print("")
            else:
                print("You have no more water!")
                print("")

        # you are thirsty
        if 4 <= thirst < 6:
            print("You are thirsty!")
            print("")

        # you died of thirst
        elif thirst >= 6:
            print("You died of thirsty!")
            print("")
            done = True

        if not done:
            # your camel is getting tired
            if 5 <= camel_tiredness < 8:
                print("Your camel is getting tired.")
                print("")

            # your camel is dead
            elif camel_tiredness >= 8:
                print("Your camel is dead.")
                print("")
                done = True

        if not done:
            # if the natives have caught up
            if natives_traveled >= miles_traveled:
                print("The natives have caught you.")
                print("")
                done = True

            # the natives are getting close
            elif natives_traveled >= miles_traveled - 10:
                print("The natives are getting close!")
                print("")

        if not done:
            if miles_traveled >= 200:
                print("You won and got the camel across the desert! Congrats on being alive!")
                print("")
                done = True


# calling the main function
main()
