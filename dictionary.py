from collections import Counter
import matplotlib.pyplot as plt
berries= [
    'strawberry',
    'blueberry', 'blueberry',
    'blackberry','blackberry','blackberry',
    'raspberry', 'raspberry', 'raspberry' , 'raspberry'
]

berry_counter=Counter(berries)
print(berry_counter)
{'raspberry': 4, 'blackberry':3, 'blueberry':2, 'strawberry': 1,}

print(berry_counter.keys())
print(berry_counter.values())



plt.bar(berry_counter.keys(), berry_counter.values())
plt.show()
names= {1: 'strawberry', 2: 'blueberry', 3: 'blackberry', 4: 'raspberry'}
print(dict(filter))
