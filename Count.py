n=int,input()
a=list(map(int,input().split()))
c=0
c1=0
for i in a:
    if(i%2==0):
        c+=1
    elif(i%2==1):
        c1+=1
print(c,c1)

