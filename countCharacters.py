import os
import shutil

def conta_caratteri_cartella(cartella):
    # Ottieni tutti i file nella cartella specificata
    files = os.listdir(cartella)
    lunghezze = set()
    lunghezze_nomi = {}

    for file in files:
        # Ignora le cartelle
        if os.path.isfile(os.path.join(cartella, file)):
            # Ottieni la parte del nome del file prima del punto
            nome_prima_del_punto = file.split('.')[0]
            lunghezza = len(nome_prima_del_punto)
            # Aggiungi la lunghezza del nome al set delle lunghezze
            lunghezze.add(lunghezza)
            lunghezze_nomi[file] = lunghezza

    # Stampa i file e le loro lunghezze
    for file, lunghezza in lunghezze_nomi.items():
        print(f"{file}: {lunghezza} caratteri prima del punto")

    # Se c'è più di una lunghezza diversa, rispondi "si", altrimenti "no"
    if len(lunghezze) > 1:

        try:
            # Copia la cartella
            shutil.copytree('/home/andrea/PycharmProjects/provaContaCaratteri/8', '/home/andrea/PycharmProjects/provaContaCaratteri/foldersOK/8', dirs_exist_ok=True)
            print(f"Cartella copiata con successo")
        except Exception as e:
            print(f"Errore durante la copia: {e}")
        return "si"

    else:
        return "no"

# Specifica il percorso della cartella
cartella = '/home/andrea/PycharmProjects/provaContaCaratteri/8'

# Chiama la funzione e stampa il risultato
risultato = conta_caratteri_cartella(cartella)
print(risultato)



