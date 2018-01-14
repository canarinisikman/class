Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
x=('hello world')
>>> x
'hello world'
>>> y=('I am in ISD class right now')
>>> y
'I am in ISD class right now'
>>> print ('x' \n 'y')
SyntaxError: unexpected character after line continuation character
>>> print('x') \n print('y')
SyntaxError: unexpected character after line continuation character
>>> print('x'):\
	     print('y')
SyntaxError: illegal target for annotation
>>> print('x')\
	    print('y')
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> num1=int(input('please enter a number' ')
	       
SyntaxError: EOL while scanning string literal
>>> num1(input('please input a number' ;)
     
SyntaxError: invalid syntax
>>> x='''
hello world
I am in ISD class right now
'''
>>> print(x)

hello world
I am in ISD class right now

>>> 
