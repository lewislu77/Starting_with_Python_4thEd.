
MOD = 0.23

sale = input('Podaj wartosc sprzedazy w EURO: ')
sale = float(sale)
bonus = sale * MOD

print('Przewidywany', format(MOD, '.0%'), 'zysk przy sprzedazy na poziomie', \
      format(sale, '.2f'), 'EURO wynosi:', format(bonus, '.2f'), 'EURO')
