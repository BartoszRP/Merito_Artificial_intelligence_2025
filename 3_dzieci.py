children = int(input('Ile masz dzieci?   '))
salary = float(input('Ile zarabiasz?   '))
if salary > 5000:
    salary_netto = salary * 0.8
    print('Placisz pelny podatek')
elif salary >= 3000:
    salary_netto = salary * 0.9
    print('Placisz nizszy podatek')
elif salary >= 1000:
    salary_netto = salary
    print('Placisz zerowy podatek')
else:
    salary_netto = 0
    print('blad')
print(f'Na glowe: {(salary_netto + children * 800) / (children + 2)}')
