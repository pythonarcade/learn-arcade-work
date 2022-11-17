def main():
    print("""                 Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.    
    """)
    done = False
    choise = (input("What is your choice? "))
    if choise.upper == Q:
            done = True

    while done is False:
        print("""
        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.
        """)
    
main()