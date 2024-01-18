f = open('travels.txt','r')
l=list()
a=0
b=0
c=0
g = 0
r =0
s = 0
c1 = 0
c2 = 0
c3 = 0
a2=0
b2=0
l3 = set()
l4 = set()
for i in f:
    l.append(i[:2])
    i1 = i[10:]
    g = i1.find(' ')
    i2 = i1[g+1:]
    g2 = i2.find(' ')
    #print(i2[:g])
    #print(i[10:10+g])#[-4:]
    if int(i[:2]) == 1:
        a = a + 1
        a2 = a2 + int(i[-4:-1])
    elif int(i[:2]) == 2:
        b = b + 1
        b2 = b2 + int(i[-4:-1])
    elif int(i[:2]) == 3:
        c = c + 1
        c2 = c2 + int(i[-4:-1])
        s = s + int(i[-11:-7])
    if i[10:10+g] == "Липки":
        r = r + int(i[-4:-1])
        c1 = c1 + 1
    l3.add(i[10:10+g] + ' 0')
    l4.add(i2[:g2] + ' 0')

L4 = list(l3)
L5 = list(l4)
f.close()
f = open('travels.txt','r')
for i in f:
    #print(i,' ',i[-8:-5])
    i1 = i[10:]
    g = i1.find(' ')
    i2 = i1[g + 1:]
    g2 = i2.find(' ')
    for j in range(len(L4)):
        st = L4[j]
        if i[10:10+g] == str(L4[j])[:g]:
            g1 = str(L4[j]).find(' ')
            mi = int(st[g1+1:]) + int((i[-4:])[:3])
            L4[j] = st[:g]+ ' ' + str(mi)
            break
    for k in range(len(L5)):
        st = L5[k]
        if i2[:g2] == str(L5[k])[:g2]:
            g1 = str(L5[k]).find(' ')
            st_m = str(st[g2+1:])
            g3 = st_m.find(' ')
            mi = int(st[g2+1:]) + int((i2[-4:])[:3])
            print(st[g3:], st[g2:])
            #benz = int(st[:g2+1])
            L5[k] = st[:g2] + ' ' + str(mi) + ' ' + str()
            break

#print(L4)

L1 = [a,b,c]
for i in range(len(L1)):
    if L1[i] == max(L1):
        if i == 0:
            d = 'первый'
            v = a2
        if i == 1:
            d = 'второй'
            v = b2
        if i == 2:
            d = 'третий'
            v = c2
print(d,max(L1),v)
print('Липки',r)
print('1 octover',s,'km')
print(L4)
print(L5)