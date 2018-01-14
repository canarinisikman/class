Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
number1-input('please enter the first number: ')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    number1-input('please enter the first number: ')
NameError: name 'number1' is not defined
>>> number1=input('please enter the first number: ')
please enter the first number: 3
>>> number2=input('please enter the second number; ')
please enter the second number; 5
>>> print(int(number1+number2))
35
>>> sum = float(number1) + float(number2)
>>> print('the sum of {0} and {1} is {2}'.format(number1,number2,sum))
the sum of 3 and 5 is 8.0
>>> # question 2
>>> num = 4
num*=2
num1=num+2
num1+=3
print(num1)
SyntaxError: multiple statements found while compiling a single statement
>>> #didnt work because it cant run multiple statements at once
>>> num=4
>>> num*=2
>>> num1=num+2
>>> print(num1)
10
>>> #question 3
>>> print (2/3)
0.6666666666666666
>>> print (2//3)
0
>>> #gives a different answer because when we use '//' it will only give the number before the decimal point.
>>> 
