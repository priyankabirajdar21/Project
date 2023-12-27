import copy

microservice_prefers = {
 'm1':  ['c4', 'c2', 'c1', 'c3'],
 'm2':  ['c4', 'c2', 'c1', 'c3'],
 'm3':  ['c4', 'c2', 'c1', 'c3'],
 'm4':  ['c4', 'c2', 'c1', 'c3'],
}
container_prefers = {
 'c1':  ['m2', 'm3', 'm4', 'm1'],
 'c2':  ['m2', 'm3', 'm4', 'm1'],
 'c3':  ['m2', 'm3', 'm4', 'm1'],
 'c4':  ['m2', 'm3', 'm4', 'm1'],
}


M = sorted(microservice_prefers.keys())
C = sorted(container_prefers.keys())
 
 
#print(type(M))

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
    #print("ms")
    print(m_free)
    matching1  = {}
    m_prefers2 = copy.deepcopy(microservice_prefers)
    c_prefers2 = copy.deepcopy(container_prefers)
    while m_free:
        m_s = m_free.pop(0)
        print("step")
        m_list = m_prefers2[m_s]
        c_s = m_list.pop(0)
        print(m_s)
        print(m_list)
        print(c_s)
        temp_matching = matching1.get(c_s)
        print(temp_matching)
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
#print()
'''print('Engagement stability check PASSED'
      if check(matching1) else 'Matching stability check FAILED')
 
print('\n\nSwapping two fiances to introduce an error')
matching1[C[0]], matching1[C[1]] = matching1[C[1]], matching1[C[0]]
for c in C[:2]:
    print('  %s is now mapped to %s' % (c, matching1[c]))
print()
print('Matching stability check PASSED'
      if check(matching1) else 'Matching stability check FAILED')'''

print(matching1)