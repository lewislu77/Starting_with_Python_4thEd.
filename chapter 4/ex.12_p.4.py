# silnia liczby nieujemnej n (n!)
# lewis_lu 17/07/2019

liczba = int(input('\n\tPodaj nieujemna liczbe: '))

silnia = 1

for n in range(2, liczba + 1):
    silnia *= n

print('\tSilnia z:', liczba, 'to', silnia, '\n')