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








👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
