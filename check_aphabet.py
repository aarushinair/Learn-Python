#Write a Python program to check if a string contains all letters of the alphabet.
import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
#the above output = true
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)
#the above output = false














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
