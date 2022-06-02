from subprocess import Popen, PIPE, STDOUT
import re

def main(host):
    ping_res = Popen("ping -n 1 -w 1 "+host, stdout=PIPE, stderr=STDOUT)
    text = ''
    for line in ping_res.stdout.readlines():
        text += line.decode('cp866')

    items = re.findall(r'время=(\d+)', text)
    if len(items)!=0:
        if int(items[0])<100:
            return (host,int(items[0]))
            #print(text)