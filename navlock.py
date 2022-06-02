#def ipInfo(addr=''):
#    from urllib.request import urlopen
#    from json import load
#    if addr == '':
#        url = 'https://ipinfo.io/json'
#    else:
#        url = 'https://ipinfo.io/' + addr + '/json'
#    res = urlopen(url)
#    #response from url(if res==None then check connection)
#    data = load(res)
#    #will load the json response into data
#    mas=[]
#    for attr in data.keys():
#        #will print the data line by line
#        mas +=(attr,data[attr])
#    #print(mas)
#    return mas

def ipInfo(addr=''):
    from ip2geotools.databases.noncommercial import DbIpCity
    response = DbIpCity.get(addr, api_key='free')
    return response.country
