a = 'aayush'
b = 'notso'
c = []
d=''
for i in range (0, len(a),1):
    c.append(a[i])

for  j in range (0, len(b),1):
    c.append(b[j])
print(c)
for i in c:
    if c.count(i)==1:
        d=d+i

print(d)
