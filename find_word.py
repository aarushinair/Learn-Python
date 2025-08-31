#Write a Python program to find smallest and largest word in a given string
def smallest_largest_words(str1):
    word = "";
    all_words = [];
    str1 = str1 + " ";
    for i in range(0, len(str1)):
        if(str1[i] != ' '):
            word = word + str1[i];  
        else:
            all_words.append(word);  
            word = "";  
          
    small = large = all_words[0];  
#Find smallest and largest word in the str1  
    for k in range(0, len(all_words)):
        if(len(small) > len(all_words[k])):
            small = all_words[k];
        if(len(large) < len(all_words[k])):
            large = all_words[k];
    return small,large;

str1 = "Write a Python program to sort an array of given integers using Quick sort Algorithm.";  
print("Original Strings:\n",str1)
small, large = smallest_largest_words(str1)  
print("Smallest word: " + small);  
print("Largest word: " + large);










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
