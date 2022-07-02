import psycopg2
import sys
import pprint
 
def main():
	
	conn_string = "host='10.72.16.72' dbname='russel' user='russel' password='russel'"
	print "Connecting to database\n	->%s" % (conn_string)
 	conn = psycopg2.connect(conn_string)
 	cursor = conn.cursor()
	print "Connected!\n"
	#sql_string = "SELECT trip_no,dt_message,i_lat,i_long,odometer_reading from gps_data20130301 ORDER BY trip_no,dt_message"
	sql_string = "SELECT trip_no,dt_message,i_lat,i_long,odometer_reading from gps_data20130301 where trip_no=807518 ORDER BY dt_message"
	cursor.execute(sql_string)
	records=cursor.fetchall()
	w=open("collect.csv",'w')
	i=0;
	for row in records:
		if i==0:
			trip_no=int(row[0])
			i+=1
		if int(row[0])==trip_no:
			w.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+"\n")
		else:
			break
		
	w.close()
	 
if __name__ == "__main__":
	main()
