'''def cap(word):
	vowels=('a','i','o','u','e')
	for c in word:
		if c in vowels:
			res=c.capitalize()
			word=word.replace(c,res)
			print(word)


if __name__ == '__main__':
	x="abuios"
	b=cap(x)'''
#program to remove word

''''def remov(word):
	vowels =('a','i','o','u','e')
	for i in word:
		for i in vowels:
			res=word.replace(i,"")
	return res
if __name__ == '__main__':

	a="hellow"
	b=remov(a)
	print(b)'''
#to reverse a word
''''def rev(x):
	i=x.split(" ")
	y=i[-1::-1]
	o=" ".join(y)
	return o
if __name__ == '__main__':
	f="hemu is good boy"
	print(rev(f))'''

#sum of odd no and  even

''''def sum(x):
	sum=0
	for i in range(2,x+1,2):
		sum=sum+i
	return sum
a=10
print(sum(a))'''

#find nth fibonacci no

''''def fib(n):
	if n<0:
	 print("input correct")
	elif n==1:
		return 0
	elif n==2:
		return 1

	else:
		return fib(n-1)+fib(n-2)
if __name__ == '__main__':
	x=10
	print(fib(x))'''
#sum of fibo nacci series
''''def fsum(n):
	if n<=0:
		return 0
	fibo=[0]*(n+1)
	fibo[1]=1
	sum=fibo[0]+fibo[1]

	
	for i in range(2,n+1):
		fibo[i]=fibo[i-1]+fibo[i-2]
		sum=sum+fibo[i]
	return sum
if __name__ == '__main__':
	x=10
	print(fsum(x))''' 
#largest of three no
'''n1=40
n2=20
n3=50
if (n1>=n2) and (n1>=n3):
	print(n1)
elif (n2>=n1) and (n2>=n3):
	print(n2)
else: 
	print(n3)'''
'''def  fibo(n):

	if n<=1:
		return n
	else:
		return fibo(n-1)+fibo(n-2)
x=10
for i in range(x):
	print(fibo(i),end=" ")
	print()'''

'''def counting(n):
	count=0

	for i in n:
		if i=='a' or i=='i' or i=='o' or i=='u' or i=='e':
			count=count+1
	return count
if __name__ == '__main__':
	n="geekseeeuuu"
	x=n.lower()
	y=list(x)
	print(counting(y))'''
'''def factors(n):
	for i in range(1,n+1):
		if n%i==0:
			print(i)
if __name__ == '__main__':
	x=10
	v=factors(x)
	#print(max(factors(x)))
'''
'''def arm(a,b):
	for num in range(a,b):
		temp=num
		sum=0
		while temp>0:



			digit=temp%10
			sum=sum+digit**3
			temp=temp//10
		if sum==num:
		print (num)
if __name__ == '__main__':
	
	b=arm(1,600)'''
'''
import math
def nterm(n):
	#TN = a1 * r(N-1) 
	
	if (n%2==0):
			x=int(n/2)
			p=x
			r1=3
			tn=math.pow(r1,p-1)
			print(tn)
	else:
			
			x=int(n+1/2)
			p=x
			r=2
			tn=math.pow(r,p-1)
			print(tn)
if __name__ == '__main__':
	a=nterm(16)
'''

def fibonacci(n):
	t1=0
	t2=1
	for i in range(1, n+1): 
			nextTerm=t1+t2
			t1=t2
			t2=nextTerm
			print(t1)

def prime(n):
    primes = 1
    num = 2
    while primes <= n:
            mod = 1
            ptrue = True
            while mod < (num - 1):
                    if num%(num-mod) == 0:
                            ptrue = False
                            break
                    mod += 1
            if ptrue == True:
                    primes += 1
    return(num)

n=int(input())
if(n%2==1):
	fibonacci(int(n/2)+1)
else:
	print(prime(int(n/2)))