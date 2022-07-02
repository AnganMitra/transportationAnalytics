import os
import math

f=open("collect.csv",'r')
i=0;
distance=[]
date=[]
lat=[]
lon=[]
dates=""
_lat=""
_lon=""
while True:
	line=f.readline()
	if not line:
		date.append(dates)
		lat.append(_lat)
		lon.append(_lon)
		break
	if i==0:
		
		prev_odo=(line.split(','))[4]
		dates=(line.split(','))[1]
                _lat=(line.split(','))[2]
		_lon=(line.split(','))[3]
		i+=1
		continue
	_odo=(line.split(','))[4]
	d =float( _odo)-float(prev_odo)
	if d>=0:
        	distance.append(d)
	        date.append(dates)
		lat.append(_lat)
		lon.append(_lon)
        prev_odo=_odo
	dates=(line.split(','))[1]
	_lat=(line.split(','))[2]
	_lon=(line.split(','))[3]
f.close()	
threshold=1
print distance
cur=0
mean_lat=0
mean_long=0
std_lat=0
std_lon=0
#print "here"
for i in range(0,len(distance)):

	
		#print "Waited till time: " + str(linecache.getline("collect.csv", pos)[4])
		#break

	if distance[i] < threshold:
		cur+=1
		mean_lat+=float(lat[i])
		mean_long+=float(lon[i])
			
		if i==0 or distance[i-1]>=threshold:
			strt_date=date[i]
			strt_pos=i
		if i==len(distance)-1 or distance[i+1]>=threshold:
			end_date=date[i+1]
			print "standstill from "+strt_date+" to "+end_date
		        time=strt_date.split(' ')
                        strt_time=int((time[1].split(':'))[0])*60+int((time[1].split(':'))[1])
                        time=end_date.split(' ')
			end_time=int((time[1].split(':'))[0])*60+int((time[1].split(':'))[1])
			print "TIME  :"+str(end_time-strt_time)
			mean_lat=float(mean_lat/cur)
			mean_long=float(mean_long/cur)
			for j in range(strt_pos,i+1):
				std_lat+=(float((float(lat[j])-mean_lat)*(float(lat[j])-mean_lat)))
				std_lon+=(float((float(lon[j])-mean_long)*(float(lon[j])-mean_long)))

			std_lat=math.sqrt((std_lat/cur))
			std_lon=math.sqrt((std_lon/cur))
			cur=0
			mean_lat=0
			mean_long=0
			print "Latitude standard deviation :"+str(std_lat)
			print "Longitude standard deviation :"+str(std_lon)+"\n"
			std_lat=0
			std_lon=0
	
		
