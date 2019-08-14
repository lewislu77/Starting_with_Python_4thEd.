# podatki
# lewis_lu 03/08/2019

TAX1 = 0.025
TAX2 = 0.05

def podatek_hrab(shopping):
	return shopping * TAX1
	
def podatek_stan(shopping):
	return shopping * TAX2
	
def shop_total(x):
	return x + podatek_hrab(x) + podatek_stan(x)

def main():
	x = float(input('\n Podaj wartosc zakupow: '))
	
	podatek_hrab(x)
	podatek_stan(x)
	shop_total(x)

	print ('\n Wartosc zakupow wynosi', format(x,'.2f'), '$')
	print (' Podatek w hrabstwie to', format(TAX1, '.1%'), '- czyli', \
       format(podatek_hrab(x), '.2f'), '$')
	print (' Podatek stanowy to', format(TAX2, '.1%'), '- czyli', \
       format(podatek_stan(x), '.2f'), '$')
	print (' Calkowita wartosc zakupow z podatkiem wynosi', \
       format(shop_total(x), '.2f'), '$\n')
	   
main()
	   