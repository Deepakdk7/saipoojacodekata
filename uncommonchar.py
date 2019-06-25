ax=input()
bx=input()
a=[]
if (ax.isalpha() or " " in ax) and (bx.isalpha() or " " in bx):
    ax=list(ax.split())
    bx=list(bx.split())
    for i in ax:
        if ax.count(i) > bx.count(i) and i not in a:
            a.append(i)
    for i in bx:
        if bx.count(i)>ax.count(i) and i not in a:
            a.append(i)
    print(*a)
else:
    for i in ax:
        if ax.count(i)>bx.count(i) and i not in a:
            a.append(i)
    for j in bx:
        if bx.count(j)>ax.count(j) and j not in a:
            a.append(j)
    print(*a)
