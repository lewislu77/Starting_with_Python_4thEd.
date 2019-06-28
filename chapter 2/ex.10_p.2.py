
print()

ile = input('\tPodaj oczekiwana ilosc ciasteczek: ')
ile = float(ile)

cuk = (ile * 1.5) / 48
mas = ile / 48
maka = (ile * 2.75) / 48

print()

print('\tDo przygotowania', format(ile, '.0f'), 'ciasteczek, potrzebujesz:')
print('\t', format(cuk, '.2f'), 'szklanki cukru')
print('\t', format(mas, '.2f'), 'szklanki masla')
print('\t', format(maka, '.2f'), 'szklanki maki')
