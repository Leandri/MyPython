__author__ = '15848485'
#REsms2
#import string

import re
import time
#import timeit

time1 = time.clock()

file = open('pg76.txt')

for line in file:
    output = ''

    line = line.lower()
    line = line.split()
    
    for word in line:
        punctuation = re.sub(r'([^A-Za-z0-9])','', word)      #punctuation, moenie laaste wees nie, ander manier re.sub(r'[^A-Za-z0-9])', '', input)

        vowels = re.sub(r'\B[aeiou]\B', '', punctuation) #vowels
    
        repeat = re.sub(r'([a-z])\1+', r'\1', vowels)       #  
        output += repeat + ' '

    print output



time2 = time.clock()
diff = time2 - time1
print diff
