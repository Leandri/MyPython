__author__ = '15848485'
#REsms2
#import string

import re
import time
#import timeit

time1 = time.clock()

def sms(input):
    output = ''

    input = input.lower()
    wordlist = input.split()
    
    for word in wordlist:
        punctuation = re.sub(r'([^A-Za-z0-9])','', word)      #punctuation, moenie laaste wees nie, ander manier re.sub(r'[^A-Za-z0-9])', '', input)

        vowels = re.sub(r'\B[aeiou]\B', '', punctuation) #vowels
    
        repeat = re.sub(r'([a-z])\1+', r'\1', vowels)       #  
        output += repeat + ' '

    # output = re.sub(r'\W', '', input.lower())
    # removes repeating letters
    # re.sub(r'[^a-zA-Z\1])
##    match = re.search('(.)\\1+', output)
##    if match:
##        output = re.sub('(.)\\1+', '\\1', output)
    
    print output

input = open('pg76.txt')
sms(input)
##input1 = "Hello World!"
##input2 = "This is a text."
##
##print input1
##print sms(input1)
##print
##print input2
##print sms(input2)
##print

time2 = time.clock()
diff = time2 - time1
print diff

