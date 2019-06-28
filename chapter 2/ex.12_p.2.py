
print()

ILE_AKCJI = 2000

CENA_ZAKUPU = 40
CENA_SPRZEDAZY = 42.75

TAX = 0.03

kupno = ILE_AKCJI * CENA_ZAKUPU
tax_k = kupno * TAX
zakup = kupno + tax_k


sprzedaz = ILE_AKCJI * CENA_SPRZEDAZY
tax_s = sprzedaz * TAX
zysk = sprzedaz - tax_s

total_zysk = zysk - zakup

print('\tKoszt zakupu', ILE_AKCJI, 'akcji, po cenie', format(CENA_ZAKUPU, '.2f'),\
      '$ wynosi', format(zakup, '.2f'), '$.')
print('\tW tym', format(TAX, '.0%'), 'prowizja brokera', format(tax_k, '.2f'))

print('\n\tWartosc sprzedazy', ILE_AKCJI, 'akcji, po cenie', format(CENA_SPRZEDAZY, '.2f'),\
      '$ wynosi', format(zysk, '.2f'), '$.')
print('\tWartosc po odjeciu', format(TAX, '.0%'), 'prowizji brokera', format(tax_s, '.2f'))

print('\n\tCalkowity zysk z transakcji kupna/sprzedazy wyniosl: ', format(total_zysk, '.2f'), '$.')

