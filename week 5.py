Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#question 1
>>> if a+1 <= b \
   print('true')\
   
SyntaxError: invalid syntax
>>> if a+1 <= b :
	print('true')
	else:
		
SyntaxError: invalid syntax
>>> if a+1 <= b :
	print ('true')
	else
	
SyntaxError: invalid syntax
>>> a=13
>>> b=14
>>> if a+1 <= b :
	print('true')
else:
	print('false')

	
true
>>> #before it wasnt working because I was making basic synthax errors
>>> if a + 1 >= b :
	print ('true')
else:
	print('false')

	
true
>>> if a + 1 != b :
	print('true')
else:
	print('false')

	
false
>>> #1 and 2 are true statements while the 3rd one is a false statement
>>> #question 2
>>> myage = input('how old are you')
how old are you5
>>> my age=input('how old are you= ')
SyntaxError: invalid syntax
>>> myage=input('how old are you= ')
how old are you= 5
>>> myage=input('how old are you= '):
	
SyntaxError: invalid syntax
>>> if myage:
	print('hi there, you are +myage+old')
myage=input('how old are you= ')
SyntaxError: invalid syntax
>>> myage=input('how old are you= ')
how old are you= 5
>>> if myage:
	print('hi there, you are +myage+old')

	
hi there, you are +myage+old
>>> if myage:
	print('hi there, you are + myage + old')

	
hi there, you are + myage + old
>>> #couldnt figure out what was wrong with the code
>>> #question 4
>>> list = [3,11,78,112,4,18]
>>> sum(list)
226
>>> len(list)
6
>>> avg=float(sum(list))/len(list)
>>> 226/6
37.666666666666664
>>> #question 5
>>> print('x= '):
	
SyntaxError: invalid syntax
>>> print('x= ')
x= 
>>> print(input('x= '))
x= 347
347
>>> x%7
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x%7
NameError: name 'x' is not defined
>>> 
