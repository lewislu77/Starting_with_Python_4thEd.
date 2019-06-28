
print()

    P = input('\tKwota wplacona na konto oszczednosciowe w $: ')
    R = input('\tStopa oprocentowania w %: ')
    n = input('\tCzestotliwosc naliczania odsetek (4-gdy kwartalnie; 12-gdy rocznie): ')
    t = input('\tIlosc lat deklarowanego zdeponowania pieniedzy: ')

    P = float(P)
    R = float(R)
    n = float(n)
    t = float(t)

    r = R/100

    A = P*((1+r/n)**(n*t))

print('\n\tKwota oszczednosci po', format(t, '.0f'), 'latach, przy', format(R, '.1f'), \
      '% stopie oprocentowania')
print('\tWYNOSI: ', format(A, '.2f'), '$.')
