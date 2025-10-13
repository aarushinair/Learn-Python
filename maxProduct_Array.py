def maxArrayProduct(arr, n):
    result = arr[0]
 
    for i in range(n):
     
        mul = arr[i]
       
        for j in range(i + 1, n):
         
            result = max(result, mul)
            mul *= arr[j]

        result = max(result, mul)
     
    return result
 

# Driver code
arr = [ 5, -1, -4, 0, 2, -6, -1 ]
n = len(arr)
print("Maximum product in Sub Array is" , maxArrayProduct(arr, n))








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
