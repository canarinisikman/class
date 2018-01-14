Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
radius=input('radius:')
radius:2
>>> x=3.14
>>> pi=x
>>> area=pi*radius**2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    area=pi*radius**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> area=int('pi*radius**2)
	 
SyntaxError: EOL while scanning string literal
>>> area=int('pi*radius**2')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    area=int('pi*radius**2')
ValueError: invalid literal for int() with base 10: 'pi*radius**2'
>>> area=('pi*radius**2')
>>> area
'pi*radius**2'
>>> pi=3.14
>>> area=int('pi*radius*2')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    area=int('pi*radius*2')
ValueError: invalid literal for int() with base 10: 'pi*radius*2'
>>> 
=============================== RESTART: Shell ===============================
>>> radius=int(input('radius:')
	   2
	   
SyntaxError: invalid syntax
>>> import math
>>> radius=input('radius:')
radius:2
>>> x=3.14
>>> pi=x
>>> area=pi*radius**2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    area=pi*radius**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> radius = input(float("Enter the radius:"))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    radius = input(float("Enter the radius:"))
ValueError: could not convert string to float: 'Enter the radius:'
>>> #cannot convert the string to float
>>> radius = input(float("Enter the radius:"))
>>> radius=input('enter the radius:')
enter the radius:2
>>> #now the radius is 2
>>> #question 4
>>> print(3+4+5/3)
8.666666666666666
>>> print((3+4+5)/3)
4.0
>>> #didnt calculate the avarage because there werent brackets around what was divided by 3
>>> #question 5
>>> x=19.93
>>> y=20.00
>>> z=y-x
>>> print(z)
0.07000000000000028
>>> #it prints a float, so we need to change it to an integer
>>> print(int(z))
0
>>> #question 6
>>> intx=2
>>> print(x,squares is,x*x)
SyntaxError: invalid syntax
>>> xcubed=x***3
SyntaxError: invalid syntax
>>> int(x)=2
SyntaxError: can't assign to function call
>>> #question 7
>>> from math import sqrt
>>> x=2
>>> y=4
>>> print('the product of',x,'and',y,'is',x+y)
the product of 2 and 4 is 6
>>> print('the root of their difference is',sqrt(x-y))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('the root of their difference is',sqrt(x-y))
ValueError: math domain error
>>> #question 8
>>> print('Hello /t , next year you will be /t years old')
Hello /t , next year you will be /t years old
>>> print('hello \t , next year you will be /t years old')
hello 	 , next year you will be /t years old
>>> print('hello \t , next year you will be \t years old')
hello 	 , next year you will be 	 years old
>>> #I accidentally wrote the wrong slash and thats why the first two didnt work
>>> #question 9
>>> print('radius is:2')
radius is:2
>>> print('area is;12.57')
area is;12.57
>>> #question 10
>>> p=17
>>> q=18
>>> p//10+p%10
8
>>> p%2+q%2
1
>>> (p+q)//2
17
>>> (p+q)/2.0
17.5
>>> 
