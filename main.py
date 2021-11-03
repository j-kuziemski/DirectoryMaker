import os
import sys

print (sys.argv[1])

#Folder name taken from parameter
directory = (sys.argv[1])

#path
parent_dir = "C:/Users/kuziemsk/OneDrive - Nokia/PROJEKTY/NBI/"

#something
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)