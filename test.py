import sys

# Creating a string with the path to the pymrio package on your computer
_pymrio_path = r'C:/Programming/pymrio'  

# if the pymrio path is not in "System path" - then add it
if not _pymrio_path in sys.path:
    sys.path.append(_pymrio_path)
    
# Cleaning up: deleting the string object
del _pymrio_path


# Importing all the code to a "namespace" called "mr" - now you can run all functions by writing
# mr.func1("inputstring") input string in example function
# mr.func2(2) - input int in example function
import pymrio as mr

mrio = mr.load_test()

mrio.calc_all()

mrio.save_all(r'C:\Programming\full_mrio_txt', table_format='txt')