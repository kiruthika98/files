def p(n11,n22):
	while(n22!=0):
		t=n22
		n22=n11%n22
		n11=t
	return n11
def main():
	m=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(m):
		l.append(int(input()))
	print(l)
	for c in range(q):
		n11=int(input())
		n22=int(input())
		r.append(p(l[n11-11],l[n22-11]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
