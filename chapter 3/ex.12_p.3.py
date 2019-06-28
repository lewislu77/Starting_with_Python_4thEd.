# rabat
# lewis_lu 24/06/2019

PRISE = 99

val = int(input('Podaj ilosc sztuk zakupionego oprogramowania: '))


if val < 10:
	sale = PRISE * val
	print('Nie przyznano rabatu. Cena zakupu to:', format(sale, '.2f'), '$.')
	
elif val >= 10 and val < 20:
	discount = (PRISE * val) * 0.1
	sale = (PRISE * val) - discount
	print('Otrzymales 10% rabat. Cena zakupu to:', format(sale, '.2f'), '$, przy rabacie', format(discount, '.2f'), '$.')
	
elif val >= 20 and val < 50:
	discount = (PRISE * val) * 0.2
	sale = (PRISE * val) - discount
	print('Otrzymales 20% rabat. Cena zakupu to:', format(sale, '.2f'), '$, przy rabacie', format(discount, '.2f'), '$.')
	
elif val >= 50 and val < 100:
	discount = (PRISE * val) * 0.3
	sale = (PRISE * val) - discount
	print('Otrzymales 30% rabat. Cena zakupu to:', format(sale, '.2f'), '$, przy rabacie', format(discount, '.2f'), '$.')
	
elif val >= 100:
	discount = (PRISE * val) * 0.4
	sale = (PRISE * val) - discount
	print('Otrzymales 40% rabat. Cena zakupu to:', format(sale, '.2f'), '$, przy rabacie', format(discount, '.2f'), '$.')