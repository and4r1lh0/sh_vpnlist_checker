import base64
import qrcode as qr
#example
encryption = 'bf-cfb'
password = 'test'
ip = '192.168.100.1'
port = '8888'

uri = encryption+':'+password+'@'+ip+':'+port

#uri = 'bf-cfb:test@192.168.100.1:8888' #encryption_method:password@ip:port 
    
encoded_uri = base64.b64encode(uri.encode('utf-8'))
print('ss://%s' % encoded_uri.decode('utf-8'))

encoded_uri = encoded_uri.decode('utf-8')
decoded_uri = base64.b64decode(encoded_uri.encode('utf-8'))
print('%s' % decoded_uri.decode('utf-8'))

qr.make('ss://%s'+encoded_uri).save('image.png') #create QR code
