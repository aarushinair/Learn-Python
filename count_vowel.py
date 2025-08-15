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









"""
👋 Hi, I’m @aarushinair — Aarushi Nair (she/her)
🎓 CS Engineer | AI Researcher | Software Engineer | DEI Professional
💡 Interests: AI/ML/DL, Responsible Tech, Innovative Technologies, Ethics in AI
🌍 Advocate for Women in Tech | Community & Events Manager @AnitaB.org India
🎙️ Speaker | Content Creator | STEM Mentor
📫 Let’s connect: https://www.linkedin.com/in/aarushinair/
📹 YouTube: Code with Aarushi → https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🐦 Twitter/X: https://x.com/aarushinair_
📁 Portfolio, projects & talks: https://github.com/aarushinair
"""
