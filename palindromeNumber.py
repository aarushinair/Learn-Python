import math

# the recursive function to reverse
def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))


number = 9669669
# printing the original number
print ("The original number is : " + str(number))
# printing the reversed number
print ("Reversed number: " + str(rev(number)))

# for checking a number is palindrome
res = number == rev(number)
# printing result
print ("Is the number palindrome : " + str(res))
