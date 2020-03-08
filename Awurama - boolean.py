Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = True
>>> print (not (a))
False
>>> a = True
>>> a = False
>>> b = True
>>> c = False
>>> print (b and c)
False
>>> print (b or c)
True
>>> print (not (a) and b)
True
>>> print ( (a and b) or not (c))
True
>>> print ( not (b) and not (a or c))
False
>>> print ((not ((not (b) or not (a)) and c ) or a ))
True
>>> 