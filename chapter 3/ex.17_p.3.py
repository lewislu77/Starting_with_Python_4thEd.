# diagnostyka wi-fi
# lewis_lu 28/06/2019


print('Ten program przeprowadzi cie krok po kroku w rozwiazaniu problemu polaczenia Wi-Fi')
print('Ponowniem uruchom komputer i sprobuj nawiazac polaczenie.')


user_ans = input('Czy to rozwiazalo problem? (T gdy Tak lub N gdy Nie): ')


if user_ans.upper() == 'N':
    print('Ponowniem uruchom komputer i sprobuj nawiazac polaczenie.')
    user_ans = input('Czy to rozwiazalo problem? (T gdy Tak lub N gdy Nie): ')
    if user_ans.upper() == 'N':
        print('Upewnij sie o prawidlowym polaczeniu przewodem routera i modemu.')
        user_ans = input('Czy to rozwiazalo problem? (T gdy Tak lub N gdy Nie): ')
        if user_ans.upper() == 'N':
            print('Przenies router w inne miejsce i sprobuj nawiazac polaczenie.')
            user_ans = input('Czy to rozwiazalo problem? (T gdy Tak lub N gdy Nie): ')
            if user_ans.upper() == 'N':
                print('Kup nowy router.')
				
				
if user_ans.upper() == 'T':
    print('Ciesze sie ze udalo sie nawiazac polaczenie Wi-Fi z routerem.')