d = {
    'vm2': ['c2'],
    'vm3': ['c1', 'c2'],
}

print(d)
#temp=[]
temp = d.get('vm3')
print(temp)
print(d)
x=temp.pop(0)
print(x)
print(d)