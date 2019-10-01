#writing and reading files to hardrive
import os
#read the file
myfile = open('/Users/Zayyad/Dropbox/Udemy_Python/files.txt', 'r')
content = myfile.read()
print(content)
myfile.close()

#open file in write mode
myfile = open('/Users/Zayyad/Dropbox/Udemy_Python/files.txt', 'w')
myfile.write('We just want to add more data: ')
myfile.close()

#open file in append mode
myfile = open('/Users/Zayyad/Dropbox/Udemy_Python/files.txt', 'a')
myfile.write('I checked few shortcuts in VScode')
myfile.close()

#open in read mode
myfile = open('/Users/Zayyad/Dropbox/Udemy_Python/files.txt', 'r')
print(myfile.read())
myfile.close()

#using shelve
import shelve
shelfFile = shelve.open('testdata')
books = ['dictionary', 'notes', 'jotter']
shelfFile['books'] = books
shelfFile.close()

