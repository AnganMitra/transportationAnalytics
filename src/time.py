import psycopg2
import sys


def difference(e,s):
	st=s.split(' ')
	_start=st[1].split(':')
	end=e.split(' ')
	_end=end[1].split(':')
	time1=int(_end[0])*60+int(_end[1])
	time2=int(_start[0])*60+int(_start[1])
	return (time1-time2)

def main():
	conn_string="host='10.72.16.72' dbname='russel'user='russel' password='russel'"
	print "Connection todatabase\n ->%s" %(conn_string)
	conn=psycopg2.connect(conn_string)
	cursor=conn.cursor()
	print "connected\n"
	date=01;
	month=03;
	prev_trip_no=0
	a=[]
	while date<31:
		sql="SELECT trip_no,dt_message FROM gps_data2013"+str(month/10)+str(month%10)+str(date/10)+str(date%10)+" ORDER BY trip_no,dt_message"
		cursor.execute(sql)
		#records=cursor.fetchall()
		while True: 
	             #raw_input()
		     record=cursor.fetchone()
		     if not record:
				break
		     else:
			trip_no=record[0]
			if trip_no==prev_trip_no:
				end=str(record[1])
				delta=difference(end,start)
				a.append(delta)
			        #print str(delta)+"\n"
				start=str(record[1])	
			else: 
				prev_trip_no=trip_no
				start=str(record[1])
				#print "trip_no: "+str(trip_no)+"\n"
		
		print "gps_data2013"+str(month/10)+str(month%10)+str(date/10)+str(date%10)+" : "#+str(len(record))		
		if date==30:
			month+=1
			date=0
		if month==9:
			break
		date+=1
		a.sort()
		s = set(a)
		for x in s:
			print str(x)+" "+str(a.count(x))
			#print "\n"
		
		raw_input()

if __name__=="__main__":
	main() 
