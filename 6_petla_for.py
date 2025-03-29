cars_under_insurance = ['audi', 'bmw', 'fiat', 'peugeot', 'vw', 'toyota', 'volvo']

expensive_cars = ['audi', 'bmw', 'toyota']
cheap_cars = ['fiat', 'peugeot', 'vw']

cars_to_insure = ['audi', 'ciroen', 'fiat', 'saab']
for car in cars_to_insure:
    if car in cars_under_insurance:
        print(f'Tak, mozemy ubezpieczyc twoje {car}')
        if car in cheap_cars:
            print('Masz tanie auto, to 500zł miesięcznie')
        else:
            print('Będzie drogo')
    else:
        print(f'Nie mozna ubezpiezcnyc marki {car}')

