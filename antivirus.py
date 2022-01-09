import os,sys


var=int(sys.argv[1])

for i in range(var):
    os.rmdir(str(i+1))