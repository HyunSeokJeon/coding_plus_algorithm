
bdict = {chr(i):0 for i in range(ord('A'),ord('Z')+1)}
a = '3	2	1	2	4	3	1	3	1	1	3	1	3	2	1	2	2	2	1	2	1	1	1	2	2	1'.split('\t')
b = 0
for i in bdict.keys():
    bdict[i] = a[b]
    b+=1

n, m = list(map(int, input().split()))
aa, bb = input().split()
sml= min(len(aa), len(bb))

test = list()
for i in range(sml):
    test.append(aa[i])
    test.append(bb[i])
if len(aa)>len(bb):
    cc = aa
else:
    cc = bb
for i in range(sml, len(cc)):
    test.append(cc[i])

sample = list()
for i in test:
    sample.append(bdict[i])
while len(sample) != 2:
    for i in range(1, len(sample)):
        sample[i-1] = (int(sample[i])+int(sample[i-1]))%10
    sample.pop()

if sample[0] == 0:
    sample[0] = ''
print(str(sample[0])+str(sample[1])+'%')