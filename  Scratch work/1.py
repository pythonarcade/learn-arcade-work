print("Автодилер")
price=int(input("\nВведите стоимость автомобиля без наценок: "))

nalog=price/100*10
sbor_reg=price/100*5
sbor_ag=price+1500
delivery=price+1000
everything=nalog+sbor_reg+sbor_ag+delivery
print(""" 'Итого: налог', nalog,
     '\nрегистрацьіонньій сбор' sbor_reg,
     '\nагенский сбор', sbor_ag,
     '\nдоставка', delivery
     '\nВсього:' everything """)