from checkClass import checkClass
from nextFit import nextFit
def harmonic(items_normal, cap, k):
	items = [i/cap for i in items_normal]
	bins_k = [] #items divided n classes, list of list
	res_k = [] #bins required in every class
	for i in range(0, k):
		classes = [] #single list
		bins_k.append(classes)
	for item in items:
		clas = checkClass(k, item)
		bins_k[clas].append(item)
	for classes in bins_k:
		if (len(classes) != 0):
			bins = nextFit(classes, len(classes), 1)
		else:
			bins = 0
		res_k.append(bins)
		#print(classes)
	res = 0
	#print(bins_k)
	for i in bins_k:
		pass
		#print(len(i))
	for r in res_k:
		res = res + r
	#print(res_k)
	return res