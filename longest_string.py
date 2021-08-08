#Write a Python program to find the longest common sub-string from two given strings
ef lcs(i, j, count) :  
      
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

    
    
    
    
    
    
👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
