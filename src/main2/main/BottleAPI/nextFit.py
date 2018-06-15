def nextFit(weight, n, c):
	res = 1
	bin_rem = c
	for i in range(0, n):
		if (weight[i] > bin_rem):
			res = res + 1
			bin_rem = c - weight[i]
		else:
			bin_rem = bin_rem - weight[i]
	return res