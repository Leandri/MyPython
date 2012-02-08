__author__ = '15848485'
#import string
import re
import time
#import timeit

time1 = time.time()
#print time1

file = open('new.txt')
output = ''
dict = {}

for line in file:
#
    line = line.lower()
    line = line.split()
   
    for word in line:
        punctuation = re.sub(r'([^A-Za-z0-9])','', word)    # punctuation, moenie laaste wees nie, ander manier re.sub(r'[^A-Za-z0-9])', '', input)
        
        vowels = re.sub(r'\B[aeiou]\B', '', punctuation)    # vowels
    
        repeat = re.sub(r'([a-z])\1+', r'\1', vowels)       # removes repeating letters
        output += repeat + ' '
        dict[repeat] = punctuation
        
print dict
print
file.close()

sms = open('sms.txt', 'w')
sms.write(output)
sms.close()

search = ''
file = open('sms.txt')
for line in file:
    line = line.lower()
    line = line.split()
    for word in line:
        search += str(dict.get(word)) + ' '
print search
file.close()
            
converted = open('converted.txt','w')
converted.write(search)
converted.close()

time2 = time.time()
#print time2
diff = time2 - time1
print diff
#print time.time() - start_time, "seconds"


