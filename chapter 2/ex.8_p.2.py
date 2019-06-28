
print()

TIP = 0.18
TAX = 0.07

dinner = input(' Podaj koszt obiadu: ')
dinner = float(dinner)

TIP_VAL = dinner * TIP
TAX_VAL = dinner * TAX

TOTAL = dinner + TIP_VAL + TAX_VAL

print()

print(' Calkowity koszt obiadu to', format(TOTAL, '.2f'), 'w tym', \
      format(TAX, '.0%'), 'podatek, czyli', format(TAX_VAL, '.2f'),\
      'oraz napiwek.')
print(' Nalezny napiwek wynosi: ', format(TIP_VAL, '.2f'), '\n')
