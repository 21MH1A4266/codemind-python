def perfect_number(N):
 sum=0
 for i in range(1,N):
   if(N%i==0):
      sum=sum+i
 return sum
N=int(input())
if(N==perfect_number(N)):
  print("True")
else:
  print("False")