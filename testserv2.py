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
    if string=='m1'or string=='m2' or string=='m3'or string=='m4'or string=='m5'or string=='m6'or string=='m7'or string=='m8'or string=='m9'or string=='m10':
        subprocess.call(['./3.sh', str(port2), cont])
    elif string=='m11'or string=='m12'or string=='m13'or string=='m14'or string=='m15'or string=='m16'or string=='m17'or string=='m18'or string=='m19'or string=='m20':
        subprocess.call(['./4.sh', str(port2), cont])
    elif string=='m21'or string=='m22'or string=='m23'or string=='m24'or string=='m25'or string=='m26'or string=='m27'or string=='m28'or string=='m29'or string=='m30':
        subprocess.call(['./5.sh', str(port2), cont])
    elif string=='m31'or string=='m32'or string=='m33'or string=='m34'or string=='m35'or string=='m36'or string=='m37'or string=='m38'or string=='39'or string=='m40':
        subprocess.call(['./6.sh', str(port2), cont])
    elif string=='m41'or string=='m42'or string=='m43'or string=='m44'or string=='m45'or string=='m46'or string=='m47'or string=='m48'or string=='m49'or string=='m50':
        subprocess.call(['./7.sh', str(port2), cont])
    elif string=='m51'or string=='m52'or string=='m53'or string=='m54'or string=='m55'or string=='m56'or string=='m57'or string=='m58'or string=='m59'or string=='m60':
        subprocess.call(['./8.sh', str(port2), cont])
    elif string=='m61'or string=='m62'or string=='m63'or string=='m64'or string=='m65'or string=='m66'or string=='m67'or string=='m68'or string=='m69'or string=='m70':
        subprocess.call(['./9.sh', str(port2), cont])
    elif string=='m71'or string=='m72'or string=='m73'or string=='m74'or string=='m75'or string=='m76'or string=='m77'or string=='m78'or string=='m79'or string=='m80':
        subprocess.call(['./10.sh', str(port2), cont])
    elif string=='m81'or string=='m82'or string=='m83'or string=='m84'or string=='m85'or string=='m86'or string=='m87'or string=='m88'or string=='m89'or string=='m90':
        subprocess.call(['./11.sh', str(port2), cont])
    elif string=='m91'or string=='m92'or string=='m93'or string=='m94'or string=='m95'or string=='m96'or string=='m97'or string=='m98'or string=='m99'or string=='m100':
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
