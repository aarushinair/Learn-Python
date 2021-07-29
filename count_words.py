#Write a program to count number of words in a string.
def number_words(text):
  print('Total number of words in String', len(text.split()))
    
number_words('This is a test string')
s = 'This Python program counts\tnumber of words in a String.'
number_words(s)
