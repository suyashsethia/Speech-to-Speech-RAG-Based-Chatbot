# reader.py
import time, os

#Set the filename and open the file
filename = 'pipe.txt'
file = open(filename, 'r', encoding = 'utf-8')

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(0.5)
        file.seek(where)
    else:
        print(line)