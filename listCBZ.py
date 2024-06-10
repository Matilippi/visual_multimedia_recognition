import zipfile
import os
from collections import defaultdict

def taglia_primi_n_caratteri(stringa, n):
    # Restituisce la stringa senza i primi n caratteri
    return stringa[n:]


def lista_file_cbz(percorso_file_cbz):
    suffissi = []
    dizionario = {}
    n = 0
    for filename in os.listdir(percorso_file_cbz):
            print(filename)
            # Creare il percorso completo del file
            filepath = os.path.join(percorso_file_cbz, filename)
            if filepath.endswith(".cbz"):
                try:
                    with zipfile.ZipFile(filepath, 'r') as archivio_cbz:
                        lista_file = archivio_cbz.namelist()
                        lengths = []
                        for nome_file in lista_file:
                            #print(nome_file)
                            if nome_file.endswith('.jpg'):
                                name = nome_file[:-4]  # Rimuove ".jpg" dal nome del file
                                lengths.append(len(name))
                        min_length = min(lengths)
                        for nome_file in lista_file:
                            if len(nome_file)>min_length and '/' not in nome_file:
                               
                                nome_file=nome_file[:-4]
                                suffisso = taglia_primi_n_caratteri(nome_file,min_length)
                                #elimina i caratteri inutili
                                suffisso = suffisso.replace("_", "")
                                suffisso = suffisso.replace("-", "")
                                suffisso = suffisso.replace("(", "")
                                suffisso = suffisso.replace(")", "")     
                                suffisso = suffisso.replace(" ", "")   
                                if suffisso!="" or suffisso != 0:
                                    suffissi.append(suffisso)
                                suffissi=list(set(suffissi))
                                if suffisso in dizionario:
                                    # Controllare se la stringa è già nella lista associata alla chiave
                                    if filename not in dizionario[suffisso]:
                                        dizionario[suffisso].append(filename)
                                else:
                                    # Inizializzare una nuova lista con la stringa
                                    dizionario[suffisso] = [filename]  
                except zipfile.BadZipFile:
                    print(f"Errore: {filename} non è un file CBZ valido.")
                    n=n+1
                except Exception as e:
                    print(f"Si è verificato un errore: {e}")  

    with open("dictionary.txt", "w") as file:
        for chiave, lista in dizionario.items():
            # Unire gli elementi della lista con una virgola
            valori = ", ".join(lista)
            print(chiave,len(lista))
            # Scrivere la chiave e i valori nel file
            file.write(f"{chiave}: {len(lista)} : {valori}\n")
    print("FILE CBZ ERRATI ",n)
percorso_file_cbz = "../../../../dune/DATASETS/PSS_DCM/dcm_22k/cbz"
lista_file_cbz(percorso_file_cbz)