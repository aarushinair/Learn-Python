#Write a program that accepts a string from user and returns it after re-moving vowels from it.
# Python program to remove vowels from a string 
# Function to remove vowels 
def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
              
    # Print string without vowels 
    print(string) 
  
# Driver program 
string = "Learn Code with Aarushi - The fastest method to master Python"
rem_vowel(string)
