s = 0
n = 0
a = []
while True:
    num=input()
    if len(num)==0:
        break
    k=int(num)
    a.append(k)
    s+=k
    n+=1
avg=s/n
print(avg)
for x in a:
    if x<avg:
        print(x)
for x in a:
    if x==avg:
        print(x)
for x in a:
    if x>avg:
        print(x)
