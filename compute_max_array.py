#Compute the maximum for each row in the given array?
import numpy 
  
# Function to get max element 
def maxelement(arr): 
      
    # get number of rows and columns 
    no_of_rows = len(arr) 
    no_of_column = len(arr[0]) 
      
    for i in range(no_of_rows): 
          
        # Initialize max1 to 0 at beginning 
        # of finding max element of each row 
        max1 = 0
        for j in range(no_of_column): 
            if arr[i][j] > max1 : 
                max1 = arr[i][j] 
                  
        # print maximum element of each row 
        print(max1) 
  
# Driver Code 
arr = [[3, 4, 1, 8], 
       [1, 4, 9, 11], 
       [76, 34, 21, 1], 
       [2, 1, 4, 5]] 
  
# Calling the function         
maxelement(arr)




"""
👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
"""
