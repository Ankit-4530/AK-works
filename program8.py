n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
def getSum(n):  
     
    sum = 0
    for digit in str(rev):   
      sum += int(digit)        
    return sum
    
n = rev
print(getSum(rev))