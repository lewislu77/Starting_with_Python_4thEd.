# ruletka - kolory przedzialow
# lewis_lu 23/06/2019


point = int(input('Podaj numer przedzialu: '))


if point < 0 or point > 36:
        print('Podales nieprawidlowy przedzial')
elif point == 0:        
        print('Kolor przedzialu ZIELONY')
elif point < 11:
        if point % 2 != 0:
                print ('Kolor przedzialu CZERWONY')
        else:
                print ('Kolor przedzialu CZARNY')
elif point < 19:
        if point % 2 != 0:
                print ('Kolor przedzialu CZARNY')
        else:
                print ('Kolor przedzialu CZERWONY')
elif point < 29:
        if point % 2 != 0:
                print ('Kolor przedzialu CZERWONY')
        else:
                print ('Kolor przedzialu CZARNY')
elif point <= 36:
        if point % 2 != 0:
                print ('Kolor przedzialu CZARNY')
        else:
                print ('Kolor przedzialu CZERWONY')
        
