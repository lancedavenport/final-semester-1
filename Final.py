# Lance Davenport wrote this code.

# I wanted to build a calculator that solves a variety of different types of problems

# I completed everything I wanted to do, though I would like to just add more methods so there are more options for solving equations.

# I got help from Reed, my friend Charlie, and Riley Gibbs. I also found some of the algorithms online.

# There are currently no bugs in my code.

from sympy.solvers import solve
from sympy import Symbol
from math import sqrt
import cmath 
import time

class problem(object):
	
	def ask():
		problem = input("What type of problem are you trying to solve? Multiplication, Addition, Division, Subtraction, Quadratic, Slope, Midpoint, Triangle. ").capitalize() 
		if problem == "Quadratic":
			equations.quadratic()
		elif problem == "Slope":
			equations.line()
		elif problem == "Midpoint":
			equations.midpoint()
		elif problem == "Triangle":
			equations.triangle()
		elif problem == "Multiplication":
			equations.multiply()
		elif problem == "Division":
			equations.division()
		elif problem == "Addition":
			equations.add()
		elif problem == "Subtraction":
			equations.sub()
		else:
			print("Im sorry, I didn't quite get that.")
			time.sleep(1)
			problem.ask()


	def ask_again():
		ask_again = input("Would you like to solve another equation? Yes/No \n").capitalize()
		if ask_again == "Yes":
			problem.ask()
		elif ask_again == "No":
			print("Thanks for using my calculator. See you later")
		else:
			print("Im sorry, I didn't get that.")
			time.sleep(1)
			problem.ask_again()



class equations(object):	
	
	def multiply():
		x = float(input("What is your first number? "))
		y = float(input("What is your second number? "))
		z = (y*x)
		print(f"The solution is: {z}")
		time.sleep(1)
		problem.ask_again()

	def division(): 
		div1 = float(input("What is your first number? "))
		div2 = float(input("What is your second number? "))
		if div2 == 0:
			print("The solution is: infinity. Crazy Right?")
			time.sleep(1)
			problem.ask_again()
		else:
			div3 = (div1/div2)
			print(f"The solution is: {div3}")
			time.sleep(1)
			problem.ask_again()

	def sub():
		sub1 = float(input("What is your first number? "))
		sub2 = float(input("What is your second number? "))
		sub3 = (sub1-sub2)
		print(f"The solution is: {sub3}")
		time.sleep(1)
		problem.ask_again()
	
	def add():
		add1 = float(input("What is your first number? "))
		add2 = float(input("What is your second number? "))
		add3 = (add1+add2)
		print(f"The solution is: {add3}")
		time.sleep(1)
		problem.ask_again()
	
	def quadratic(): 
		a = float(input('Enter a: '))
		b = float(input('Enter b: '))
		c = float(input('Enter c: '))
		if a == 0:
			t = Symbol('t')
			solution = solve( b*t + c, t )
			print(f"The solution is: {solution}")
		else: 
			d = (b**2)-(4*a*c)
			sol1 = (-b-cmath.sqrt(d))/(2*a)
			sol2 = (-b+cmath.sqrt(d))/(2*a)
			print(f"Your first number is {sol1}.")
			time.sleep(1)
			print(f"Your second number is {sol2}")
			problem.ask_again()

	def line():
		print("This is for finding the slope of a line with 2 (x, y) values.")
		time.sleep(1)
		x1 = float(input('Enter the first X value: ' ))
		x2 = float(input('Enter the second X value: '))
		y1 = float(input('Enter the first Y value: '))
		y2 = float(input('Enter the second y value: '))
		line = (float(y2-y1)/(x2-x1) )
		time.sleep(1)
		print(f"The slope of your line is: {line}.")
		problem.ask_again()

	def midpoint():
		print("This is for finding the midpoint between 2 (x,y) values.")
		p1 = float(input('Enter the first X value: ' ))
		p2 = float(input('Enter the second X value: '))
		c1 = float(input('Enter the first Y value: '))
		c2 = float(input('Enter the second y value: '))
		y_mid = (c1 + c2)/2
		x_mid = (p1 + p2)/2
		print(f"The X mid point is: {x_mid}")
		time.sleep(.5)
		print(f"The Y mid point is: {y_mid}")
		problem.ask_again()

	def triangle(): 
		print("This is using the pythagorean theorem to solve for whatever side indicated.")
		formula = input('Which side (a, b, c) do you wish to calculate? ')
		if formula == 'c':
			sidea = float(input('Input the length of side a: '))
			sideb = float(input('Input the length of side b: '))
			sidec = sqrt(sidea * sidea + sideb * sideb)
			print('The length of side c is: ' )
			print(sidec)
			time.sleep(1)
			problem.ask_again()
		elif formula == 'a':
			side_1 = float(input('Input the length of side b: '))
			side_2 = float(input('Input the length of side c: '))
			side_3 = sqrt((side_2 * side_2) - (side_1 * side_1))
			print('The length of side a is: ' )
			print(side_3)
			time.sleep(1)
			problem.ask_again()
		elif formula == 'b':
			side_a = float(input('Input the length of side a:'))
			side_c = float(input('Input the length of side c: '))
			side_b = sqrt(side_c * side_c - side_a * side_a)
			print('The length of side b is: ')
			print(side_b)
			time.sleep(1)
			problem.ask_again()
		else:
			print('Please select a side between a, b, c')

problem.ask()

