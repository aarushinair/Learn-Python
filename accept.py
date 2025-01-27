#Write a program to accept a dictionary (output from 4) and print the key with highest value. 
from collections import Counter 
  
# Initial Dictionary 
my_dict = {'A': 67, 'B': 23, 'C': 45,  
           'D': 56, 'E': 12, 'F': 69} 
  
k = Counter(my_dict) 
  
# Finding 3 highest values 
high = k.most_common(3)  
  
print("Initial Dictionary:") 
print(my_dict, "\n") 
  
  
print("Dictionary with 3 highest values:") 
print("Keys: Values") 
  
for i in high: 
 print(i[0]," :",i[1]," ")










"""
👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
"""
