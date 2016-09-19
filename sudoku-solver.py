with open("sudoku.txt","r") as sudoku:
	s=""
	d=sudoku.read()
	print d 
	for char in d:
		s+=char
l1=s.split("\n")
l2=[]
for item in l1: l2.append(item.split())
ly=[]
cx=0
for x in l2:
	cy=0
	for y in x:
		try: x[cy]=int(y)
		except: 
			ly.append(cx)
			ly.append(cy)
		cy+=1
	cx+=1
r=range(len(ly)/2)
r=r[::-1]
print ly

c=0
for x in ly[-2::-2]:
	print x,ly[-c*2],c*2
	del l2[x][ly[-1-c*2]]
	c+=1
	
for item in l2:
	if len(item)==0: l2.remove(item)

print l2