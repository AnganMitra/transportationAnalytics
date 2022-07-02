import os
import math

f=open("collect.csv",'r')
i=0;
distance=[]
while True:
	line=f.readline()
	if not line:
		break
	if i==0:
		
		prev_odo=(line.split(','))[4]
		i+=1
		continue
	_odo=(line.split(','))[4]
	d =float( _odo)-float(prev_odo)
	if d>=0:
        	distance.append(d)
	prev_odo=_odo

f.close()	
threshold=1

standstill=0
moving=0
for i in range(0,len(distance)):

	
		#print "Waited till time: " + str(linecache.getline("collect.csv", pos)[4])
		#break

	if distance[i] < threshold:
		print "At time: " +  '-> Standstill.'
		standstill+=1
	else:
		print "At time: " +  '-> Moving.'
		moving+=1
print "Standstill count: "+str(standstill)+"    Moving count: "+str(moving)

	
		
