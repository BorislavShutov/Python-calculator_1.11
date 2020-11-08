
import random

def wolk():

	pogoda = int(raw_input('''
	type 1 if weather is Sunny
	type 2 if weather is Rainy
	what weather now? : '''))

	print('Okey. Now you need set time!')

	time = int(raw_input('''
	type 1 if a Day
	type 2 if a night
	what time now? : '''))

	if (pogoda == 1 and time == 1 ):
		print('Ou, its good idea Bro!!!')

	elif (pogoda == 2 and time == 2):
		print('Dont do this, stay at home with hot drink')
		drink()

	elif (pogoda == 2 and time == 1):
		print('Maybe you take Umbrella? ')

	elif (pogoda == 1 and time == 2):
		print('Its not logic, you are stupid! ')

def drink():
	favorite = int(raw_input('''
	What your favorite hot drink?
	Type 1 if you like a Tea
	Type 2 if you like a Coffee: '''))
	if (favorite == 1):
		print('Put the kettle on tea Bro!')
	elif (favorite == 2):
		print('Put the kettle on coffee Bro!')
	filmList()


def filmList():
	films = ['The Godfather', 'Portrait of a Lady on Fire', 'Toy Story', 'Gravity', 
	'Parasite', '12 Years a Slave', '12 Angry Men', 'Pans Labyrinth']
	print('Maybe watch this film? : ' + random.choice(films))


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


	

def action():

	print('''What do you want to do?
	Type 1 if you want wolk on street
	Type 2 if you want stay at home
	Type 3 if you want Calculate''')

	yourAction = int(raw_input('Your choise: '))

	if (yourAction == 1):
		wolk()
	elif (yourAction == 2):
		drink()
	elif (yourAction == 3):
		calculate()


action()


