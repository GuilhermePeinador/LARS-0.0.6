import numpy as np

VetorTerraEstacao =
PEstacao =
VetorEstacao =
VetorSatelite =
VetorSateliteEstacao = VetorSatelite - VetorEstacao


#Critério de Comunicação
gamma = np.pi \
        - np.arccos((np.dot(VetorSatelite,VetorSateliteEstacao))/np.linalg.norm(VetorSatelite)*np.linalg.norm(VetorSateliteEstacao)) \
        - np.arccos((np.dot(VetorEstacao,VetorSatelite))/np.linalg.norm(VetorEstacao)*np.linalg.norm(VetorSatelite))


if gamma >= 105: #90 graus (horizonte) + 15 (elevação)
    print("1")
else:
    print("0")