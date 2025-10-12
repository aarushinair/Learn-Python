#Write a Python program to find the longest common sub-string from two given strings
def lcs(i, j, count) :  
      
    if (i == 0 or j == 0) :  
        return count    
    if (X[i - 1] == Y[j - 1]) : 
        count = lcs(i - 1, j - 1, count + 1)  
      
    count = max(count, max(lcs( i, j - 1, 0),  
                           lcs( i - 1, j, 0)))  
    return count 
  
# Driver code  
if _name_ == "_main_" : 
  
    X = "abcdxyz"
    Y = "xyzabcd"
  
    n = len(X) 
    m = len(Y) 
    print(lcs(n, m, 0))

    







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
