file=open('running-config.cfg','r')

def create_access_list(fout):
    file.seek(0)
    transit_access_in=[]
    global_access=[]
    fw_management_access_in=[]
    
    for line in file:
        line=line.strip()
        if 'access-list' in line:
            if 'transit_access_in' in line:
                transit_access_in.append(line)
            elif 'global_access' in line:
                global_access.append(line)
            elif 'fw-management_access_in' in line:
                fw_management_access_in.append(line)
    print('access list for transit_access_in::\n',transit_access_in)
    print('access list for global_access::\n',global_access)
    print('access list for fw_management_access_in::\n',fw_management_access_in)
  
create_access_list(file)

