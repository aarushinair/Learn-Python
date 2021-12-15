#Write a Python program to count number of substrings with same first and last characters of a given string.
def no_of_substring_with_equalEnds(str1): 
	result = 0; 
	n = len(str1); 
	for i in range(n): 
		for j in range(i, n): 
			if (str1[i] == str1[j]): 
				result = result + 1
	return result 
str1 = input("Input a string: ")
print(no_of_substring_with_equalEnds(str1))





👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
