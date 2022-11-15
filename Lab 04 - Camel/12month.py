months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
k = 1
s = 0
e = 3
while k != n:
        k += 1
        s += 3
        e += 3  
        
print(months[s:e])