__author__ = '15848485'

#import string
import re

def sms(input):
    
    output = ''

    output = re.sub(r'\B[aeiou]\B', '', input.lower())

    # removes repeating letters
    # re.sub(r'[^a-z
    match = re.search('(.)\\1+', output)
    if match:
        output = re.sub('(.)\\1+', '\\1', output)
    
    
    
    return output

        # re.sub(pattern, repl, string[, count])
        # re.I is shortcut for re.IGNORECASE, but prevents iteration.
        # replaces 'aeiou' with nothing ''
        # \B removes only aeiou which occurs in the middle of the word
        # input.lower() converts every letter to lowercase
        
            #\W
            #re.sub('[^A-Za-z0-9]+', '', mystring)
            #out = re.sub('[%s]' % re.escape(string.punctuation), '', s)


input1 = "Hello World!"
input2 = "This is a text."
input3 = "She sells seashells by the sea shore."
input4 = "SMS speak is annoying, don't you think?"
input5 = "I'd prefer to be out having a drink, rather than doing this assignment."

print input1
print sms(input1)
print
print input2
print sms(input2)
print
print input3
print sms(input3)
print
print input4
print sms(input4)
print
print input5
print sms(input5)

#cipherlist += re.sub(letter, alphabet[alphabet.find(letter)-13], alphabet, re.IGNORECASE)[alphabet.find(letter)]



