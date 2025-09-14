"""
delete all .pyc bytecode files in a directory tree: use the
command line arg as root if given, else current working dir
"""

# Example 6-14 codes a portable and general command line tool, with support for
# arguments, exception processing, tracing, and list-only mode.

import os, sys

findonly = False
rootdir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]
found = removed = 0
for thisDirLevel, subsHere, filesHere in os.walk(rootdir):
    for filename in filesHere:
        if filename.endswith(".pyc"):
            fullname = os.path.join(thisDirLevel, filename)
            print("=>", fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    type, inst = sys.exc_info()[:2]
                    print("*" * 4, "Failed:", filename, type, inst)
            found += 1

print("Found", found, "files, removed", removed)

# C:\...\Examples\PP4E> Tools\cleanpyc.py
# => C:\Users\mark\Stuff\Books\4E\PP4E\dev\Examples\PP4E\__init__.pyc
# => C:\Users\mark\Stuff\Books\4E\PP4E\dev\Examples\PP4E\Preview\initdata.pyc

# ...more lines here...
# Found 24 files, removed 24
# C:\...\PP4E\Tools> cleanpyc.py .
# => .\find.pyc
# => .\visitor.pyc
# => .\__init__.pyc
# Found 3 files, removed 3
