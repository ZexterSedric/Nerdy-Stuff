n=int(input('Enter limit number:\n'))
c=0
print('All prime numbers before',n)
for i in range(2,n):
    prime=True
    for j in range(2,i):
        m=i%j
        if m==0:
            prime=False
            break
    if prime:
        c+=1
        print(i)
    else:
        pass
print('Total number of prime numbers before',n,'is',c)