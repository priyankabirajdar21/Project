import socket
import random
import copy
import time
import itertools
import subprocess

microservice_prefers = {
 'm1':  ['12348', '12350', '12359', '12360'],
 'm2':  ['12348', '12350', '12359', '12360'],
 'm3':  ['12348', '12350', '12359', '12360'],
 'm4':  ['12348', '12350', '12359', '12360'],
}
container_prefers = {
 '12359':  ['m2', 'm3', 'm4', 'm1'],
 '12350':  ['m2', 'm3', 'm4', 'm1'],
 '12360':  ['m2', 'm3', 'm4', 'm1'],
 '12348':  ['m2', 'm3', 'm4', 'm1'],
}


M = sorted(microservice_prefers.keys())
C = sorted(container_prefers.keys())
 
 
def check(matching1):
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


print(matching1)

for module in matching1:
    s3 = socket.socket()
    print(module)
    print(matching1[module])
    s3.connect(('localhost', int(module)))
    s3.send(bytes(str(matching1[module]),'utf-8'))
    s3.close()