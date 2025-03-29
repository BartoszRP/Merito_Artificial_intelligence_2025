# name = input('Podaj imie:   ')
# print('Witaj')
# print(name)

# age = int(input('Ile masz lat?  '))
# print(f'Witaj {name}, wiec masz {age} lat')

# print(f'Bedziesz dorosly za {18 - age} lat')

age = int(input('Ile masz lat?  '))
if age < 18:
    print(f'mlody')
    print('przyjdz z mamą')
elif age == 18:
    print('mlody dorosly')
else:
    print('Jestes dorosly')

print('dalsza czesc programu')
print('koniec - dzieki')

# pow 5000 -> podatek 20%
# 3000-5000 -> 10%
# mniej -> brak podatku