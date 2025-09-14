#!/usr/bin/python
"""
################################################################################
Return all files matching a filename pattern at and below a root directory;
custom version of the now deprecated find module in the standard library:
import as "PP4E.Tools.find"; like original, but uses os.walk loop, has no
support for pruning subdirs, and is runnable as a top-level script;
find() is a generator that uses the os.walk() generator to yield just
matching filenames: use findlist() to force results list generation;
################################################################################
"""
import fnmatch, os


def find(pattern, startdir=os.curdir):
    for thisDir, subsHere, filesHere in os.walk(startdir):
        for name in subsHere + filesHere:
            if fnmatch.fnmatch(name, pattern):
                fullpath = os.path.join(thisDir, name)
                yield fullpath


def findlist(pattern, startdir=os.curdir, dosort=False):
    matches = list(find(pattern, startdir))
    if dosort:
        matches.sort()
    return matches


if __name__ == "__main__":
    import sys

    namepattern, startdir = sys.argv[1], sys.argv[2]
    for name in find(namepattern, startdir):
        print(name)


# C:\...\Tools> python find.py *.py .. | more
#  ..\LaunchBrowser.py
#  ..\Launcher.py
#  ..\__init__.py
#  ..\Preview\attachgui.py

#  C:\...\PP4E\System\Filetools> python
#  >>> from PP4E.Tools import find
#  >>> for filename in find.find('*.py', '..'):
#  ...
# if 'walk' in open(filename).read():
#  ...
# print(filename)
#  ...
#  ..\Launcher.py
#  ..\System\Filetools\bigext-tree.py
#  ..\System\Filetools\bigpy-path.py
#  ..\System\Filetools\bigpy-tree.py

#  C:\...\PP4E\Tools> python
#  >>> import os
#  >>> from find import find
#  >>> for name in find('[qx]*.py', r'C:\temp\PP3E'):
#  ...
# print(os.path.basename(name), os.path.getsize(name))
#  ...
#  querydb.py 635
#  queuetest-gui-class.py 1152
#  queuetest-gui.py 963
