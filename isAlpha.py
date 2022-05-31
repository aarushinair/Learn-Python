def printNonAlphabats(mystr):
	print('non-alphabats:', end='')
	for i in mystr:
		if(i.isalpha() == False):
			print(i,end=',')

printNonAlphabata('PythonLearner #11')
