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
