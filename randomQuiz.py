import random
import os
import pprint

#program that generates random quiz files for students
#TODO1: store the states and their capitals in a dictionary
capitals = {'Abia': 'Umuahia','Taraba':'Jalingo', 'Zamfara':'Gusau',
 'Adamawa':'Yola', 'Akwa-Ibom': 'Uyo',
'Anambra':'Awka', 'Bauchi':'Bauchi', 'Bayelsa':'Yenagoa', 'Crossriver':'Calabar',
'Enugu':'Enugu', 'Edo':'Benin', 'Gombe':'Gombe', 'Kano':'Kano', 'Kaduna':'Kaduna',
'Katsina':'Funtua', 'Plateau':'Jos', 'Nasarawa': 'Lafia', 'Kogi':'Lokoja',
'Benue':'Makurdi', 'Ebonyi':'Abakiliki', 'Niger': 'Minna', 'Lagos':'Ikeja',
'Osun':'Osogbo','Ondo':'Akure', 'Borno':'Maiduguri', 'Yobe':'Damaturu',
'Jigawa': 'Dutse', 'Oyo':'Ibadan', 'Kwara':'Ilorin', 'Kebbi':'Birnin-Kebbi',
'Delta':'Warri', 'Imo':'Imo', 'Rivers':'Port-Harcourt', 'Ekiti':'Ado-Ekiti',
'Ogun':'Ota', 'Sokoto':'Sokoto'}

#generate the quiz and answer key files
for fileNum in range(35):
    #write the quiz and key files
    quizFile = open('/Users/Zayyad/Dropbox/Udemy_Python/quizFile%s.txt' % (fileNum +1 ), 'w')
    quizAnswer = open('/Users/Zayyad/Dropbox/Udemy_Python/quizFile_answers%s' % (fileNum + 1), 'w')
    #write the header for the quiz files
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (fileNum + 1))
    quizFile.write('\n\n')

    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

#TODO: loop through all the states, making a question for each