f=open("lat_long.txt",'r')
count=0
w=open("strip.txt",'w')
while True:
	line=f.readline()
	if not line:
		break
	line=line.strip()
	if len(line)==0 :
		continue
	else:
		w.write(line+"\n")
	#count+=1
w.close()
f.close()
