try:
	num=int(input())
	for i in range(1,num+1):
		if(num%i==0):
			print(i,end=" ")
		else:
			continue
except ValueError:
	print("invalid")