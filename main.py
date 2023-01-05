file= open("NASA_access_log_Jul95")


#from _collections_abc import defaultdict
from collections import Counter
ip_adresses = []
try:
    for line in file:
       ip_adresses.append(line.split(" ")[0])


except:
  print("uh-oh")

import matplotlib.pyplot as plt

count = Counter(ip_adresses)
bar_labels = ['pink', 'blue', 'orange', 'purple']
bar_colors = ['tab:pink', 'tab:blue', 'tab:orange', 'tab:purple']
filtered_count = {k:v for (k,v) in count.items() if v>550}
plt.set_xlabel('Berries')
plt.bar(filtered_count.keys(), filtered_count.values(), color=bar_colors, )
plt.show()

# print({k:v for (k,v) in names.items if k%2==()})
