import os
import sys
import shutil
import re
import fileNameChanger as NC

#location of file
os.chdir(r'C:\Users\jchun\Desktop\every-common-metric-nut-and-bolt-m2-through-m20-by-heller3d')

NC.nameCreate()

#pattern to search for. \w = letter and \d= digit
namePattern=re.compile(r'\w\d+')

#loop to find the file name
for item in os.listdir():
    name=namePattern.findall(item)
    
    #go to through every folder name and pair with whatever matches
    for j in range(73):
        file = 'M'+str(j)
        #condition to move files to match folder name
        if name[0] == file:
            newName = r'C:\Users\jchun\Desktop\3D Print\ISO Metric\m'+str(j)
            shutil.move(item,newName)

print('all done')

        
