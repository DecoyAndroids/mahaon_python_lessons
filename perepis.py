f = open("Perepis.txt", "r")
l = list()
l1 = list()
for i in f:
    l.append(i)
    l1.append(i)
for i in range(len(l)):
    l1[i]=str(l[i])[-5:-1]
    if int(l1[i]) < 1978:
        print(l[i], end=" ")
a = int(input('year'))
for i in range(len(l)):
    l1[i]=str(l[i])[-5:-1]
    if int(l1[i]) < a:
        print(l[i], end=" ")
