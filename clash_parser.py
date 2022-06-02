import re
import ping 

with open('input.txt', 'r', encoding='utf-8') as f:
    ip_add = (re.findall(r'[0-2]\d{2}\.[0-2]\d{2}\.[0-2]\d{2}\.[0-2]\d{2}', f.read()))

for i in ip_add:

    ping.main(i)

#for el in enumerate ip_add:

#host = 'ya.ru'
#ping.main(host)