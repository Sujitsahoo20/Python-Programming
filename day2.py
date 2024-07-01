""" 
MODULES - Basically modules are used to borrow someone else code.

which means you can use someone else code in your program with the help of modules

TYPES OF MODULES

1. Build in Modules - These module are ready to import and use and ships with
the python interpreter. there is no need to install such module explicitly.

2. External Modules (we install with the help of pip) - These modules  are imported from the third
party file or can be installed using manager like pip or conda. Since this code is written by someone
else we can install different versions of same module with the time.

"""
import pandas
import hashlib #build in module

import tensorflow # (External module) not installed that why compiler didnt print hi

print("Hi")