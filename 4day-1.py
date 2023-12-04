file1 = open('a.txt', 'r')
Lines = file1.readlines()
t=0
tl=0
for line in Lines:
    line=line.strip()
    m,e=line.split(": ")
    #print(e)
    a,b=e.split(" | ")
    c1 = list(filter(None, a.split(" ")))
    c2 = list(filter(None, b.split(" ")))
    #print(c1, c2)
    tw=0
    for i in c2:
    	if i in c1:
    		tw=tw+1
    if tw==0:
    	t=t+0
    if tw==1: 
    	t=t+1
    if tw>=2:
    	t=t+int(2**(tw-1))
    tl=tl+1
    
print(t)
print(tl)
    
