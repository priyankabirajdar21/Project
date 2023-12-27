import socket
import random
import copy
import time
import itertools
import subprocess
import time

microservice_prefers = {
'm1':  ['12350', '12359', '12360'],
'm2':  ['12350', '12359', '12360'],
'm3':  ['12350', '12359', '12360'],
'm4':  ['12350', '12359', '12360'],
'm5':  ['12350', '12359', '12360'],
}

microservice_req = {
    'm1': 1,
    'm2': 4,
    'm3': 5,
    'm4': 3,
    'm5': 3,
}

virtual_machine_prefers = {
'12359':  ['m3', 'm4', 'm5', 'm1', 'm2'],
'12360':  ['m3', 'm4', 'm5', 'm1', 'm2'],
'12350':  ['m3', 'm4', 'm5', 'm1', 'm2'],
}

vm_cap = {
    '12359': 6,
    '12360': 10,
    '12350': 5,
}

M = sorted(microservice_prefers.keys())
V = sorted(virtual_machine_prefers.keys())



'''def check(matching1):
    inversematching = dict((v,k) for k,v in matching1.items())
    for c, m in matching1.items():
        c_likes = container_prefers[c]
        c_likesbetter = c_likes[:c_likes.index(m)]
        m_likes = microservice_prefers[m]
        m_likesbetter = m_likes[:m_likes.index(c)]
        for m_s in c_likesbetter:
            ms_cs = inversematching[m_s]
            m_likes = microservice_prefers[m_s]
            if m_likes.index(ms_cs) > m_likes.index(c):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (c, m_s, m, ms_cs))
                return False
        for c_s in m_likesbetter:
            cs_ms = matching1[c_s]
            c_likes = container_prefers[c_s]
            if c_likes.index(cs_ms) > c_likes.index(m):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (m, c_s, c, cs_ms))
                return False
    return True
 
def matchmaker():
    m_free = M[:]
    matching1  = {}
    m_prefers2 = copy.deepcopy(microservice_prefers)
    c_prefers2 = copy.deepcopy(container_prefers)
    while m_free:
        m_s = m_free.pop(0)
        m_list = m_prefers2[m_s]
        c_s = m_list.pop(0)
        temp_matching = matching1.get(c_s)
        if not temp_matching:
            # She's free
            matching1[c_s] = m_s
            print("  %s and %s" % (m_s, c_s))
        else:
            # The bounder proposes to an engaged lass!
            c_list = c_prefers2[c_s]
            if c_list.index(temp_matching) > c_list.index(m_s):
                # She prefers new guy
                matching1[c_s] = m_s
                print("  %s dumped %s for %s" % (c_s, temp_matching, m_s))
                if m_prefers2[temp_matching]:
                    # Ex has more girls to try
                    m_free.append(temp_matching)
            else:
                # She is faithful to old fiance
                if m_list:
                    # Look again
                    m_free.append(m_s)
    return matching1
 
 
print('one-to-one matching')
matching1 = matchmaker()
 
print('\nFinal Matching:')
print('  ' + ',\n  '.join('%s is mapped to %s' % i
                          for i in sorted(matching1.items())))

     new      '''

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
        m_list = m_prefers2[m_s]
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
    return matching1
 
 
print('one-to-one matching')
matching1 = matchmaker()
 
print('\nFinal Matching:')
print('  ' + ',\n  '.join('%s is mapped to %s' % i
                          for i in sorted(matching1.items())))


print(matching1)

for port in matching1:
    s3 = socket.socket()
    s3.connect(('localhost', int(port)))
    s3.send(bytes(str(len(matching1[port])),'utf-8'))
    s3.close()

for port in matching1:
    s3 = socket.socket()
    print(port)
    print(matching1[port])
    s3.connect(('localhost', int(port)))
    for module in matching1[port]:
        print(module)
        s3.send(bytes(str(module),'utf-8'))
        time.sleep(0.5)
        
    s3.close()