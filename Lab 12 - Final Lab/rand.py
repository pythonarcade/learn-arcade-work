import random
# создаємо випадкові числа із діапазона 1-6
die1 = random.randint(1, 20)
die2 = random.randrange(1, 20)
total = die1 + die2
print("При викиданні випало", die1, "і", die2, "очки в сумі", total)
input("\n\nНатисніть Enter щоб вийти")
def input(text):
    print(text)
    return input()

