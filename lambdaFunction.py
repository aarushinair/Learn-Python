# using the lambda function
lambda_cube = lambda y: y*y*y

print(lambda_cube(5))


# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
 
print(uppered_animals)








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
