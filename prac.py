def fibSeq(n):
    l = [0,1]
    for i in range(2,n+2):
        e = l[i-1]+l[i-2]
        l.append(e)
    return l
print(fibSeq(10))