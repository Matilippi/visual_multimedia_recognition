import zipfile
import os
from collections import defaultdict

def taglia_primi_n_caratteri(stringa, n):
    # Restituisce la stringa senza i primi n caratteri
    return stringa[n:]


def lista_file_cbz(percorso_file_cbz):
    suffissi = []
    dizionario = {}
   
    for filename in os.listdir(percorso_file_cbz):
        # Creare il percorso completo del file
            filepath = os.path.join(percorso_file_cbz, filename)
            if filepath.endswith(".cbz"):
                with zipfile.ZipFile(filepath, 'r') as archivio_cbz:
                    lista_file = archivio_cbz.namelist()
                    lengths = []
                    nomeCBZ = os.path.basename(filepath)
                    for nome_file in lista_file:
                        print(nome_file)
                        if nome_file.endswith('.jpg'):
                            name = nome_file[:-4]  # Rimuove ".jpg" dal nome del file
                            lengths.append(len(name))
                    min_length = min(lengths)
                    max_length = max(lengths)
                    print("-------------------")
                    for nome_file in lista_file:
                        if len(nome_file)>min_length:
                            nome_file=nome_file[:-4]
                            suffisso = taglia_primi_n_caratteri(nome_file,min_length)
                            #elimina gli underscore e i trattini
                            suffisso = suffisso.replace("_", "")
                            suffisso = suffisso.replace("-", "")    
                            if suffisso!="":
                                suffissi.append(suffisso)
                            suffissi=list(set(suffissi))
                            for s in suffissi:                 
                                if s in dizionario:
                                # Controllare se la stringa è già nella lista associata alla chiave
                                    if nomeCBZ not in dizionario[s]:
                                        dizionario[s].append(nomeCBZ)
                                else:
                                    # Inizializzare una nuova lista con la stringa
                                    dizionario[s] = [nomeCBZ]    
    print(dizionario)
    with open("dictionary.txt", "w") as file:
        for chiave, lista in dizionario.items():
            # Unire gli elementi della lista con una virgola
            valori = ", ".join(lista)
            # Scrivere la chiave e i valori nel file
            file.write(f"{chiave}: {valori}\n")
    


percorso_file_cbz = "C:/Users/Pc/Desktop/UNIFI MAGISTRALE/VISUAL AND MULTIMEDIA RECOGNITION/PROGETTO ASSEGNATO/cbz files"
lista_file_cbz(percorso_file_cbz)