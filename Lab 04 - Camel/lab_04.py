def main():
    print("""                 Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.    
    """)
    done = False
    way_miles = 0
    camael_tired = 0
    water_balbance = 0
    water_botles = 3
    tusems_way = -20

    while not done:
      
        choise = (input("""
        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.
        
        What is your choice? """))
        if choise.upper() == "Q":
            done = True
            print("you quit")
        elif choise.upper() == "E":
            print("Miles traveled:", way_miles)
            print("Drinks in canteen:", water_botles)
            print("The natives are  " + str(way_miles - tusems_way) + "  miles behind you.")
            
            

    
    
main()