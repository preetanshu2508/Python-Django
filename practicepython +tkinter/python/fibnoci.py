def fib(num):
  if num==0:
  	return(1)
  elif num==1:
  	return(0)
  else:
  	return fib(num-1)+fib(num-2)

x=fib(10)
print("fibonicai:",x)  