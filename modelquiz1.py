import math
myfile=open("running-config.cfg")
import math

def list_ifname_ip():
    mydict=dict()

    for line in myfile:
        if "nameif" in line:
            mylist = line.split()

            next(myfile)
            myline = next(myfile)
            mylist1= myline.split()

            if mylist[0]=='nameif':
                if mylist1[0] == 'ip':
                    mytuple=(mylist1[2:])
                    mydict[mylist[1]]=mytuple

    return mydict

output = list_ifname_ip()
print(output)
		



