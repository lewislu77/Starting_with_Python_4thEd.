
print()

R = input('\tPodaj dlugosc rzedu w metrach: ')
E = input('\tPodaj w metrach ilosc miejsca potrzebna na stelaz: ')
S = input('\tPodaj w metrach rzadana odleglosc miedzy krzewami: ')

R = float(R)
E = float(E)
S = float(S)

V = (R - 2*E) / S

print('\n\tPrzy podanych parametrach w rzedzie zmiesci sie', format(V, '.0f'),\
      'krzewow.')
