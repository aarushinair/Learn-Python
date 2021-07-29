#Write a program to remove odd numbers from the list and return a list with even numbers
list = [11, 22, 33, 44, 55]

# print original list
print "Original list:"
print list

# loop to traverse each element in the list
# and, remove elements
# which are ODD (not divisible by 2)
for i  in list:
	if(i%2 != 0):
	    list.remove(i)

# print list after removing ODD elements
print "list after removing ODD numbers:"
print list
