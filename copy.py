import os
import sys
import platform
import subprocess

#A simple script to copy from a document (input) in windows

if os.path.exists(sys.argv[1]):
    f = open(sys.argv[1], "r")
    f_contents = f.read()
    f.close()
else:
    print("Write: copy.py _filename_")
    exit(1)

check_os = platform.system()

if check_os == "Windows":
    subprocess.run("clip", universal_newlines=True, input=f_contents)
    print("copied successfuly")
else:
    print("failed: OS not supported")