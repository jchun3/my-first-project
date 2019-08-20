import os
import sys

os.chdir(r'c:\Users\jchun\Desktop\3D Print\ISO Metric')
for j in range(2,8):
    b='m' + str(j)
    os.mkdir(b)
for i in range(8,22,2):
    a='m' + str(i)
    os.mkdir(a)
print('done')
