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
		#sql="SELECT trip_no FROM gps_data2013"+str(month/10)+str(month%10)+str(date/10)+str(date%10)+" GROUP BY trip_no"
		sql="SELECT * FROM gps_data20130301 where trip_no=143066 ORDER BY dt_message"
		cursor.execute(sql)
		records=cursor.fetchall()
		#f=open("a.csv",'w')
		for row in records:
		#	f.writeline(row)
		#f.close()
			pprint.pprint(row)
			raw_input()
		#print "gps_data2013"+str(month/10)+str(month%10)+str(date/10)+str(date%10)+" : "+str(len(records))		
		if date==30:
			month+=1
			date=0
		if month==9:
			break
		date+=1
		raw_input()
if __name__=="__main__":
	main() 
