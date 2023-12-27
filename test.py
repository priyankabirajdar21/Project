from ast import Dict
import socket
import random
import copy
import time
import itertools
import subprocess
import time

from regex import P
from topsis import Topsis
import numpy as np
import xlwt
from xlwt import Workbook
import sys

'''
    evalaution matrix of microservices
    parameters:
    execution time      dedaline       resources requirements
'''

s1 = socket.socket()
port = 9080
host = socket.gethostname()
#host = sys.argv[1]
print(host)
s1.bind((host, port))

s1.listen(5)
print('Waiting for connection...')

portserv=12350
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
ips = ['13.233.47.221','13.235.90.1','43.204.214.254','13.232.22.250','35.154.223.214']

micro_ran_list = []
for i in range(1,101):
    temp=str(i)
    micro_ran_list.append('m'+temp)

microservice_req ={}
for i in micro_ran_list:
    microservice_req[i]=random.randint(1,100)

temp_val=list(microservice_req.values())

'''microservice_req = {
    'm1': 1,
    'm2': 4,
    'm3': 5,
    'm4': 3,
    'm5': 3,
}'''

vm_cap = {
    ips[1]: 600,
    ips[2]: 1000,
    ips[0]: 1500,
    ips[4]: 1000,
    ips[3]: 600,
}

evaluation_matrix=[]
for i in range(100):
    l1=[]
    l1.append(random.randrange(1,100))
    l1.append(random.randrange(100,500))
    l1.append(temp_val[i])
    evaluation_matrix.append(l1)
    
print(evaluation_matrix)
start_time = time.time()
'''evaluation_matrix = np.array([
    [5,40,1],
    [8,10,4],
    [2,12,5],
    [10,30,3],
    [12,25,3],
])'''



weights = [0.25, 0.50, 0.25]

'''
if higher value is preferred - True
if lower value is preferred - False
'''
criterias = np.array([True, True, True])

t = Topsis(evaluation_matrix, weights, criterias)

t.calc()
b_list= []

print("best_distance\t", t.best_distance)
print("worst_distance\t", t.worst_distance)

# print("weighted_normalized",t.weighted_normalized)

print("worst_similarity\t", t.worst_similarity)
print("rank_to_worst_similarity\t", t.rank_to_worst_similarity())

print("best_similarity\t", t.best_similarity)
b_list = t.rank_to_best_similarity()
print("rank_to_best_similarity\t", t.rank_to_best_similarity())
print(b_list)

d = {}
k=1
for i in b_list:
    j='m' + str(k)
    d[j]=i
    k=k+1
print(d)

s = {}
s= dict(sorted(d.items(), key=lambda item: item[1]))
print(s)

p_list = []
for i in s:
    p_list.append(i)

print(p_list)


pref_list = [ips[0], ips[2], ips[4], ips[1], ips[3]]

microservice_prefers = {}
for i in range(1,101):
    j='m' + str(i)
    microservice_prefers[j] = copy.deepcopy(pref_list)



'''microservice_prefers = {
'm1':  pref_list,
'm2':  pref_list,
'm3':  pref_list,
'm4':  pref_list,
'm5':  pref_list,
'm6':  pref_list,
'm7':  pref_list,
'm8':  pref_list,
'm9':  pref_list,
'm10': pref_list,

}'''

#print("pre" ,microservice_prefers)

#print("check", microservice_prefers['m10'])

virtual_machine_prefers = {
ips[1]:  copy.deepcopy(p_list),
ips[2]:  copy.deepcopy(p_list),
ips[0]:  copy.deepcopy(p_list),
ips[3]:  copy.deepcopy(p_list),
ips[4]:  copy.deepcopy(p_list),
}
print("fvxdw", virtual_machine_prefers)

M = sorted(microservice_prefers.keys())
V = sorted(virtual_machine_prefers.keys())

def matchmaker():
    m_free = M[:]
    #print("ms")
    print(m_free)
    matching1  = {}
    m_prefers2 = copy.deepcopy(microservice_prefers)
    vm_prefers2 = copy.deepcopy(virtual_machine_prefers)
    while m_free:
        m_s = m_free.pop(0)
        print("step")
        print(matching1)
        #print(m_list)
        m_list = m_prefers2[m_s]
        if not m_list:
            break
        vm_s = m_list.pop(0)
        print(m_s)
        print(m_list)
        print(vm_s)
        temp_matching = matching1.get(vm_s)
        print(temp_matching)
        if not temp_matching:
            # She's free
            if vm_cap[vm_s] >= microservice_req[m_s]:
                matching1[vm_s] = [m_s]
                print(vm_cap[vm_s])
                vm_cap[vm_s] = vm_cap[vm_s] - microservice_req[m_s]
                print(vm_cap[vm_s])
                print("  %s and %s" % (m_s, vm_s))
        else:
            # The bounder proposes to an engaged lass!
            print("hi")
            print(vm_cap[vm_s])
            if vm_cap[vm_s] >= microservice_req[m_s]:
                matching1[vm_s].append(m_s)
                vm_cap[vm_s] = vm_cap[vm_s] - microservice_req[m_s]
            else:
                vm_list = vm_prefers2[vm_s]
                print(vm_list)
                print(matching1)
                temp_rejection = matching1.get(vm_s)
                print(matching1)
                print(temp_rejection)
                rejected = []
                selected = []
                f=0
                temp_cap=0
                while temp_rejection:
                    print(matching1)
                    microservice_addon = temp_rejection.pop(0)
                    print(matching1)
                    print(microservice_addon)
                    print(vm_list.index(microservice_addon))
                    print(vm_list.index(m_s))
                    print(matching1)
                    if vm_list.index(microservice_addon) > vm_list.index(m_s):
                        # She prefers new guy
                        rejected.append(microservice_addon)
                        print("rej", rejected)
                        temp_cap = temp_cap + microservice_req[microservice_addon] + vm_cap[vm_s]
                        print(temp_cap)
                        if temp_cap >= microservice_req[m_s]:
                            f=1
                            break

                    else:
                        selected.append(microservice_addon)
                        f=0
                while temp_rejection:
                    x = temp_rejection.pop(0)
                    selected.append(x)
                print(selected)
                matching1[vm_s] = selected
                print(matching1)
                if f==1:
                    #matching1[vm_s] = selected
                    matching1[vm_s].append(m_s)
                    vm_cap[vm_s] = temp_cap - microservice_req[m_s]
                    m_free = m_free + rejected
                    '''else:
                        selected.append(container_addon)
                        matching1[vm_s] = c_s
                        print("  %s dumped %s for %s" % (vm_s, temp_matching, c_s))
                        if c_prefers2[temp_matching]:
                            # Ex has more girls to try
                            c_free.append(temp_matching)'''
                else:
                        # She is faithful to old fiance
                    if m_list:
                            # Look again
                        m_free.append(m_s)
        print(matching1)
        print(m_free)
        print(m_list)
    return matching1
 
 
print('one-to-one matching')
matching1 = matchmaker()
 
print('\nFinal Matching:')
print('  ' + ',\n  '.join('%s is mapped to %s' % i
                          for i in sorted(matching1.items())))

count_list = []
total=0
for i in matching1:
    count_list.append(len(matching1[i]))
    total= total + len(matching1[i])
    print("count", len(matching1[i]))

print(count_list)
print(total)
print(total/100)

print(matching1)

for ip in matching1:
    s3 = socket.socket()
    s3.connect((ip, portserv))
    s3.send(bytes(str(len(matching1[ip])),'utf-8'))
    s3.close()

for ip in matching1:
    s3 = socket.socket()
    print(ip)
    print(matching1[ip])
    s3.connect((ip, portserv))
    for module in matching1[ip]:
        print(module)
        s3.send(bytes(str(module),'utf-8'))
        time.sleep(0.5)
        
    s3.close()
#subprocess.call(['./2.sh'])

for ip in ips:
    c1, addr = s1.accept()
    print ('Got connection from', addr)
    print(c1.recv(1024).decode())
    c1.close()

time_taken = round((time.time() - start_time),2)
sheet1.write(1, 0, "Time Taken")
sheet1.write(1, 1, time_taken)
wb.save('xlwt10.xls')
