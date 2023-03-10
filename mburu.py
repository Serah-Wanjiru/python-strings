Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s="Akirachix"
>>> s[0]
'A'
>>> s[1]
'k'
>>> s[2]
'i'
>>> s[3]
'r'
>>> s[4]
'a'
>>> s[5]
'c'
>>> s[6]
'h'
>>> s[7]
'i'
>>> s[8]
'x'
>>> s[-1]
'x'
>>> s[-5]
'a'
>>> s[-8]
'k'
>>> s[-9]
'A'
>>> s[-10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[1:4]
'kir'
>>> s[0:3]
'Aki'
>>> s[4:8]
'achi'
>>> s[3:]
'rachix'
>>> s[-8:-6]
'ki'
>>> s[-5:-2]
'ach'
>>> s[-4:]
'chix'
>>> s[-3:-7]
''
>>> s[1:-3]
'kirac'
>>> s[-6:7]
'rach'
>>> s[-5:8]
'achi'
>>> s[3:-3]
'rac'
>>> s[-3:3]
''
>>> x=[1,2,3,4]
>>> y=["a","b","c","d"]
>>> z=[1,2,"a","b",3.33,true,false]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> z=[1,2,"a","b",3.33,"true"]
>>> type(x)
<class 'list'>
>>> a=[1,2,3,4]
>>> b=[5,6,7]
>>> c=[a+b]
>>> c
[[1, 2, 3, 4, 5, 6, 7]]
>>> d=a*3
>>> d
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> fruits=["mango","apple","banana","passion","melon"]
>>> fruits.append("pineapple")
>>> fruits
['mango', 'apple', 'banana', 'passion', 'melon', 'pineapple']
>>> fruits.extend["orange","grape"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> fruits.extend(["orange","grape"])
>>> fruits
['mango', 'apple', 'banana', 'passion', 'melon', 'pineapple', 'orange', 'grape']
>>> fruits.insert(1,"avocado")
>>> fruits
['mango', 'avocado', 'apple', 'banana', 'passion', 'melon', 'pineapple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'avocado', 'banana', 'grape', 'mango', 'melon', 'orange', 'passion', 'pineapple']
>>> fruits.reverse()
>>> fruits
['pineapple', 'passion', 'orange', 'melon', 'mango', 'grape', 'banana', 'avocado', 'apple']
>>> fruits.remove("melon")
>>> fruits
['pineapple', 'passion', 'orange', 'mango', 'grape', 'banana', 'avocado', 'apple']
>>> fruits.pop()
'apple'
>>> len(fruits)
7
>>> fruits[0]
'pineapple'
>>> fruits[3]
'mango'
>>> fruits[6]
'avocado'
>>> fruits[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> fruits[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> fruits[3:5]
['mango', 'grape']
>>> fruits[ :4]
['pineapple', 'passion', 'orange', 'mango']
>>> fruits[2: ]
['orange', 'mango', 'grape', 'banana', 'avocado']
>>> x=[1,2,3,4,5]
>>> x
[1, 2, 3, 4, 5]
>>> for n in x:print(n)
... 
1
2
3
4
5
>>> for n in x:print(n*10)
... 
10
20
30
40
50
>>> for n in x:print(n*2)
... 
2
4
6
8
10
>>> for n in x:print(n*n)
... 
1
4
9
16
25
>>> for c in fruits:print(uppercase())
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'uppercase' is not defined
>>> for c in fruits:print(c.upper())
... 
PINEAPPLE
PASSION
ORANGE
MANGO
GRAPE
BANANA
AVOCADO
>>> for fruit in fruits:print(fruit.upper())
... 
PINEAPPLE
PASSION
ORANGE
MANGO
GRAPE
BANANA
AVOCADO
