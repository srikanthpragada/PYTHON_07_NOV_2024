import sys

# Modify module search path
sys.path.append(r'c:\classroom\python\demo\mods')
print(sys.path)  # Module Search Path

from num_funs import *
print(iseven(10))
