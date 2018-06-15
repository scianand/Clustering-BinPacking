from __future__ import division
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import numpy as np
import pandas as pd
import datetime
import operator
from sklearn.cluster import KMeans, MiniBatchKMeans
import sys

def checkClass(k, a):
	for i in range(k, 1, -1):
		if (a > (1.0/i) and a <= (1.0/(i-1))):
			clas = (i-1)
			break
		else:
			clas = k
	return (clas-1)

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

def k_means(X, n):
	mbk = MiniBatchKMeans(n_clusters=n, batch_size=10000)
	mbk = mbk.fit(X)
	labels = mbk.predict(X)
	C = mbk.cluster_centers_
	return C, mbk

def mainjson(dictionary):

	df = pd.DataFrame(dictionary)
	X = np.array(list(zip(df['collection_longitude'], df['collection_latitude'])))

	centr, mb = k_means(X, 21)
	d = {i: X[np.where(mb.labels_ == i)] for i in range(mb.n_clusters)} # Cluster points' value
	d1 = {i: np.where(mb.labels_ == i)[0] for i in range(mb.n_clusters)} # Cluster points' index
	k = list(d.keys())
	v = list(d.values())
	vids = list(d1.values())

	date_time = []
	for i in range(0, len(vids)):
		date_time1 = {}
		for j in range(0, len(vids[i])):
			date_time1.update({vids[i][j]: df['collection_date'].iloc[vids[i][j]]})
		date_time.append(date_time1)

	date_time_sorted = []
	for diction in date_time:
		sorted_x = sorted(diction.items(), key=operator.itemgetter(1))
		date_time_sorted.append(sorted_x)

	l = []
	for i in date_time_sorted:
		d = {}
		for j in i:
			key = j[1]
			d.setdefault(key, []).append(j[0]) # Append the new time into new list
		l.append(d)

	li = []
	for i in l:
		sorted_i = sorted(i.items(), key=operator.itemgetter(0))
		li.append(sorted_i)

	d = []
	for i in li:
		d1 = []
		for j in i:
			temp = j[1]
			d2 = []
			for k in j[1]:
				d2.append(df['size'].iloc[k])
			d1.append(d2)
		d.append(d1)

	bins = 0
	for i in d:
		for j in i:
			bins += harmonic(j, 1, 4)
	return bins
	# return dictionary
    # return bins

def fun(data):
	res = len(data)
	return res

@app.route("/", methods=['POST', 'OPTIONS'])
def index():
	if request.method == 'POST':
		content = request.get_json()
		app.logger.info(content)
		print(content)
		print("TEST")
		# return content
		result = fun('a')
		# return jsonify(result)
		return result
	else:
		return 'ok'

if __name__ == '__main__':
	app.run(debug = True)