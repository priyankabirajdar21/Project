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