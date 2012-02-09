__author__ = '15848485'

import re
import time

time1 = time.clock()                                        # Calculates current time at beginning of program.
#print time1

file = open('pg2600.txt')                                      # Opens the original text/book to read.
output = ''
dict = {}
wordpunc = ''
count1 = 0
count2 = 0

for line in file:                                           # Iterates over each line in the original file. 

    line = line.lower().split()                             # Ensures lowercase. Splits each line into a list at the spaces, (excluding spaces) so that each word can be handled individually.
    #print line                                             # Line is now a list of words.
   
    for word in line:                                       # Every word is individually looked at. 
        punctuation = re.sub(r'([^A-Za-z0-9])','', word)    # punctuation, moenie laaste wees nie, ander manier re.sub(r'[^A-Za-z0-9])', '', input)
        wordpunc += punctuation + ' '                       # STRING OF WORDS WITHOUT PUNCTUATION TO USE FOR COMPARISON
        
        vowels = re.sub(r'\B[aeiou]\B', '', punctuation)    # vowels
    
        repeat = re.sub(r'([a-z])\1+', r'\1', vowels)       # removes repeating letters

        output += repeat + ' '                              # After 3 statements, latest version of the word gets added to output. 
        dict[repeat] = punctuation                          # Dictionary created, sms word left, english right.
        count1 += 1                                         # Counts nr of words in file.

#print dict
#print
file.close()                                                

sms = open('sms.txt', 'w')
sms.write(output)                                           # All new sms words written to separate sms file.
sms.close()

search = ''     
sms = open('sms.txt')
for line in sms:
    line = line.lower()
    line = line.split()
    for word in line:                                       # Every word is looked at again in the sms file. 
        search += str(dict.get(word)) + ' '                 # When it matches the left side of dictionary, the corresponding word gets added to 'search'.
#print search
sms.close()
            
converted = open('converted.txt','w')
converted.write(search)                                     # All the converted (to original) words is written to new file.
converted.close()

convertlist2 = []
converted = open('converted.txt')
for line in converted:
    line = line.split()
    convertlist2 += line                                    # LIST OF WORDS WITHOUT PUNCTUATION TO USE IN COMPARISON.
    for word in line:
        count2 += 1                                         # Number of words in converted file are counted.
converted.close()

# counting words
print str(count1) + ' words in original book.'
print str(count2) + ' words in converted book.'
#print wordpunc

file = open('pg2600.txt')
convertlist1 = wordpunc.split()                             ###When string is split it changes into a list.
##print convertlist1

converted = open('converted.txt')
#print convertlist2

match = 0
n=0
for word in convertlist2:                                   # Checks every word in converted.txt
    if convertlist2[n] == convertlist1[n]:                  # Words in converted.txt compared with words in ALL.txt
        match += 1
    n += 1
print str(match) + ' words are exactly the same.'

# Percentage recovered
percent = 100 * float(match)/float(count1)
print str(percent) + ' percent recovered.'

file.close()
converted.close()
        
# Timing
time2 = time.clock()                                     # Calculates current time at end of program. 
#print time2
diff = time2 - time1                                     # Calculates difference, output in seconds. 
print str(diff) + ' seconds'

