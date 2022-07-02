import psycopg2
import sys
import pprint
import os
import math 
def main():
   	
	conn_string = "host='10.72.16.72' dbname='russel' user='russel' password='russel'"
	print "Connecting to database\n	->%s" % (conn_string)
 	conn = psycopg2.connect(conn_string)
 	cursor = conn.cursor()
	print "Connected!\n"
	sql_string = "SELECT trip_no,dt_message,i_lat,i_long,odometer_reading from gps_data20130301 ORDER BY trip_no,dt_message"
	cursor.execute(sql_string)
	records=cursor.fetchall()
	a=0  
	w2=open("lat_long.txt",'w')      
	while True:   
		w=open("collect.csv",'w')
        	for i in range(a,len(records)):
			if i==a:
				if(i!=0):
					w2.write("\n")
                        	trip_no=int(records[a][0])
			if int(records[i][0])==trip_no:
				w.write(str(records[i][0])+","+str(records[i][1])+","+str(records[i][2])+","+str(records[i][3])+","+str(records[i][4])+"\n")
			else:
				a=i
				break
		
		w.close()


		f=open("collect.csv",'r')
		i=0;
                distance=[]
		date=[]
		lat=[]
		lon=[]
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
		cur=0
		mean_lat=0
		mean_long=0
		
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
					#print "standstill from "+strt_date+" to "+end_date
		        		time=strt_date.split(' ')
                        		strt_time=int((time[1].split(':'))[0])*60+int((time[1].split(':'))[1])
                        		time=end_date.split(' ')
					end_time=int((time[1].split(':'))[0])*60+int((time[1].split(':'))[1])
					#print "TIME  :"+str(end_time-strt_time)
					mean_lat=float(mean_lat/cur)
					mean_long=float(mean_long/cur)
					cur=0
					w2.write("latitude :"+str(mean_lat)+":longitude :"+str(mean_long)+"\n")
					mean_lat=0
					mean_long=0
					#raka_code
		if(a==len(records)-1):
			break			
	w2.close()	 
if __name__ == "__main__":
	main()
		
