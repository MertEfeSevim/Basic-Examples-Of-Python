counts=dict()
names = ['csev','cwen','csev','zqian','cwen']

for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name] = counts[name]+1
    print(counts)


counts1 = {"chuck" : 1, "fred":2}
for key in counts1:
    print(key,counts1[key])