print(' * argument')

def gaurav(*a):
	for i in a:
		print(i)
gaurav('hello','world','gaurav','python')

print()



# key word argument
def gaurav(**a):
	
	for i,value in a.items():
		
		print(i,'=',value)
		
gaurav(a = 'apple', b = 'ball', c = 'crow',d = 'donkey')

print()

# yeild function

# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun(): # company create this
	yield 1
	yield 2
	yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

def gaurav():  # gaurav create this
	yield 'gaurav'
	yield 12
	yield 90
for i  in gaurav():
	# if i ==12:
		print(i)
		# break



def gaurav():
	a=input('enter thi 1st num')
	b=input('enter thi 2st num')

	if a<b:
		print(f'the num of b is greater : {b}')

	else:
		print(f'the num of a is greater : {a}')
gaurav()











