#Write a program to check if a given word is a palindrome word or not. Example of palindrome is âMADAMâ
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)  
string = input("Enter the string: ")
print("Method 1")
status= check_palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")

    
    
    
    
    
    
    
    
    
ð Hi, Iâm @aarushinair - Aarushi Nair (she/her/ella)
ð Iâm a Computer Science Engineering Student
ðï¸ Iâm looking to collaborate on #java, #python, #R, #applicationdevelopment
ð± #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
ð« How to reach me: https://www.linkedin.com/in/aarushinair/
ð©âð« YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
ðâ Follow me on Twitter: https://twitter.com/aarushinair_
