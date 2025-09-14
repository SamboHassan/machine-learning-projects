"""
Find the largest Python source file in a single directory.
Search Windows Python source lib, unless dir command-line arg.
"""

import os
import glob
import sys

dirname = r"C:\Users\DELL PRO\miniconda3\Lib" if len(sys.argv) == 1 else sys.argv[1]

# "C:\Users\DELL PRO\miniconda3\Lib"
# "C:\Users\DELL PRO\Desktop\ONGOING\4-learn_python_code"

allSizes = []
allPy = glob.glob(dirname + os.sep + "*.py")

for filename in allPy:
    filesize = os.path.getsize(filename)
    allSizes.append((filesize, filename))

allSizes.sort()
print(allSizes[:2])
print(allSizes[-2:])
