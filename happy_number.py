import math

def digitsSquareSum(Number):
    sum=rem=0
    while Number>0:
      rem=Number%10
      sum=sum+math.pow(rem,2)
      Number=Number//10
    return sum
    
    
Number=int(input())
Temp=Number


while Temp!=1 and Temp!=4:
     Temp=digitsSquareSum(Temp)
    
    
    
if Temp ==1:
    print("True")
else:
    print("False")
    