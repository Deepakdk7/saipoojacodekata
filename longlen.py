astr=input()
l=list(astr.split(" "))
m=1
for i in l:
	c=len(i)
	if c>m:
		m=len(i)
		a=i
print(a)