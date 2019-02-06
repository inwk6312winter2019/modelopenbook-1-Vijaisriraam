fp=open("running-config.cfg")
readfile=fp.read()

def list_ifname_ip():
	mydict=dict()
	newdict=dict()	
	for line in readfile.split():
		word=line.strip()
		if word not in mydict:
			mydict[line]=1
		else:
			mydict[line]+=1
#	print(mydict)

	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))	
	print(mylist)
	
	for key,value in mydict.items():
		
list_ifname_ip()
		
