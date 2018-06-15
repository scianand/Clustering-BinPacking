import numpy as np
import matplotlib.pyplot as plt

#filepath = 'C:/BinPackingAlgos/src/Dataset/binpack1_output_harm.txt'
filepath = 'C:/Ashish/Clustering-Bin-Packing/src/main/output/binpack1_output.txt'
#filepath = 'C:/BinPackingAlgos/src/Dataset/binpack1_output.txt'
data = []

with open(filepath, "r+") as fp:  
   line = fp.readline()
   while line:
       data_temp = (line.strip().split('\t'))
       data.append(list(map(int, data_temp)))
       line = fp.readline()

fp.close()
#print(data)
randomDists = ['Harmonic', 'NextFit', 'BestFit', 'FirstFit']
#randomDists = ['FirstFit', 'NextFit', 'BestFit', 'FirstFitD', 'NextFitD', 'BestFitD']
fig, ax1 = plt.subplots(figsize=(7, 5))
fig.canvas.set_window_title('A Boxplot Example')
#plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax1.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
plt.boxplot(data)

ax1.set_title('Comparison of Online and Harmonic Bin Packing Algorithms')
#ax1.set_title('Comparison of Online and Offline Bin Packing Algorithms')
ax1.set_xlabel('Algorithms')
ax1.set_ylabel('Performance')
xtickNames = plt.setp(ax1, xticklabels=np.repeat(randomDists, 1))
plt.setp(xtickNames, rotation=45, fontsize=8)
fig.savefig('C:/Ashish/Clustering-Bin-Packing/src/main/output/online_harmonic.png', bbox_inches='tight')
#fig.savefig('online_offline.png', bbox_inches='tight')

plt.show()
