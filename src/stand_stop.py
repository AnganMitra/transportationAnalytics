import os
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km 
    
f=open("collect.csv",'r')
i=0;
distance = []
while True:
	line=f.readline()
	if not line:
		break
	if i==0:
		
		prev_lat=(line.split(','))[2]
		prev_long=(line.split(','))[3]
		i+=1
		continue 
	_lat=(line.split(','))[2]
	_long=(line.split(','))[3]
			
	distance.append(haversine(float(_long)* 3.14 / 180.0,float(_lat)* 3.14 / 180.0,float(prev_long)* 3.14 / 180.0,float(prev_lat)* 3.14 / 180.0))
	prev_lat=_lat
	prev_long=_long

f.close()	
threshold=1

for i in range(0,len(distance)):

	
		#print "Waited till time: " + str(linecache.getline("collect.csv", pos)[4])
		#break

	if distance[i] < threshold:
		print "At time: " +  '-> Standstill.'
		
	else:
		print "At time: " +  '-> Moving.'
		


	
		
