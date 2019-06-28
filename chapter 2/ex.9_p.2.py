
print()

temp_C = input('\t Podaj temperature w stopniach Celsjusza: ')
temp_C = float(temp_C)

temp_F = ((9/5) * temp_C) + 32

print('\t', format(temp_C, '.1f'), '* Celsjusza, to',\
      format(temp_F, '.1f'), '* Fahrenheita.\n')
