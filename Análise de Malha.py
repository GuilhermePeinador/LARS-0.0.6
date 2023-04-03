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

b = [[10   , 30 , 0   , 15.867372940646838 , 165.7204225372201 ],
     [10   , 30 , 90  , 15.867401739303064 , -77.65935926415366],
     [10   , 30 , 180 , 15.867333737253764 ,  38.96065046164395],
     [10   , 30 , 270 , 15.86736478469942  , 155.58087350000582],
     [0.01 , 30 , ],
     [0.01 , 30 ,],
     [0.01 , 30 , ],
     [0.01 , 30 , ],
     [10   , 98 , 0   , 23.428750145544534 , 132.72082788676713 ],
     [10   , 98 , 90  , 23.428838862759523 , -110.65903078206155],
     [10   , 98 , 180 , 23.428848384176614 , 5.961123801947356  ],
     [10   , 98 , 270 , 23.428759268791357 , 122.5812948921998  ],
     [0.01 , 98 , 0   ,],
     [0.01 , 98 , 90  ,],
     [0.01 , 98 , 180 , 24.405971771831016 , 5.7755789144641225],
     [0.01 , 98 , 270 , 24.405882218935243 , 122.39575034159724 ]]

print(tabulate(b, headers=["deltT", "Inclinação", "RAAN", "Latitude", "Longitude"]))
#I=52 , Número de elementos , Latitude e Longitude
npontos = [558 , 1116 , 5580 , 11161 , 13951 , 18601 , 27902 , 55805 , 558051 , 5580518 ]
Latitude  = [17.5362878838941   , 20.011385523167636 , 21.970597312613457 , 22.45708797308703  , 22.457104219700742 , 22.457116814130597 , 22.554257588665383 , 22.651339604518128 , 22.69986840259014 , 22.708111751615995 ]
Longitude = [150.50935691910428 , 152.74918095945375 , 154.59186019872035 , 155.04018572949124 , 155.04421210503222 , 155.04823489819478 , 155.13829879434243 , 155.22849194320466 , 155.27525116694127 , 155.2829458130034 ]

#I = 30 vetor de latitudes e longitudes com deltT = 10, RAAN > 0,90,180,270
Latitudes30  = [15.867372940646838 , 15.867401739303064 , 15.867333737253764 , 15.86736478469942]
Longitudes30 = [165.7204225372201  , -77.65935926415366 , 38.96065046164395  , 155.58087350000582]

#I = 30 vetor de latitudes e longitudes com deltT = 0.01, RAAN > 0,90,180,270
Latitudesref30  = [ ,  ,  , ]
Longitudesref30 = [  ,  ,   , ]

#I = 98 vetor de latitudes e longitudes com deltT = 10, RAAN > 0,90,180,270
Latitudes98  = [23.428750145544534 , 23.428838862759523 , 23.428848384176614 , 23.428759268791357]
Longitudes98 = [132.72082788676713 , -110.65903078206155 , 5.961123801947356 , 122.5812948921998]

#I = 98 vetor de latitudes e longitudes com deltT = 0.01, RAAN > 0,90,180,270
Latitudesref98  = [ ,  , 24.405971771831016 , 24.405882218935243]
Longitudesref98 = [ ,  , 5.7755789144641225 , 122.39575034159724]


#Erro de Latitude
Verro = []

for i in range(len(Latitude)):
      erro = round((abs(Latitude[i]-Latitude[-1])/Latitude[-1]) * 100 , 2)
      Verro.append(erro)
print(Verro)

#Erro de Longitude
V2erro = []

for i in range(len(Longitude)):
      erro1 = round((abs(Longitude[i]-Longitude[-1])/Longitude[-1]) * 100 , 2)
      V2erro.append(erro1)
print(V2erro)

#------------------------------------------------------------------------------------------------
#Erro latitude I=30 / RAAN=0
erro1 = round((abs(Latitudes30[0]-Latitudesref30[0])/Latitudesref30[0]) *100 , 2)
print("(I = 30 e RAAN = 0) Erro entre Latitudes:", erro1)
#Erro latitude I=30 / RAAN=90
erro2 = round((abs(Latitudes30[1]-Latitudesref30[1])/Latitudesref30[1]) *100 , 2)
print("(I = 30 e RAAN = 90) Erro entre Latitudes:", erro2)
#Erro latitude I=30 / RAAN=180
erro3 = round((abs(Latitudes30[2]-Latitudesref30[2])/Latitudesref30[2]) *100 , 2)
print("(I = 30 e RAAN = 180) Erro entre Latitudes:", erro3)
#Erro latitude I=30 / RAAN=270
erro4 = round((abs(Latitudes30[3]-Latitudesref30[3])/Latitudesref30[3]) *100 , 2)
print("(I = 30 e RAAN = 270) Erro entre Latitudes:", erro4)
#--------------------------------------------------------------------------------------------------
#Erro latitude I=98 / RAAN=0
erro5 = round((abs(Latitudes98[0]-Latitudesref98[0])/Latitudesref98[0]) *100 , 2)
print("(I = 98 e RAAN = 0) Erro entre Latitudes:", erro5)
#Erro latitude I=98 / RAAN=90
erro6 = round((abs(Latitudes98[1]-Latitudesref98[1])/Latitudesref98[1]) *100 , 2)
print("(I = 98 e RAAN = 90) Erro entre Latitudes:", erro6)
#Erro latitude I=98 / RAAN=180
erro7 = round((abs(Latitudes98[2]-Latitudesref98[2])/Latitudesref98[2]) *100 , 2)
print("(I = 98 e RAAN = 180) Erro entre Latitudes:", erro7)
#Erro latitude I=98 / RAAN=270
erro8 = round((abs(Latitudes98[3]-Latitudesref98[3])/Latitudesref98[3]) *100 , 2)
print("(I = 98 e RAAN = 270) Erro entre Latitudes:", erro8)
#--------------------------------------------------------------------------------------------------
#Erro longitude I=30 / RAAN=0
erro8 = round((abs(Longitudes30[0]-Longitudesref30[0])/Longitudesref30[0]) *100 , 2)
print("(I = 30 e RAAN = 0) Erro entre Longitudes:", erro8)
#Erro longitude I=30 / RAAN=90
erro9 = round((abs(Longitudes30[1]-Longitudesref30[1])/Longitudesref30[1]) *100 , 2)
print("(I = 30 e RAAN = 90) Erro entre Longitudes:", erro9)
#Erro longitude I=30 / RAAN=180
erro10 = round((abs(Longitudes30[2]-Longitudesref30[2])/Longitudesref30[2]) *100 , 2)
print("(I = 30 e RAAN = 180) Erro entre Longitudes:", erro10)
#Erro longitude I=30 / RAAN=270
erro11 = round((abs(Longitudes30[3]-Longitudesref30[3])/Longitudesref30[3]) *100 , 2)
print("(I = 30 e RAAN = 270) Erro entre Longitudes:", erro11)
#---------------------------------------------------------------------------------------------------
#Erro longitude I=98 / RAAN=0
erro12 = round((abs(Longitudes98[0]-Longitudesref98[0])/Longitudesref98[0]) *100 , 2)
print("(I = 98 e RAAN = 0) Erro entre Longitudes:", erro12)
#Erro longitude I=98 / RAAN=90
erro13 = round((abs(Longitudes98[1]-Longitudesref98[1])/Longitudesref98[1]) *100 , 2)
print("(I = 98 e RAAN = 90) Erro entre Longitudes:", erro13)
#Erro longitude I=98 / RAAN=180
erro14 = round((abs(Longitudes98[2]-Longitudesref98[2])/Longitudesref98[2]) *100 , 2)
print("(I = 98 e RAAN = 180) Erro entre Longitudes:", erro14)
#Erro longitude I=98 / RAAN=270
erro15 = round((abs(Longitudes98[3]-Longitudesref98[3])/Longitudesref98[3]) *100 , 2)
print("(I = 98 e RAAN = 270) Erro entre Longitudes:", erro15)
#----------------------------------------------------------------------------------------------------

fig, ax = plt.subplots()


plt.scatter(npontos, Latitude, color='red')
plt.xlim(550,5600000)
plt.xscale('log')
plt.ylim(16,24)
plt.axhline(22.7081, linestyle = 'dashed') # assíntota horizontal
#plt.show()

plt.scatter(npontos, Longitude, color='blue')
plt.xlim(550,5600000)
plt.ylim(150,156)
plt.axhline(155.283, linestyle = 'dashed')
plt.xscale('log')
#plt.show()

