
#import matplotlib.pyplot as plt
#import numpy as np
#import matplotlib as mpl

#xpoints = list(range(0,10)) 
#ypoints= list(range(-10,0))
#plt.plot (xpoints,ypoints)
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt

#x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
#y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#plt.plot(x, y)
#plt.grid()
#plt.show()
#plt.title("Triangle")

#import numpy as np
#import matplotlib.pyplot as plt

#x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
#y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#plt.plot(x, y)

#plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

#plt.show()
import matplotlib.pyplot as plt

categories= ['goldencheese', 'whitelily', 'purevanilla', 'darkcacao', 'hollyberry']
numbers= [54, 77, 96, 101, 85]
plt.bar(categories, numbers, color=['orange', 'green', 'blue', 'purple', 'pink'])

plt.bar(categories, numbers, color=['orange', 'lime', 'aqua', 'blueviolet', 'deeppink'])


plt.show()