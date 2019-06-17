def selectionSort(l):
 for start in range(len(l)):#scanning the slices from l[0:len(l)-1]
  minpos=start
  for i in range(start,len(l)):
    if l[i]<l[minpos]:
       minpos=i

    #and move it to start of slice
  (l[start],l[minpos])=(l[minpos],l[start])
  
    

l=input('enter the no: ').split()
l=[int(x) for x in l]
selectionSort(l)
print('Sorted list: ',end='')
print(l)
   