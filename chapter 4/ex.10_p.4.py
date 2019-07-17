# wzrost czesnego
# lewis_lu 17/07/2019


tax = 0.03
cost = 8000

print('\n\tTabela wzrostu czesnego w nastepnych 5 latach')
print('\t Aktualne czasne', cost, '$, roczny wzrost', format(tax, '.1%'))
print('\t\tRok\t\t  Czesne')

for n in range(5):
	cost_add = cost * tax
	cost += cost_add
	print('\t\t', n+1, '\t\t', format(cost, '.2f'), '$')
	
print()