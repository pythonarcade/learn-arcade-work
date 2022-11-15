months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
selected_month = [months[i:i+3] for i in range(0, len(months), 3)][n-1]
print('selected month is: ', selected_month)
5