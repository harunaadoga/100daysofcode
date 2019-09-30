import pyperclip
import re


#paste the copied text from clipboard
text = str(pyperclip.paste())

#create regex for phone
phoneRegex = re.compile(r'\+\d{3}\s\d{10}',re.VERBOSE)
#check for a phone number match
phoneMatch = phoneRegex.findall(text)
#create regex for email
emailRegex = re.compile(r'([a-zA-Z0-9._%+=]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))', re.VERBOSE)
#check for a match.
emailMatch = emailRegex.findall(text)
#add and print
matchesFound = phoneMatch + emailMatch
if len(matchesFound) > 0:
    pyperclip.copy(str(matchesFound))
    print('Phone numbers and emails copied to clipboard: ')
    print(str(matchesFound))
else:
    print('There are no phone numbers or emails found. ')
