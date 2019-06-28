
print()

TAX = 0.07

prod1 = input ('Podaj cene 1 produktu: ')
prod2 = input ('Podaj cene 2 produktu: ')
prod3 = input ('Podaj cene 3 produktu: ')
prod4 = input ('Podaj cene 4 produktu: ')
prod5 = input ('Podaj cene 5 produktu: ')

prod1 = float(prod1)
prod2 = float(prod2)
prod3 = float(prod3)
prod4 = float(prod4)
prod5 = float(prod5)

TAX_prod1 = prod1 * TAX
TAX_prod2 = prod2 * TAX
TAX_prod3 = prod3 * TAX
TAX_prod4 = prod4 * TAX
TAX_prod5 = prod5 * TAX

shopping = prod1 + TAX_prod1 + prod2 + TAX_prod2 + prod3 + \
           TAX_prod3 + prod4 + TAX_prod4 + prod5 + TAX_prod5

print()

print ('Wartosc netto poduktu 1 -', format(prod1, '.2f'), '+ VAT', \
       format (TAX, '.0%'), 'czyli', format(TAX_prod1, '.2f'))

print ('Wartosc netto poduktu 2 -', format(prod2, '.2f'), '+ VAT', \
       format (TAX, '.0%'), 'czyli', format(TAX_prod2, '.2f'))

print ('Wartosc netto poduktu 3 -', format(prod3, '.2f'), '+ VAT', \
       format (TAX, '.0%'), 'czyli', format(TAX_prod3, '.2f'))

print ('Wartosc netto poduktu 4 -', format(prod4, '.2f'), '+ VAT', \
       format (TAX, '.0%'), 'czyli', format(TAX_prod4, '.2f'))

print ('Wartosc netto poduktu 5 -', format(prod5, '.2f'), '+ VAT', \
       format (TAX, '.0%'), 'czyli', format(TAX_prod5, '.2f'))

print()

print ('Wartosc zakupow z VAT to:', format (shopping, '.2f'))
