def insertionsort(seq):
  for sliceEnd in range(len(seq)):
  	#building a longer and sorted slices in seq[0:slice end]
  	#move the first element after sorted slices placed
  	#till it is in correct place
  	pos=sliceEnd
  	while pos> 0 and seq[pos]<seq[pos-1]:
  	  (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
  	  pos=pos-1

seq=input('enter the no: ').split()
seq=[int(x) for x in seq]
insertionsort(seq)
print('Sorted list: ',end='')
print(seq)


#time complexity O(n^2)