q=1
while 0<1:
    Goldbach=True
    c=0
    n=2*q
    y=[]
    for i in range(2,n):
        prime=True
        for j in range(2,i):
            m=i%j
            if m==0:
                prime=False
                break
        if prime:
            y.append(i)
        else:
            pass
    for a in range(0,len(y)):
        for b in range(0,len(y)):
            s=y[a]+y[b]
            if s==n:
                Goldbach=True
                c+=1
            else:
                pass
    if c==0:
        Goldbach=False
    print('Goldbach is',Goldbach)
    q+=1