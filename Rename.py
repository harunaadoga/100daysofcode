#!/usr/bin/env python3
#Searches for American style dates in filenames and renames to European
#American(MM-DD-YYYY), European(DD-MM-YYYY)
import re, os, shutil
#American regex
datePattern = re.compile(r"""^(.*?) # all text before date
((0|1)?\d)-                  # one or two digits for the month
((0|1|2|3)?\d)-                 # one or two digits for day
((19|20)\d\d)                   # four digits for the year
(.*?)$                      # all text after the date                
""", re.VERBOSE)
#Loop over the files in the current working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    #European pattern
    datePattern = re.compile(r"""^(1)     # all text before the date
    (2 (3))-                # one or two digits for the month
    (4(5))-                 # one or two digits for the day
    (6(7))                  # all text after the date
    (8)$                    # all txt after the date
    """, re.VERBOSE)
    euroFilename = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)


