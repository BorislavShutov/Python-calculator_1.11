

def calculate():

	first = int(raw_input('Type the first number: '))
	second = int(raw_input('Type second number: '))
	operator = raw_input('Type operator:');

	if operator == '+':
		print(first + second)

	elif operator == '-':
		print(first - second)

	elif operator == '*':
		print(first * second)

	elif operator == '/':
		print(first / second)

	else:
		print('This is bad operator')


def again():
	calculator = raw_input('Psss, Do you need some Math? Press Y or N: ')

	if calculator.upper() == 'Y':
		calculate()
	elif calculator.upper() == 'N':
		print('Okey, bye!')
	else:
		again()

again()