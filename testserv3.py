import socket
import subprocess
import time
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
s = socket.socket()
port = 12359
port2 = 9010
port3 = port2
s.bind(('localhost', port))

s.listen(5)
print('Waiting for connection...')

c, addr = s.accept()
print ('Got connection from', addr)
count = int(c.recv(1024).decode())
print(count)

c, addr = s.accept()
x=0
strings = []
while x<count:
    string = c.recv(1024).decode()
    print(string)
    strings.append(string)
    x=x+1

print(strings)
col = 2
for string in strings:
    start_time = time.time()
    subprocess.call(['./3.sh', str(port2)])
    time.sleep(7)
    s3 = socket.socket()
    s3.connect(('localhost', port2))
    s3.send(bytes(str(port), 'utf-8'))
    port2=port2+1
    print(s3.recv(1024).decode())
    time_taken = round((time.time() - start_time),2)
    sheet1.write(4, col, time_taken)
    col = col+1
    s3.close()
wb.save('xlwt2.xls')
time.sleep(20)

subprocess.call(['./1.sh', str(port2)])