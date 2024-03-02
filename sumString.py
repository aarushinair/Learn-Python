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
👋 Hi, I’m @aarushinair - Aarushi Nair (she/her/ella)
👀 I’m a Computer Science Engineering Student
💞️ I’m looking to collaborate on #java, #python, #R, #applicationdevelopment
🌱 #GirlsWhoCode #WomenInTech #WomenInIT #WomenInSTEM #CyberSecurity #QuantumComputing #BlockChain #AI #ML
📫 How to reach me: https://www.linkedin.com/in/aarushinair/
👩‍🏫 YouTube Channel - Code with Aarushi : https://www.youtube.com/channel/UCKj5T1ELHCmkGKujkpqtl7Q
🙋‍ Follow me on Twitter: https://twitter.com/aarushinair_
"""
