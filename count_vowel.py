#Write a function name ”CountVowel” which accepts a string from the user and returns a dictionary which contains the count of each vowel present in the string.

str = "Hello world"

# declare count 
count = 0

# iterate and check each character
for i in str:
	# check the conditions for vowels
	if( i=='A' or i=='a' or i=='E' or i=='e'
	or i=='I' or i=='i' or i=='O' or i=='o'
	or i=='U' or i=='u'):
		count +=1;
		
# print count
print "Total vowels are: ", count
