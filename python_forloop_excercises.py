#01 print number 1 to 5 
for i in range(1,6):
  print (i , end=" ")

#02 print the Even number 
for i in range (1 ,11):
    if i %2 == 0:
        print("this is even ",i)
    #else :
       # print("this is odd",i)

#03 sum the 1 to 5 counting 
total =0 
for  i in range (1,6):
    total += i
print("this is", total )
#04  reverse the letter "python"
word = 'python'
for i in range(len(word) -1 , -1 ,-1):

    print(word[i])

#05 check the vowel in word 
vowel = 'aeiou'
word = 'education'
count = 0 
for char in word:
    if char in vowel:
        count += 1
print("total vowels in",word, count )
#06 sequence of febonanci 
a = 0
b = 1
print(a , b ,end =" ")

for _ in range(8):
    update  = b + a
    print(update ,end =" ")
    a,b = b ,update
#07 factorial of 6
n = 3
f = 1 #6 
for i in range(1,n+1):
   #print(i)
    f *= i
print (f"this is factorial of {n} is {f}")

#08 is the number is prime or not 
num = 3
is_prime = True

for i in range(2, int(num ** 0.5)+1 ):
    if num % i == 0:
     is_prime = False
    break 
if is_prime and num >1:
        print(f'{num}  is a prime numebr ')
else :
    print(f"{num} is not a prime number ")
    
