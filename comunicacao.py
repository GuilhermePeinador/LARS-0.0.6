import numpy as np

'''
Coordenadas Antena INPE Natal
Latitude: -5.871778
Longitude: -35.206864
'''



for i in range (len(r)):
    VetorTerraEstacao = [ -5.871778 , 6371 , -35.206864 ]
    VetorSatelite = [rx[i] , ry[i] , rz[i]]

    VetorSateliteEstacao = VetorSatelite - VetorTerraEstacao

    #Critério de Comunicação
    AComunicacao = np.pi \
            - np.arccos((np.dot(VetorSatelite,VetorSateliteEstacao))/np.linalg.norm(VetorSatelite)*np.linalg.norm(VetorSateliteEstacao)) \
            - np.arccos((np.dot(VetorTerraEstacao,VetorSatelite))/np.linalg.norm(VetorTerraEstacao)*np.linalg.norm(VetorSatelite))


    if AComunicacao >= 105: #90 graus (horizonte) + 15 (elevação)
        print("1") #Tem comunicação
    else:
        print("0") # não tem comunicação