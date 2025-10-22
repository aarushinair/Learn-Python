#Write a Python3 program for removing i-th indexed character from a string.

def remove(string, i): 

	# Characters before the i-th indexed 
	# is stored in a variable a 
	a = string[ : i] 
	
	# Characters after the nth indexed 
	# is stored in a variable b 
	b = string[i + 1: ] 
	
	# Returning string after removing 
	# nth indexed character. 
	return a + b 
# Driver Code 
if _name_ == '_main_': 
	
	string = "aarushi"
	
	# Remove nth index element 
	i = 5
	
	# Print the new string 
	print(remove(string, i))

	
	
	
	
	
	
	
	









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
