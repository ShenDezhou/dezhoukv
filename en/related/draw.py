
import numpy as np
import matplotlib.pyplot as plt


x1 =  np.arange(11) * 10

y1 = [135000,17000,8500.0,5666.7,4250.0,3400.0,2833.3,2428.5,2125.0,1888.8,1720.0]

plt.subplot(1, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title(u"Theoretical IOPS value with space usage")

plt.xlabel(u"Space usage%")
plt.ylabel('IOPS')

plt.show()