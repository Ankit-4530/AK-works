# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
print("enter the inputs")
n=int(input("number1="))
num2 = int(input("number2="))

print("The L.C.M. is equal to", compute_lcm(n, num2))