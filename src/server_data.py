import psycopg2
import sys
import pprint
def main():
	conn_string="host='10.72.16.72' dbname='russel'user='russel' password='russel'"
	print "Connection todatabase\n ->%s" %(conn_string)
	conn=psycopg2.connect(conn_string)
	cursor=conn.cursor()
	print "connected\n"
	date=01;
	month=03;
	while date<31:
		sql="SELECT trip_no,dt_message FROM gps_data2013"+str(month/10)+str(month%10)+str(date/10)+str(date%10)+" ORDER BY trip_no,dt_message"
		cursor.execute(sql)
		records=cursor.fetchall()
		for row in records:	
			print str(row[0])+" :  "+str(row[1])+"\n"
		#pprint.pprint(records)
		print "gps_data2013"+str(month/10)+str(month%10)+str(date/10)+str(date%10)+" : "+str(len(records))		
		if date==30:
			month+=1
			date=0
		if month==9:
			break
		date+=1

if __name__=="__main__":
	main() 
