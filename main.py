import os
import sys
import shutil

print (sys.argv[1])
print (sys.argv[2])

#Folder name taken from parameter
directory = (sys.argv[1])
filename1 = (sys.argv[2]) + "_" + "PER" + "_" + "01"
filename2 = (sys.argv[2]) + "_" + "PER" + "_" + "02"
#path
parent_dir = "C:/Users/kuziemsk/OneDrive - Nokia/PROJEKTY/NBI/"

#path merging
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

#File creation
filename_suffix = 'txt'
filename_suffix2 = 'cfg'
file1 = os.path.join(path, filename1)
file2 = os.path.join(path, filename2)
file3 = os.path.join(path,(sys.argv[2]) + "_")
f_isis = open(file1 + "_isis" + "." + filename_suffix, "w+")
f_isis2 = open(file2 + "_isis" + "." + filename_suffix, "w+")
f_mpls = open(file1 + "_mpls" + "." + filename_suffix, "w+")
f_mpls2 = open(file2 + "_mpls" + "." + filename_suffix, "w+")
f_boot = open(file1 + "_boot" + "." + filename_suffix, "w+")
f_boot2 = open(file2 + "_boot" + "." + filename_suffix, "w+")
f_card = open(file1 + "_card" + "." + filename_suffix, "w+")
f_card2 = open(file2 + "_card" + "." + filename_suffix, "w+")
f_chassis = open(file1 + "_chassis" + "." + filename_suffix, "w+")
f_chassis2 = open(file2 + "_chassis" + "." + filename_suffix, "w+")
f_mda = open(file1 + "_mda" + "." + filename_suffix, "w+")
f_mda2 = open(file2 + "_mda" + "." + filename_suffix, "w+")
f_port = open(file1 + "_mda" + "." + filename_suffix, "w+")
f_port2 = open(file2 + "_mda" + "." + filename_suffix, "w+")
f_cfg = open(file1 + "." + filename_suffix2, "w+")
f_cfg2 = open(file2 + "." + filename_suffix2, "w+")
shutil.copy('C:/Users/kuziemsk/OneDrive - Nokia/PROJEKTY/NBI/Acceptance Test Results v0.13_IP.docx', file3  + '_Acceptance Test Results v0.13_IP.docx') # complete target filename given