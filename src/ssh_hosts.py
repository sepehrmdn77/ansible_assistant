import subprocess
y = subprocess.check_output('whoami',shell=True,text=True)
# print(y[:-1]) # printing current user
x = open(f'/home/{y[:-1]}/.ssh/config','r')
z = x.readlines()
# for line in z:
#     print(line) # printing config file
a = [line[:-1].replace('  ','') for line in z] # extracting characters in config file
b = [char for char in [c.split() for c in a]] # spliting characters
# now b is a list[list[str]]
# the main ssh command : ssh -i ~/.ssh/id_rsa git@github.com
# we have to pipe it to ansible so we need the path for ansible.cfg below
# [defaults]
# private_key_file = ~/.ssh/id_rsa
def clear(item):
    result = []
    for items in item:
        if isinstance(items, str):
            result.append(items)
        elif isinstance(items, (list, tuple)):
            result.extend(clear(items))
    return result

flatten_list = clear(b)
# print(flatten_list)
# 8 items exist for each host and for each host we need items
# with index : 3(hostname), 5(sshuser), 7(ssh_key)
# test = [flatten_list[5],flatten_list[3],flatten_list[7]]

def match_host(list):
    result = []
    current_host = {}
    for index, items in enumerate(list):
        if items == 'Host':
            if current_host:
                result.append(current_host)
            current_host = {'Host': list[index + 1]}
        elif items == 'User':
            current_host['remote_user'] = list[index + 1]
        elif items == 'IdentityFile':
            current_host['private_key_file'] = list[index + 1]
        elif items == 'HostName':
            current_host['hostname'] = list[index + 1]
        elif items == 'Port':
            current_host['Port'] = list[index + 1]
    
    if current_host:
        result.append(current_host)
    
    return result

hosts_dicts_list = match_host(flatten_list) # we have a list of dictionaries that show the hosts
x.close()