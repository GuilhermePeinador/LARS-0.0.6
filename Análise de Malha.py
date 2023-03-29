from tabulate import tabulate
import matplotlib.pyplot as plt

a = [ [100  , 558 , 17.5362878838941 , 150.50935691910428 , 1.6682021617889404],
      [50   , 1116 , 20.011385523167636 , 152.74918095945375 , 1.6882400512695312],
      [10   , 5580 , 21.970597312613457 , 154.59186019872035 , 4.371733903884888] ,
      [5    , 11161 , 22.45708797308703 , 155.04018572949124 , 8.236107110977173],
      [4    , 13951 , 22.457104219700742 , 155.04421210503222 , 9.498253345489502],
      [3    , 18601 , 22.457116814130597  , 155.04823489819478 , 10.76041316986084],
      [2    , 27902 , 22.554257588665383 , 155.13829879434243 , 19.439849376678467],
      [1    , 55805 , 22.651339604518128 , 155.22849194320466 , 31.395272254943848],
      [0.1  , 558051 , 22.69986840259014 , 155.27525116694127 , 273.8160591125488],
      [0.01 , 5580518 , 22.708111751615995 , 155.2829458130034 , 2414.4545657634735]]

print(tabulate(a, headers=["delT", "Número de elementos", "Latitude", "Longitude", "Tempo"]))

npontos = [558 , 1116 , 5580 , 11161 , 13951 , 18601 , 27902 , 55805 , 558051 , 5580518 ]
Latitude  = [17.5362878838941   , 20.011385523167636 , 21.970597312613457 , 22.45708797308703  , 22.457104219700742 , 22.457116814130597 , 22.554257588665383 , 22.651339604518128 , 22.69986840259014 , 22.708111751615995 ]
Longitude = [150.50935691910428 , 152.74918095945375 , 154.59186019872035 , 155.04018572949124 , 155.04421210503222 , 155.04823489819478 , 155.13829879434243 , 155.22849194320466 , 155.27525116694127 , 155.2829458130034 ]

#Erro de Latitude
Verro = []

for i in range(len(Latitude)):
      erro = round(abs(Latitude[i]-Latitude[-1])/Latitude[-1] * 100 , 2)
      Verro.append(erro)
print(Verro)

#Erro de Longitude
V2erro = []

for i in range(len(Longitude)):
      erro = round(abs(Longitude[i]-Longitude[-1])/Longitude[-1] * 100 , 2)
      V2erro.append(erro)
print(V2erro)

fig, ax = plt.subplots()


plt.scatter(npontos, Latitude, color='red')
plt.xlim(550,5600000)
plt.xscale('log')
plt.ylim(16,24)
plt.axhline(22.7081, linestyle = 'dashed') # assíntota horizontal
plt.show()

plt.scatter(npontos, Longitude, color='blue')
plt.xlim(550,5600000)
plt.ylim(150,156)
plt.axhline(155.283, linestyle = 'dashed')
plt.xscale('log')
plt.show()

