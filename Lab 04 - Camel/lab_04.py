import random
def main():
    print("""                 Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.    
    """)
    done = False
    way_miles = 0
    camael_tired = 0
    water_balance = 0
    water_botles = 4
    tusems_way = -20

    while not done:
      
        choise = (input("""
        A. Выпить воды с запасов.
        B. Двигаться вперед.
        C. Двигаться вперед на полной скорости.
        D. Остановиться на ночь.
        E. Проверить статус.
        Q. Выйти.
        
        Сделайте свой выбор? """))
        if choise.upper() == "Q":
            done = True
            print("Вы вышли")
        elif choise.upper() == "E":
            print("Пройдено миль:", way_miles)
            print("Бутылок в запасах:", water_botles)
            print("Туземцы на  " + str(way_miles - tusems_way) + "  миль позади тебя.")
        elif choise.upper() == "D":
            print("Верблюд отдохнул, усталость сброшена")
            camael_tired =  0
            tusems_way =+ random.randrange(7, 15)
        elif choise.upper() == "C":
            water_balance += 1
            way_miles += random.randrange(10, 21)
            camael_tired += random.randrange(1, 4)
            tusems_way += random.randrange(7, 15)
            print("Вы прошли - " + str(way_miles) + " миль")
        elif choise.upper() == "B":
            water_balance += 1
            way_miles += random.randrange(5, 13)
            camael_tired += 1
            tusems_way += random.randrange(7, 15)
            print("Вы прошли - " + str(way_miles) + " миль")
        elif choise.upper() == "A":
            if water_botles > 0:
                water_balance = 0
                water_botles -= 1
            else:
                print("Вода закончилась")
        while water_balance in range(4, 7):
            print("Вы хотите пить")
            break
        while water_balance > 6:
            print("Вы умерли от жажды")
            done = True
            break
        while camael_tired in range(5, 9):
            print("Ваш верблюд устал, необходимо остановиться на ночь для отдыха")
            break
        while camael_tired > 8:
            print("Ваш верблюд умер, вы проиграли")
            done = True
            break
        while tusems_way == way_miles:
            print("Туземцы вас поймали, вы проиграли")
            done = True
            break
        while way_miles - tusems_way < 15:
            print("Туземцы приближаются!")
            break
        while way_miles > 200:
            print("Вы прошли пустыню, и выиграли")
            done = True
            break


        
                    
            

    
    
main()