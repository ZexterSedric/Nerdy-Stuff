from matplotlib import pyplot as plt
ver=int(input('Enter number:\t'))
f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
f7=0
f8=0
f9=0
n=[1,2,3,4,5,6,7,8,9]
while ver>1:
    if ver%2==0:
        ver=ver/2
        m=str(ver)
        if (m[0])=='1':
            f1+=1
        elif (m[0])=='2':
            f2+=1
        elif (m[0])=='3':
            f3+=1
        elif (m[0])=='4':
            f4+=1
        elif (m[0])=='5':
            f5+=1
        elif (m[0])=='6':
            f6+=1
        elif (m[0])=='7':
            f7+=1
        elif (m[0])=='8':
            f8+=1
        elif (m[0])=='9':
            f9+=1
    else:
        ver=3*ver+1
        m=str(ver)
        if (m[0])=='1':
            f1+=1
        elif (m[0])=='2':
            f2+=1
        elif (m[0])=='3':
            f3+=1
        elif (m[0])=='4':
            f4+=1
        elif (m[0])=='5':
            f5+=1
        elif (m[0])=='6':
            f6+=1
        elif (m[0])=='7':
            f7+=1
        elif (m[0])=='8':
            f8+=1
        elif (m[0])=='9':
            f9+=1
b=[f1,f2,f3,f4,f5,f6,f7,f8,f9]
plt.bar(n,b,color='black')
plt.show()