#Write a NumPy program to calculate cumulative sum of the elements along a given axis, 
#sum over rows for each of the 3 columns and sum over columns for each of the 2 rows of a given 3x3 array.
import numpy as np
x = np.array([[1,2,3], [4,5,6]])
print("Original array: ")
print(x)
print("Cumulative sum of the elements along a given axis:")
r = np.cumsum(x)
print(r)
print("\nSum over rows for each of the 3 columns:")
r = np.cumsum(x,axis=0) 
print(r)
print("\nSum over columns for each of the 2 rows:")
r = np.cumsum(x,axis=1) 
print(r)









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
