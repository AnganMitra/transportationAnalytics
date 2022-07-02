def diff(a,b,c,d):
	return(c*60+d-a*60-b)	
	
def printing(time):
	return str(time/60)+" hrs : " + str(time%60)+" mins "

f=open("collect.csv",'r')
f.readline()
flag=0			 # 0 for standstill 1 for moving
i=0
count=0
threshold=1
tolerance = 1
a=[]
while  True:
	line=f.readline()
	if not line: 
		break
	ids=line.split(',') # distance = 18  message = 4
	if i==0:
		print "starts at " + ids[4]
		_s=ids[4].split(' ')
		time=_s[1].split(':')		
		hr=int(time[0])
		mn=int(time[1])
		i+=1
		continue
	if i==1 and float(ids[18])>threshold:
		flag=1
		i+=1
		continue
	if i==1 and float(ids[18])<threshold:
		flag=0
		i+=1
		continue	
	if float(ids[18])>threshold and flag==1:
		count+=1
		continue
		
	if float(ids[18])<threshold and flag==0:
		count+=1
		continue
		
	if float(ids[18])>threshold and flag==0 and count > tolerance:
		count = 0;
		_s=ids[4].split(' ')
		time=_s[1].split(':')		
		cur_hr=int(time[0])
		cur_mn=int(time[1])
		
		a.append(diff(hr,mn,cur_hr,cur_mn)*10+flag)
		hr=cur_hr
		mn=cur_mn
		flag=1
		line=f.readline()
		if not line: 
			break
		ids=line.split(',')		
		if float(ids[18])>threshold:
			
			flag=1
			continue
		if i==1 and float(ids[18])<threshold:
			
			flag=0
			continue
		
	if float(ids[18])<threshold and flag==1 and count > tolerance:
		count = 0
		_s=ids[4].split(' ')
		time=_s[1].split(':')		
		cur_hr=int(time[0])
		cur_mn=int(time[1])
		line=f.readline()
		if not line: 
			break
		ids=line.split(',') # distance = 18  message = 4
		
		a.append(diff(hr,mn,cur_hr,cur_mn)*10+flag)
		hr=cur_hr
		mn=cur_mn
		flag=0
		if float(ids[18])>threshold:
			
			flag=1
			continue
		if i==1 and float(ids[18])<threshold:
			flag=0
			
			continue
		
if flag==1:
		_s=ids[4].split(' ')
		time=_s[1].split(':')		
		cur_hr=int(time[0])
		cur_mn=int(time[1])
		a.append(diff(hr,mn,cur_hr,cur_mn)*10+flag)
else:
		_s=ids[4].split(' ')
		time=_s[1].split(':')		
		cur_hr=int(time[0])
		cur_mn=int(time[1])
		a.append(diff(hr,mn,cur_hr,cur_mn)*10+flag)


#print a		
prev_flag=0
i=0
s=0;
for x in a:
	if i==0:
		i+=1
		prev_flag=x%10
	flag=x%10
	if flag==prev_flag:
		s+=x/10
	if flag!=prev_flag:
		if prev_flag==0:
			print "waiting : "+printing(s)
		if prev_flag==1:
			print "moving : "+printing(s)
		s=x/10
	prev_flag=flag	
if flag==0:
	print "waiting : "+printing(s)
if flag==1:
	print "moving : "+printing(s)	
		

