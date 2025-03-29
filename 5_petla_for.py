lista_liczb = [2, 45, 4, 5, 1, 56]

for i in range(5):
    print(f'Element {i+1} to:')
    print(i)
    print()

for i in range(6):
    print(f'Element {i+1} to {lista_liczb[i]}')

print(f'Ile mam liczb? :  {len(lista_liczb)}')

for i in range(len(lista_liczb)):
    print(f'Element {i+1} to {lista_liczb[i]}')
    # lista_liczb[i] % 2   # zwróć resztę z dzielenia przez 2
    if lista_liczb[i] % 2 == 0:
        print(f'{lista_liczb[i]} jest parzysta')
    else:
        print(f'{lista_liczb[i]} jest NIEparzysta')
