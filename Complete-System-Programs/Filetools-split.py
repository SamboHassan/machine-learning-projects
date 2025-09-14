#!/usr/bin/python
"""
################################################################################
 split a file into a set of parts; join.py puts them back together;
 this is a customizable version of the standard Unix split command-line
 utility; because it is written in Python, it also works on Windows and
 can be easily modified; because it exports a function, its logic can
 also be imported and reused in other applications;
################################################################################
"""
import sys, os

kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)  # default: roughly a floppy


def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):  # caller handles errors
        os.mkdir(todir)  # make dir, read/write parts
    else:
        for fname in os.listdir(todir):  # delete any existing files
            os.remove(os.path.join(todir, fname))
    partnum = 0
    input = open(fromfile, "rb")  # binary: no decode, endline
    while True:  # eof=empty string from read
        chunk = input.read(chunksize)  # get next part <= chunksize
        if not chunk:
            break
        partnum += 1
        filename = os.path.join(todir, ("part%04d" % partnum))
        fileobj = open(filename, "wb")
        fileobj.write(chunk)
        fileobj.close()  # or simply open().write()
    input.close()
    assert partnum <= 9999  # join sort fails if 5 digits
    return partnum


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-help":
        print("Use: split.py [file-to-split target-dir [chunksize]]")
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input("File to be split? ")  # input if clicked
            todir = input("Directory to store part files? ")
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]  # args in cmdline
            if len(sys.argv) == 4:
                chunksize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print("Splitting", absfrom, "to", absto, "by", chunksize)
        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print("Error during split:")
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print("Split finished:", parts, "parts are in", absto)
        if interactive:
            input("Press Enter key")  # pause if clicked


# C:\temp> cd C:\temp
# C:\temp> dir python-3.1.msi
# ...more...
# 06/27/2009  04:53 PM        13,814,272 python-3.1.msi
#             1 File(s)     13,814,272 bytes
#             0 Dir(s)  188,826,189,824 bytes free
# C:\temp> python C:\...\PP4E\System\Filetools\split.py -help
# Use: split.py [file-to-split target-dir [chunksize]]
# C:\temp> python C:\...\P4E\System\Filetools\split.py python-3.1.msi pysplit
# Splitting C:\temp\python-3.1.msi to C:\temp\pysplit by 1433600
# Split finished: 10 parts are in C:\temp\pysplit
# C:\temp> dir pysplit
# ...more...
# 02/21/2010  11:13 AM    <DIR>          .
# 02/21/2010  11:13 AM    <DIR>          ..
# 02/21/2010  11:13 AM         1,433,600 part0001
# 02/21/2010  11:13 AM         1,433,600 part0002
# 02/21/2010  11:13 AM         1,433,600 part0003
# 02/21/2010  11:13 AM         1,433,600 part0004
# 02/21/2010  11:13 AM         1,433,600 part0005
# 02/21/2010  11:13 AM         1,433,600 part0006
# 02/21/2010  11:13 AM         1,433,600 part0007
# 02/21/2010  11:13 AM         1,433,600 part0008
# 02/21/2010  11:13 AM         1,433,600 part0009
# 02/21/2010  11:13 AM           911,872 part0010
#             10 File(s)     13,814,272 bytes
#             2 Dir(s)  188,812,328,960 bytes free
