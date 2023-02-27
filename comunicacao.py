import ephem
import math

# Define a localização do observador
observer = ephem.Observer()
observer.lat = '- 5.836126' # Latitude da antena do INPE - Natal
observer.lon = '-35.207609' # Longitude da antena do INPE - Natal
observer.elevation = '56'   # Altitude da antena do INPE - Natal (METROS)

# Define as coordenadas do satélite em função do tempo
satellite_lat = '' # Ler a partir do arquivo gerado na simulação
satellite_lon = '' # Ler a partir do arquivo gerado na simulação

# Cria um objeto "PyEphem" para o satélite
satellite = ephem.FixedBody()
satellite._ra = ephem.degrees(satellite_lon)
satellite._dec = ephem.degrees(satellite_lat)

# Calcula a posição do satélite em relação ao observador
satellite.compute(observer)

# Calcula a elevação do satélite em relação ao horizonte do observador
elevation = math.degrees(satellite.alt)

# Exibe a elevação calculada
print("A elevação do satélite é:", elevation, "graus")
