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
