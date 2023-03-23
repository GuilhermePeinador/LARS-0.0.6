import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

a = [ [100 , 558 , 17.5362878838941 , 150.50935691910428 , 1.6682021617889404],
      [50  , 1116 , 20.011385523167636 , 152.74918095945375 , 2.1955997943878174],
      [10  , 5580 , 21.970597312613457 , 154.59186019872035 , 6.821180105209351] ,
      [5   , 11161 , 22.45708797308703 , 155.04018572949124 , 13.659641742706299],
      [3   , 18601 , 22.457116814130597  , 155.04823489819478 , 32.72131705284119],
      [1   , 55805 , 22.651339604518128 , 155.22849194320466 , 115.6702675819397],
      [0.1 , 55051 , 22.69986840259014 , 155.27525116694127 , 983.3409202098846]]

print(tabulate(a, headers=["delT", "Número de elementos", "Latitude", "Longitude", "Tempo"]))

#todo refazer cálculo para delT = 0.1

npontos = [558 , 1116 , 5580 , 11161 , 18601 , 55805 ]
Latitude = [17.5362878838941 , 20.011385523167636 , 21.970597312613457 , 22.45708797308703 , 22.457116814130597 , 22.651339604518128]
Longitude = [150.50935691910428 , 152.74918095945375 , 154.59186019872035 , 155.04018572949124 , 155.04823489819478 , 155.22849194320466]



fig, ax = plt.subplots()


plt.scatter(npontos, Latitude, color='red')
plt.xlim(550,56000)
plt.xscale('log')
plt.ylim(16,24)
plt.axhline(22.75, linestyle = 'dashed') # assíntota horizontal

#z=np.polyfit(npontos, Latitude, 1)
#p = np.poly1d(z)
#plt.plot(npontos,p(npontos),"r--")

plt.show()

plt.scatter(npontos, Longitude, color='blue')
plt.xlim(550,56000)
plt.ylim(150,156)
plt.axhline(155.35, linestyle = 'dashed')
plt.xscale('log')
plt.show()

