import socket
import subprocess
import time
import xlwt
from xlwt import Workbook
import sys

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
cont = sys.argv[1]
s = socket.socket()
port = 12350
port2 = 9030
port3 = port2
host = socket.gethostname()
s.bind((host, port))

s.listen(5)
print('Waiting for connection...')

c, addr = s.accept()
print ('Got connection from', addr)
count = int(c.recv(1024).decode())
print(count)

c, addr = s.accept()
print ('Got connection from', addr)
x=0
strings = []
while x<count:
    string = c.recv(1024).decode()
    print(string)
    strings.append(string)
    x=x+1

print(strings)
col = 2
start_time = time.time()
for string in strings:
    if string=='m1'or string=='m2' :
        subprocess.call(['./3.sh', str(port2), cont])
    elif string=='m3'or string=='m4':
        subprocess.call(['./4.sh', str(port2), cont])
    elif string=='m5'or string=='m6':
        subprocess.call(['./5.sh', str(port2), cont])
    elif string=='m7'or string=='m8':
        subprocess.call(['./6.sh', str(port2), cont])
    elif string=='m9'or string=='m10':
        subprocess.call(['./7.sh', str(port2), cont])
    elif string=='m11'or string=='m12':
        subprocess.call(['./8.sh', str(port2), cont])
    elif string=='m13'or string=='m14':
        subprocess.call(['./9.sh', str(port2), cont])
    elif string=='m15'or string=='m16':
        subprocess.call(['./10.sh', str(port2), cont])
    elif string=='m17'or string=='m18':
        subprocess.call(['./11.sh', str(port2), cont])
    elif string=='m19'or string=='m20':
        subprocess.call(['./12.sh', str(port2), cont])
    port2=port2+1

port2=port3

for string in strings:
    c, addr = s.accept()
    print ('Got connection from', addr)
    print(c.recv(1024).decode())
    c.close()
    port2=port2+1

port2=port3
subprocess.call(['./2.sh'])

for string in strings:
    s3 = socket.socket()
    s3.connect(('0.0.0.0', port2))
    print(s3.recv(1024).decode())
    port2=port2+1
    s3.close()

s3 = socket.socket()
s3.connect((sys.argv[2], 9080))
s3.send(bytes('Done','utf-8'))
s3.close()

time_taken = round((time.time() - start_time),2)
sheet1.write(4, col, time_taken)
wb.save('xlwt3.xls')
time.sleep(60)

subprocess.call(['./1.sh'])
