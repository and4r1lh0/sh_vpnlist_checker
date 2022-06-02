import socket

def scan_port(ip,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.1) #set timeout in sec 
  try:
     connect = sock.connect((ip,port))
     #print('Port :',port,' its open.')
     return 'open'
     sock.close()
  except:
     #pass
     return None
