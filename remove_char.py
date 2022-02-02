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

	
	
	
	
	
	
	
	
	
👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
