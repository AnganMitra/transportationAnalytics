import os
import glob

#list all the files in a directory and then read one by one
filename= glob.glob('*.csv')
i=0;
f = open (filename[i],'r');

while True:
	line=f.readline()
	if  len(line)==0:
		break;
	print line
	id = line.split(',')
	for part in id:
		print id[0],id[2],id[4],id[16],id[17],id[22],id[24],id[26],id[27]
		print '\n'
		


print "over"



