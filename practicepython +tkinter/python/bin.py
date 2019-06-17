#dupicates in the string
''''from Collection import Counter
def dup(x):
	wc=Counter(input)
	j=-1
	for i in wc.values():
		j=j+1
		if(i>1):
			print(wc.keys()[j])
if __name__ == '__main__':
	input="geeksssggh"
	dup(input)
'''
def dup(x):
	size=len((x))
	repeated=[]
	for i in range(size):
		k=i+1
		for j in range(k,size):
			if x[i]==x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated
if __name__ == '__main__':
	x="geeksss"
	c=list(x)
	print(dup(c))





