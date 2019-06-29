# wybor restauracji
# lewis_lu 29/06/2019


"""
								  weget	      wegan	    glut-free
									
		Joe's Gourmet Burgers		-			-			-
		Main Street Pizza Company	+			-			+
		Corner Cafe					+			+			+	
		Mama's Fine Italian			+			-			-
		The Chef's Kitchen			+			+			+
		


"""

print()

weget_ans = input('Czy ktos spozywa dania wegetarianskie? (T gdy Tak lub N gdy Nie): ')
wegan_ans = input('Czy ktos spozywa dania weganskie? (T gdy Tak lub N gdy Nie): ')
bglut_ans = input('Czy ktos spozywa dania bezglutenowe? (T gdy Tak lub N gdy Nie): ')



if weget_ans.upper() == 'T' and wegan_ans.upper() == 'T':
	if bglut_ans.upper() == 'T':
		print("\nOto lista dostepnych restauracji: \n\tCorner Cafe \n\tThe Chef's Kitchen\n" )

if weget_ans.upper() == 'T' and wegan_ans.upper() == 'T':
		if bglut_ans.upper() == 'N':
			print("\nOto lista dostepnych restauracji: \n\tCorner Cafe \n\tThe Chef's Kitchen\n" )
			
if weget_ans.upper() == 'T' and wegan_ans.upper() == 'N':
		if bglut_ans.upper() == 'N':
			print("\nOto lista dostepnych restauracji: \n\tMain Street Pizza Company \n\tCorner Cafe \n\tMama's Fine Italian \n\tThe Chef's Kitchen\n" )
			
if weget_ans.upper() == 'T' and wegan_ans.upper() == 'N':
		if bglut_ans.upper() == 'T':
			print("\nOto lista dostepnych restauracji: \n\tMain Street Pizza Company \n\tCorner Cafe \n\tThe Chef's Kitchen\n" )
			
if weget_ans.upper() == 'N' and wegan_ans.upper() == 'N':
		if bglut_ans.upper() == 'T':
			print("\nOto lista dostepnych restauracji: \n\tMain Street Pizza Company \n\tCorner Cafe \n\tThe Chef's Kitchen\n" )

if weget_ans.upper() == 'N' and wegan_ans.upper() == 'T':
		if bglut_ans.upper() == 'T':
			print("\nOto lista dostepnych restauracji: \n\tCorner Cafe \n\tThe Chef's Kitchen\n" )

if weget_ans.upper() == 'N' and wegan_ans.upper() == 'N':
		if bglut_ans.upper() == 'N':
			print("\nOto lista dostepnych restauracji: \n\tJoe's Gourmet Burgers \n\tMain Street Pizza Company \n\tCorner Cafe \n\tMama's Fine Italian \n\tThe Chef's Kitchen\n" )
			

