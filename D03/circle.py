import sys
import numpy as np

radius = int(sys.argv[1])
area = round(np.pi*int(radius)**2,2)
print(f'The area of the circle is: {area}')




