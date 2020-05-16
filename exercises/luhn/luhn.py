string=input()
list1=string.split(" ")
list2=[]
sum=0
for i in range(len(list1)):
	num=list1[i]
	for j in num:
		list2.append(j)
for i in range(len(list2)):
	if(i%2==0):
		val=int(list2[i])+int(list2[i])
		if(val>9):
			val=val-9
		list2[i]=str(val)
print(list2)
for i in list2:
	sum=sum+int(i)
print(sum)
