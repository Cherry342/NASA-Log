file= open("NASA_access_log_Jul95")

from _collections_abc import defaultdict
from collections import Counter
items=file(list)
ip_adresses = []
try:
    for line in file:
        print(file)

    
    
    ip_adresses.append(line.split(" ")[0])
    
    print(line.split(" ")[0])
   # from _collections_abc:
    #print(file(list))


except:
    print("uh-oh")
    pass
import matplotlib.pyplot as plt
count = Counter(ip_adresses)
print(ip_adresses)
print(ip_adresses.keys())
print(ip_adresses.values())

plt.bar(ip_adresses.keys(),ip_adresses.values())
plt.show()
