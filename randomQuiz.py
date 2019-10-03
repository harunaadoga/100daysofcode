#This program is to generate random quiz files for Nigerian students about states and their capitals
import random
#store the states and capitals in a dictionary
capitals = {'Abia': 'Umuahia','Taraba':'Jalingo', 'Zamfara':'Gusau',
 'Adamawa':'Yola', 'Akwa-Ibom': 'Uyo',
'Anambra':'Awka', 'Bauchi':'Bauchi', 'Bayelsa':'Yenagoa', 'Crossriver':'Calabar',
'Enugu':'Enugu', 'Edo':'Benin City', 'Gombe':'Gombe', 'Kano':'Kano', 'Kaduna':'Kaduna',
'Katsina':'Katsina', 'Plateau':'Jos', 'Nasarawa': 'Lafia', 'Kogi':'Lokoja',
'Benue':'Makurdi', 'Ebonyi':'Abakiliki', 'Niger': 'Minna', 'Lagos':'Ikeja',
'Osun':'Osogbo','Ondo':'Akure', 'Borno':'Maiduguri', 'Yobe':'Damaturu',
'Jigawa': 'Dutse', 'Oyo':'Ibadan', 'Kwara':'Ilorin', 'Kebbi':'Birnin-Kebbi',
'Delta':'Warri', 'Imo':'Owerri', 'Rivers':'Port-Harcourt', 'Ekiti':'Ado-Ekiti',
'Ogun':'Abeokuta', 'Sokoto':'Sokoto'}


#generate 40 quiz files
for num in range(40):
    quizFile = open('/Users/quizfile%s.txt' %(num +1), 'w') #this creates 40 empty quizfiles 
    answerKeyFile = open('/Users/answerkeyfile%s.txt' %(num+1), 'w') #creates 40 answer files
    quizFile.write('\nStudent Name:\n\nDate:\n\nSubject:\n\n ')  #the header for student info
    quizFile.write(('  ' * 20) + 'Nigerian Sates and Capitals Quiz (Form%s)' %(num+1)) #tile of quiz
    quizFile.write('\n\n')

    #shuffle the order of the states in dictionary
    shuffleState = list(capitals)
    random.shuffle(shuffleState)
    #loop through all 36 states, making a question for each
    for qnumber in range(36):
        #create the right and wrong answers
        rightAnswers = capitals[shuffleState[qnumber]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(rightAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [rightAnswers]
        random.shuffle(answerOptions)
        #write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (qnumber + 1,
        shuffleState[qnumber]))
        #loop through the quizfiles to generate 4 options
        for v in range(4):
            quizFile.write('    %s. %s\n' %('ABCD'[v], answerOptions[v]))
        quizFile.write('\n')
        #write the answer key the file created earlier
        answerKeyFile.write('%s. %s\n' % (qnumber + 1, 'ABCD' [
            answerOptions.index(rightAnswers)]))
quizFile.close()  #closes the quizfile
answerKeyFile.close()  #closes the answer file


