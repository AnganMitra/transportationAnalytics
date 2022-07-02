import os
m=int(raw_input("Enter trip id: "))
f=open("GPS_Data20130101.csv",'r')
w=open("collect.csv",'w')
w.write(f.readline())
while True:
	line=f.readline()
	if len(line)==0:
		print "Finished parsing."
		break;
	id=line.split(',')
	if int(id[6])==m:
		w.write(line)
w.close()
f.close()
