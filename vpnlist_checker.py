import base64
import re
import ping
#import simple_ping as s
import navlock
from portscan import scan_port

def proc(str):
    sharp_replace = str.partition('#')[0]
    result = sharp_replace.replace('ss://', '', 1)
    return result

def parse(encstr):
    decoded_uri = base64.b64decode(encstr.encode('utf-8'))
    return('%s' % decoded_uri.decode('utf-8'))

i=1
file = open("input.txt", "r")
file2 = open("output.txt", "w")

while True:
    line = file.readline()
    if not line:
        break
    cur_line = (line.strip())
    proc_line = proc(cur_line)
    parsed_line = parse(proc_line)
    double_parse = parsed_line.partition(':')[-1]
    port = double_parse.partition(':')[-1]
    
    ip_add = (re.search(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',parsed_line))
    ip_address = ip_add[0]
    ping_attempt = scan_port(ip_address,int(port))

    #ping_attempt = s.myping(ip_add[0])

    #if ping_attempt==None:
    #    pass
    #else: 

    if ping_attempt==None:
        pass
    else:
        pinga = ping.main(ip_address)
        country = navlock.ipInfo(ip_add[0])
        #country = country[9]
        if pinga == None:
            pinga = [0,'Err']
        print('№ ',i,'\tIP: ',ip_add[0],'\t| Ping: ',pinga[1],'\t| Country: ',country)
        i+=1
        #file2.write(line + '\n')
        file2.writelines(line)
file2.close()
file.close()
