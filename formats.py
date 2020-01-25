
#formatted stings and lists outputs
harun_list = ['Haruna Umar', '5 Carolside', 'Glasgow', '0773234421']
mama_list = ['Rakiya Umaru', 'Millionaires Qtrs', 'Lafia', '0806538374']
suleiman_string = 'Suleiman Umar,Bank road,Kebbi,080333233331'
fati_string = 'Fatsuma Abubakar,CBN Qtrs,Abuja,0805623454'

print('Name             Address:            Town:           Phone_Number')
print('-----------   ------------     --------------      -------------')
#harun list
print('{:18} {:24} {:10} {:15}'.format(harun_list[0], harun_list[1], harun_list[2], harun_list[3]))
print('{:18} {:24} {:10} {:15}'.format(mama_list[0], mama_list[1], mama_list[2], mama_list[3]))
#create lists from strings and print formatted output
suleiman_list = suleiman_string.split(',')
fati_list = fati_string.split(',')
print('{:18} {:24} {:10} {:15}'.format(suleiman_list[0], suleiman_list[1], suleiman_list[2], suleiman_list[3]))
print('{:18} {:24} {:10} {:15}'.format(fati_list[0], fati_list[1], fati_list[2], fati_list[3]))