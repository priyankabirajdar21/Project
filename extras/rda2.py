import copy

#from matplotlib import container

'''container_prefers = {
    'a':  ['B', 'A', 'C'],
    'b':  ['A', 'B', 'C'],
    'c':  ['A', 'B', 'C'],
    'd':  ['B', 'A'],
    'e':  ['B'],
}

container_req = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 6,
}

virtual_machine_prefers = {
    'A':  ['d', 'c', 'b', 'a'],
    'B':  ['e', 'd', 'c', 'b', 'a'],
    'C':  ['a', 'c', 'b'],
}

vm_cap = {
    'A': 5,
    'B': 6,
    'C': 3,
}'''


'''container_prefers = {
    'c1':  ['vm3', 'vm1', 'vm2'],
    'c2':  ['vm2'],
    'c3':  ['vm3', 'vm1', 'vm2'],
    'c4':  ['vm3', 'vm1', 'vm2'],
}

container_req = {
    'c1': 1,
    'c2': 4,
    'c3': 2,
    'c4': 2,
}

virtual_machine_prefers = {
    'vm1':  ['c3', 'c4', 'c1'],
    'vm2':  ['c2', 'c3', 'c4', 'c1'],
    'vm3':  ['c3', 'c4', 'c1'],
}

vm_cap = {
    'vm1': 3,
    'vm2': 6,
    'vm3': 2,
}'''

container_prefers = {
    'c1':  ['vm3', 'vm1', 'vm2'],
    'c2':  ['vm3', 'vm1', 'vm2'],
    'c3':  ['vm3', 'vm1', 'vm2'],
    'c4':  ['vm3', 'vm1', 'vm2'],
    'c5':  ['vm3', 'vm1', 'vm2'],
}

container_req = {
    'c1': 1,
    'c2': 4,
    'c3': 5,
    'c4': 3,
    'c5': 3,
}

virtual_machine_prefers = {
    'vm1':  ['c3', 'c4', 'c5', 'c1', 'c2'],
    'vm2':  ['c3', 'c4', 'c5', 'c1', 'c2'],
    'vm3':  ['c3', 'c4', 'c5', 'c1', 'c2'],
}

vm_cap = {
    'vm1': 6,
    'vm2': 10,
    'vm3': 5,
}

C = sorted(container_prefers.keys())
V = sorted(virtual_machine_prefers.keys())

def matchmaker():
    c_free = C[:]
    #print("ms")
    print(c_free)
    matching1  = {}
    c_prefers2 = copy.deepcopy(container_prefers)
    vm_prefers2 = copy.deepcopy(virtual_machine_prefers)
    while c_free:
        c_s = c_free.pop(0)
        print("step")
        print(matching1)
        c_list = c_prefers2[c_s]
        vm_s = c_list.pop(0)
        print(c_s)
        print(c_list)
        print(vm_s)
        temp_matching = matching1.get(vm_s)
        print(temp_matching)
        if not temp_matching:
            # She's free
            if vm_cap[vm_s] >= container_req[c_s]:
                matching1[vm_s] = [c_s]
                print(vm_cap[vm_s])
                vm_cap[vm_s] = vm_cap[vm_s] - container_req[c_s]
                print(vm_cap[vm_s])
                print("  %s and %s" % (c_s, vm_s))
        else:
            # The bounder proposes to an engaged lass!
            print("hi")
            print(vm_cap[vm_s])
            if vm_cap[vm_s] >= container_req[c_s]:
                matching1[vm_s].append(c_s)
                vm_cap[vm_s] = vm_cap[vm_s] - container_req[c_s]
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
                    container_addon = temp_rejection.pop(0)
                    print(matching1)
                    print(container_addon)
                    print(vm_list.index(container_addon))
                    print(vm_list.index(c_s))
                    print(matching1)
                    if vm_list.index(container_addon) > vm_list.index(c_s):
                        # She prefers new guy
                        rejected.append(container_addon)
                        print("rej", rejected)
                        temp_cap = temp_cap + container_req[container_addon] + vm_cap[vm_s]
                        print(temp_cap)
                        if temp_cap >= container_req[c_s]:
                            f=1
                            break

                    else:
                        selected.append(container_addon)
                        f=0
                while temp_rejection:
                    x = temp_rejection.pop(0)
                    selected.append(x)
                print(selected)
                matching1[vm_s] = selected
                print(matching1)
                if f==1:
                    #matching1[vm_s] = selected
                    matching1[vm_s].append(c_s)
                    vm_cap[vm_s] = temp_cap - container_req[c_s]
                    c_free = c_free + rejected
                    '''else:
                        selected.append(container_addon)
                        matching1[vm_s] = c_s
                        print("  %s dumped %s for %s" % (vm_s, temp_matching, c_s))
                        if c_prefers2[temp_matching]:
                            # Ex has more girls to try
                            c_free.append(temp_matching)'''
                else:
                        # She is faithful to old fiance
                    if c_list:
                            # Look again
                        c_free.append(c_s)
        print(matching1)
        print(c_free)
    return matching1
 
 
print('one-to-one matching')
matching1 = matchmaker()
 
print('\nFinal Matching:')
print('  ' + ',\n  '.join('%s is mapped to %s' % i
                          for i in sorted(matching1.items())))


