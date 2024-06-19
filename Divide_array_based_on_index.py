array=[]
evenarray=[]
oddarray=[]
n=int(input("enter the size of array:"))
for i in range(0,n):
  num= int(input("enter array element at {} index".format{i}))
  array.append(num)
  if i%2==0:
    evenarray.append(array[i])
  else:
     oddarray.append(array[i])
evenarray=sorted(evenarray)
print("the sorted evenarray are:",evenarray[0:len(evenarray]))
oddarray=sorted(oddarray)
print("the sorted oddarray are:",oddarray[0:len(oddarray]))
print("the sum of second highest number is:",evenarray[-2]+oddarray[-2]
