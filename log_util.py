# -*- coding: utf-8 -*-
import tailer
from os import listdir
from os.path import isfile, join, sep, expanduser

path = expanduser("~")+sep+"logutil"+sep+"testFolder"
files = [ f for f in listdir(path) if isfile(join(path,f)) ]
sorted_files = sorted(files)
last_log_file = sorted_files.pop()
file_with_path=path+sep+last_log_file

for original in tailer.tail(open(file_with_path),50):
    print original

for line in tailer.follow(open(file_with_path)):
    print line
