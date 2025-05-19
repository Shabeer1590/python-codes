# sum of odd digits
odd=0
for num in range(1,11):
   if num%2 != 0:
       odd += num
print("sum of odd numbers from 1 to 11 is:",odd)

#.............................................
# sum of even numbers
even=0
for num in range(1,11):
    if num%2 == 0:
       even += num
print("sum of even numbers from 1 to 10 is", even)
#..............................................
# sum of all 1-10 digits
sum=0
for num in range(1,11):
   for digit in str(num):
      sum +=int(digit)
print("sum of all digits from 1 to 11:",sum)  

#.............................................
# greatest of two numbers
num1=int(input("enter a number:" ))
num2=int(input("enter a number:" ))
if num1>num2:
   print("The greatest number is:",num1)
elif num2>num1:
   print("The greatest number is:",num2)
else:
   print("Both are equal")  
    #.........................................
# greatest of 3 numbers
a=int(input("Enter a number:", )) 
b=int(input("Enter a number:", ))
c=int(input("Enter a number:", )) 
if a>=b and a>=c :
  greatest=a
elif b>=a and b>=c:
  greatest=b
else:
 greatest=c
print("the greatest number is:", greatest)
# ..............................................
# prime numbers b/w 1-10
for x in range(1,11):
    for y in range(2,x):
      if x%y==0:
         break
    else:
        print(x)
# ..................................
# m=int(input('Enter '))
if (m%4==0 and m%100!=0) or (m%400==0):
    print('leapyear')
else:
    print('not a leapyear')
