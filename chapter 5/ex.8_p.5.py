# koszty prac malarskich
# lewis_lu 14/08/2019

ILOSC_FARBY = 4
ROB_GODZ = 35
CZAS_PRACY = 8

koszt_pracy = CZAS_PRACY * ROB_GODZ

p = float(input('\n Powierzchnia do pomalowania (w m^2): '))
f = float(input(' Koszt 4 litrow farby: '))

print('\n * ilosc farby (w litrach):', ILOSC_FARBY)
print(' * czas malowania (w godzinach):', CZAS_PRACY)
print(' * koszt farby:', format(f, '.2f'), 'PLN')
print(' * koszt pracy:', koszt_pracy, 'PLN')
print(' * calkowity koszt:', format(koszt_pracy + f, '.2f'), 'PLN\n')

