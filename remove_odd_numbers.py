#Write a program to remove odd numbers from the list and return a list with even numbers
list = [11, 22, 33, 44, 55]

# print original list
print "Original list:"
print list

# loop to traverse each element in the list
# and, remove elements
# which are ODD (not divisible by 2)
for i  in list:
	if(i%2 != 0):
	    list.remove(i)

# print list after removing ODD elements
print "list after removing ODD numbers:"
print list














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
