
print()

k = input('Podaj liczbe kobiet: ')
k = int(k)
m = input('Podaj liczbe mezczyzn: ')
m = int(m)

proc_k = k/(k+m)
proc_m = m/(k+m)

print()
print('Procentowy udzial kobiet', format(proc_k, '.0%'),\
      ', mezczyzn', format(proc_m, '.0%'), '\n')
