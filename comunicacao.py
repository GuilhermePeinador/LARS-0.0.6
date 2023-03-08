import ephem
import math
import pandas as pd
import teste

# Define a localização do observador
observer = ephem.Observer()
observer.lat = '- 5.836126' # Latitude da antena do INPE - Natal
observer.lon = '-35.207609' # Longitude da antena do INPE - Natal
observer.elevation = '56'   # Altitude da antena do INPE - Natal (METROS)

df = pd.read_csv(teste.resource_path("data/dados_ECI.csv"), sep='=', engine='python', on_bad_lines='skip')  #********* n calcula lat e long?

latitude = df['7']
longitude = df['8']

for i in range( 0 , len(latitude) , 1 ): # inicio, fim, passo

    # Define as coordenadas do satélite em função do tempo
    #renan
    #satellite_lat = '' # Ler a partir do arquivo gerado na simulação
    #satellite_lon = '' # Ler a partir do arquivo gerado na simulação

    # Cria um objeto "PyEphem" para o satélite
    satellite = ephem.FixedBody()
    satellite._ra = ephem.degrees(longitude[i])
    satellite._dec = ephem.degrees(latitude[i])

    # Calcula a posição do satélite em relação ao observador
    satellite.compute(observer)

    elevation = []

    # Calcula a elevação do satélite em relação ao horizonte do observador
    elevation = math.degrees(satellite.alt)

# Exibe a elevação calculada
print("A elevação do satélite é:", elevation, "graus")



elevationTF = []

for i in elevation:
    if elevation[i]>=15:
        elevationTF.append(True)
    else:
        elevationTF.append(False)

elevationTF.count(True)






