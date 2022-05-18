import shopping.shopping_cart as ssc
import utility as utl

# region 'Description'
"""
Any python file is considered a module and every time we import a module in another python file,
a __pycache__ folder is created in the directory of the module.

When we create a folder in the directory and we create a file in that folder, that is considered
a package (a folder with modules inside it).
! One rule for all the packages is that they need to have a file with the name:
! __init__.py
! this is for the interpreter to know that this is a package.


? import a module
* import MODULENAME
? import a module from a package
* import FOLDERNAME.MODULENAME as FM
? import a module from nested packages
* from FOLDER1.FOLDER2 import MODULENAME

? import all the methods from a module
* from MODULENAME import *
? import specific methods from a module
* from MODULENAME import MTD01, MTD02, MTD03...
? import specific methods from a module in a package
* from FOLDERNAME.MODULENAME import MTD01, MTD02, MTD03...

"""
# endregion

ssc.sayHello()
utl.sayHello()
