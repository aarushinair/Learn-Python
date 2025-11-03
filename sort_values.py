#Write a Python program to sort a dictionary by values.
def dictionairy():  
 # Declare hash function       
 key_value ={}     
  
# Initializing value  
 key_value[2] = 56       
 key_value[1] = 2 
 key_value[5] = 12 
 key_value[4] = 24
 key_value[6] = 18      
 key_value[3] = 323 
  
 print ("Task 1:-\n") 
 print ("Keys are") 
   
 # iterkeys() returns an iterator over the  
 # dictionary’s keys. 
 for i in sorted (key_value.keys()) :  
     print(i, end = " ") 
  
def main(): 
    # function calling 
    dictionairy()              
      
# Main function calling 
if _name=="main_":       
    main()






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
