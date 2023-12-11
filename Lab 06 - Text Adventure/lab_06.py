# Define a class called room and adding constructor function
class Room:
    def __init__(self, description, north, south, east, west):
        self.description = str(description)
        self.north = north
        self.south = south
        self.east = east
        self.west = west


# Defining the main function
def main():
    # Creating an empty array
    room_list = []
    done = False

    # Creating rooms with attributes
    room0 = Room(
        "It's dark. The only light is a candle on a desk next to a bed. To your east is a door. All other sides are "
        "walls.",
        None, None, 1, None)
    room1 = Room(
        "You have entered a long hallway with a chandelier above you. To your west you have a door to the dimly lit "
        "bedroom. \nTo your east is what looks to be the dining room. The hallway continues north. There is an exit "
        "to the south through a window.",
        4, None, 2, 0)
    room2 = Room(
        "You are in a dining room with a magnificent wooden table set for 12. You may go west to go back to the "
        "hallway or \nnorth to go into the kitchen.",
        5, None, None, 1)
    room3 = Room(
        "You are in a brightly lit bedroom with two beds. There is a window to the north and west. To the south is"
        " a wall. \nYou have a wooden door to the east.",
        None, None, 4, None)
    room4 = Room(
        "You have entered the north side of the hallway. To the south is the rest of the hallway with a beautiful "
        "chandelier. \nThere is a brightly lit bedroom to the west, a door to what seems to be the kitchen to your "
        "east and a set of double \ndoors to the north.",
        6, 1, 5, 3)
    room5 = Room(
        "You are in the kitchen and its Hot! Someone must be cooking up a feast but no one is around. A door to the "
        "south seems to \nlead you to the dining room. A door to the west leads back to the hallway.",
        None, 2, None, 4)
    room6 = Room(
        "You are on a balcony overlooking a beautiful garden. There seems to be no way down. To your South is a set of"
        "\ndouble doors back into the house.",
        None, 4, None, None)

    # Append rooms to room_list
    room_list.append(room0)
    room_list.append(room1)
    room_list.append(room2)
    room_list.append(room3)
    room_list.append(room4)
    room_list.append(room5)
    room_list.append(room6)

    # Set starting room
    current_room = room_list[0]

    # Create while loop to loop through the game until player is done
    while not done:
        # room 1 start
        if current_room == room_list[0]:
            print()
            print(room_list[0].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                if current_room.south is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 1 end

        # room 2 start
        if current_room == room_list[1]:
            print()
            print(room_list[1].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                print()
                user_choice = input("Are you sure you want to exit through the window?")
                if user_choice.lower() == "y" or user_choice.lower() == "yes":
                    print("You jumped out of the window... goodbye!")
                    done = True
                else:
                    print("You returned inside.")
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 2 end

        # room 3 start
        if current_room == room_list[2]:
            print()
            print(room_list[2].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                if current_room.south is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 3 end

        # room 4 start
        if current_room == room_list[3]:
            print()
            print(room_list[3].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                if current_room.south is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 4 end

        # room 5 start
        if current_room == room_list[4]:
            print()
            print(room_list[4].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                if current_room.south is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 5 end

        # room 6 start
        if current_room == room_list[5]:
            print()
            print(room_list[5].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                if current_room.south is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 6 end

        # room 7 start
        if current_room == room_list[6]:
            print()
            print(room_list[6].description)
            print("You may say \"go\" with a direction to change areas.")
            user_choice = input("Which way would you like to go? ")
            if user_choice.lower() == "go n" or user_choice.lower() == "go north":
                if current_room.north is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "go s" or user_choice.lower() == "go south":
                if current_room.south is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "go e" or user_choice.lower() == "go east":
                if current_room.east is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "go w" or user_choice.lower() == "go west":
                if current_room.west is None:
                    print("You cant go that way.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("I do not understand that command, please try again.")
                # room 7 end


# initiate main function and start the program
main()
