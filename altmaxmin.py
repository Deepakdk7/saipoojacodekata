try:
	num=int(input())
	arr=[int(x) for x in input().split()]
	a=[]
	b=sorted(arr)
	while len(b)!=0:
		if len(b)!=1:
			a.append(b[-1])
			a.append(b[0])
			b.remove(b[0])
			b.remove(b[-1])
		else:
			a.append(b[0])
			b.remove(b[0])
	print(*a)	
except ValueError:
	print("invalid")