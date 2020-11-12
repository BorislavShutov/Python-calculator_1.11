
import random

# Weather :

def wolk():

	weather = int(raw_input('''
	type 1 if weather is Sunny
	type 2 if weather is Rainy
	what weather now? : '''))

	print('Okey. Now you need set time!')

	time = int(raw_input('''
	type 1 if a Day
	type 2 if a night
	what time now? : '''))

	if (weather == 1 and time == 1 ):
		print('Ou, its good idea Bro!!!')

	elif (weather == 2 and time == 2):
		print('Dont do this, stay at home with hot drink')
		drink()

	elif (weather == 2 and time == 1):
		print('Maybe you take Umbrella? ')

	elif (weather == 1 and time == 2):
		print('Its not logic, you are stupid! ')

# Favorite drink function: 

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

# FilmsDB :

def filmList():
	films = ['The Godfather', 'Portrait of a Lady on Fire', 'Toy Story', 'Gravity', 
	'Parasite', '12 Years a Slave', '12 Angry Men', 'Pans Labyrinth']
	print('Maybe watch this film? : ' + random.choice(films))

# Calculate:

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

# CannaDoctor function : 

def cD():
	sortsM = {'1' : ['Critical Kush', 'Bubba Kush', 'Pineapple Chunk', 'Dr. Grinspoon', ],
			  '2' : ['Bad Azz Kush', 'Bubba Kush', 'Amherst Sour Diesel ', 'Satori'],
			  '3' : ['Dr. Grinspoon', 'Pineapple Chunk', 'Wild Thailand', 'Colombian Gold', 'Amherst Sour Diesel', 'Satori']}
	

# 1 = relieve stress,
# 2 = pain or depression,
# 3 = high effect.

	a = raw_input('Type 1 if cannabis need  for relieve stress\nType 2 if cannabis need  for pain or depression\nType 3 if cannabis need  for high effect')
	if a in sortsM:
		y = sortsM[a]
		print('I think this sort will suit you perfectly :   ' + random.choice(y))

	b = raw_input('Maybe you want see all sorts?\nY or N : ')

	if b == 'y':
		for x in sortsM[a]:
			print('*' + x)
			
	elif b == 'n':
		print('Good bye')
	else:
		print('Idiot')


	
# Main func :

def action():

	nameP = raw_input('name: ')
	name = nameP.capitalize()
	print('Hello ' + name)

	print('''What do you want to do?
	Type 1 if you want wolk on street
	Type 2 if you want stay at home
	Type 3 if you want Calculate
	Type 4 if you need help from cannabis''')

	yourAction = int(raw_input('Your choise: '))

	if (yourAction == 1):
		wolk()
	elif (yourAction == 2):
		drink()
	elif (yourAction == 3):
		calculate()
	elif (yourAction == 4):
		cD()


action()   # Start 


