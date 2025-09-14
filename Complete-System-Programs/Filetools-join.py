#!/usr/bin/python
"""
################################################################################
join all part files in a dir created by split.py, to re-create file.
This is roughly like a 'cat fromdir/* > tofile' command on unix, but is
more portable and configurable, and exports the join operation as a
reusable function.  Relies on sort order of filenames: must be same
length.  Could extend split/join to pop up Tkinter file selectors.
################################################################################
"""
import os, sys

readsize = 1024


def join(fromdir, tofile):
    output = open(tofile, "wb")
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, "rb")
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-help":
        print("Use: join.py [from-dir-name to-file-name]")
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input("Directory containing part files? ")
            tofile = input("Name of file to be recreated? ")
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print("Joining", absfrom, "to make", absto)
        try:
            join(fromdir, tofile)
        except:
            print("Error joining files:")
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print("Join complete: see", absto)
        if interactive:
            input("Press Enter key")  # pause if clicked


# C:\temp> python C:\...\PP4E\System\Filetools\join.py -help
# Use: join.py [from-dir-name to-file-name]

# C:\temp> python C:\...\PP4E\System\Filetools\join.py pysplit mypy31.msi
# Joining C:\temp\pysplit to make C:\temp\mypy31.msi
# Join complete: see C:\temp\mypy31.msi
# C:\temp> dir *.msi
# ...more...
# 02/21/2010  11:21 AM        13,814,272 mypy31.msi
# 06/27/2009  04:53 PM        13,814,272 python-3.1.msi
#             2 File(s)     27,628,544 bytes
#             0 Dir(s)  188,798,611,456 bytes free
# C:\temp> fc /b mypy31.msi python-3.1.msi
# Comparing files mypy31.msi and PYTHON-3.1.MSI
# FC: no differences encountered


# #----------------------------------------------------
# C:\temp> set PYTHONPATH=C:\...\dev\Examples
# C:\temp> python
# >>> from PP4E.System.Filetools.split import split
# >>> from PP4E.System.Filetools.join  import join
# >>>
# >>> numparts = split('python-3.1.msi', 'calldir')
# >>> numparts
# 10
# >>> join('calldir', 'callpy31.msi')
# >>>
# >>> import os
# >>> os.system('fc /B python-3.1.msi callpy31.msi')
# Comparing files python-3.1.msi and CALLPY31.msi
# FC: no differences encountered
# 0
