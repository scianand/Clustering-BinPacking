def checkClass(k, a):
	for i in range(k, 1, -1):
		if (a > (1.0/i) and a <= (1.0/(i-1))):
			clas = (i-1)
			break
		else:
			clas = k
	return (clas-1)