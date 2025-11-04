#Calculate the sum of numbers in a string and divide it by the number of letters.
#Display the result to the nearest integer

def calc(strParam):
  letter = 0
  sum = 0.0
  for i in strParam:
    if (i.isnumeric()):
      sum = sum +int(i)
    if (i.isalpha()):
      letter += 1

  sum = sum / letter
  sum = round(sum)

  return sum


print (calc(input()))












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
