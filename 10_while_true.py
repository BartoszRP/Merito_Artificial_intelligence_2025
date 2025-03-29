userlist = ['Kamil01', 'piesekXD', 'Paula07']

while True:
    user = input('Podaj nazwe uzytkownika:   ')
    if user in userlist:
        print('uzytkownik rozpoznany')
        passwd = input('Podaj haslo:    ')
        if passwd == '1234':
            break
        else:
            print('Haslo niepoprawne')
    elif user == 'servis':
        id = input('Tryb servisowy, podaj ID:  ')
        if id == '7':
            passwd = input('podaj haslo serwisowe:  ')
            if passwd == '77':
                break
    else:
        print('uztkownik nierozpoznany')
print('Witamy w systemie')
