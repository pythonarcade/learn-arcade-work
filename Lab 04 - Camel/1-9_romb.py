for row in range(10):      

    for space in range( 10 - row ):
        print(" ", end=" ")
    for column in range(1, row + 1):
        print(column, end=" ")
    for column in range( row - 1, 0, -1 ):
        print(column, end=" ")
    print()    
for row2 in range (10):
    
    for space2 in range(row2 + 2):
        print(" ", end=" ")
    for column2 in range(1, 9 - row2 ):
        print(column2, end=" ")
    for column2 in range(7 - row2, 0, -1):
        print(column2, end=" ")
    

    print()
