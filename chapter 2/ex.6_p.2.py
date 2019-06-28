
print()

TAX1 = 0.025
TAX2 = 0.05

shopping = input(' Podaj wartosc zakupow: ')
shopping = float(shopping)

SHOP_TAX1 = shopping * TAX1
SHOP_TAX2 = shopping * TAX2

shop_total = shopping + SHOP_TAX1 + SHOP_TAX2


print()

print (' Wartosc zakupow wynosi', format(shopping, '.2f'), '$\n')

print (' Podatek w hrabstwie to', format(TAX1, '.1%'), '- czyli', \
       format(SHOP_TAX1, '.2f'), '$')
print (' Podatek stanowy to', format(TAX2, '.1%'), '- czyli', \
       format(SHOP_TAX2, '.2f'), '$\n')

print (' Calkowita wartosc zakupow z podatkiem wynosi', \
       format(shop_total, '.2f'), '$\n')
