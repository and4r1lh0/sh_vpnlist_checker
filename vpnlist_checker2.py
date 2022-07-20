import base64
import re
import ping
#import simple_ping as s #scan default port
import navlock
from portscan import scan_port
import pygeoip

def proc(str):
    sharp_replace = str.partition('#')[0]
    result = sharp_replace.replace('ss://', '', 1)
    return result

def parse(encstr):
    decoded_uri = base64.b64decode(encstr.encode('utf-8'))
    return('%s' % decoded_uri.decode('utf-8'))

def remove_subdomain(text):
    return(text.replace(text, '.'.join(text.split('.')[-2:])))

i=1
file = open("out_full.txt", "r")
file2 = open("output.txt", "w")

while True:
    line = file.readline()
    if not line:
        break
   
    #ver1
    cur_line = (line.strip())
    cyphertext = proc(cur_line)
    open_ip = parse(cyphertext)
    plaintext = open_ip.partition(':')[-1]

    cypher = open_ip.partition(':')[0]
    ip_and_port = plaintext.partition('@')[-1]
    port = ip_and_port.partition(':')[-1]
    host = ip_and_port.partition(':')[0]

    ##ver2
    #cur_line = (line.strip())
    #cyphertext = proc(cur_line)
    ##plaintext = open_ip.partition(':')[-1]
    ##cypher = cyphertext.partition(':')[0]
    #ip_and_port = cyphertext.partition('@')[-1]
    #port = ip_and_port.partition(':')[-1]
    #host = ip_and_port.partition(':')[0]

    ping_attempt = scan_port(host,int(port)) #scan custom port
    #ping_attempt = s.myping(host) #scan default port

    if ping_attempt==None:
        pass
    #elif cypher == 'aes-256-cfb': #customized cypher
    else:
        #pinga = ping.main(host) #ping attempt

        GEOIP = pygeoip.GeoIP("GeoIP.dat", pygeoip.MEMORY_CACHE)
        #GeoIP Legacy Databases (DAT): https://www.miyuru.lk/geoiplegacy
        ##https://c-s.net.ua/url?u=https%3A%2F%2Fdl.miyuru.lk%2Fgeoip%2Fmaxmind%2Fcountry%2Fmaxmind4.dat.gz

        try:
            country = GEOIP.country_name_by_addr(host)
        except:
            #host=(remove_subdomain(host))
            #country = GEOIP.country_name_by_addr(host)
            print('')

        #country = 'Null'
        pinga = None
        if pinga == None:
            pinga = [0,'Err']
        print('№ ',i,'\tIP: ',host,'\t| Ping: ',pinga[1],'\t| Country: ',country)
        i+=1
        #file2.write(line + '\n')
        file2.writelines(line)
file2.close()
file.close()