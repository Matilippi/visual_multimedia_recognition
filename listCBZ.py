import zipfile

def taglia_primi_n_caratteri(stringa, n):
    # Restituisce la stringa senza i primi n caratteri
    return stringa[n:]


def lista_file_cbz(percorso_file_cbz):
    try:
        with zipfile.ZipFile(percorso_file_cbz, 'r') as archivio_cbz:
            lista_file = archivio_cbz.namelist()
            lengths = []
            
            for nome_file in lista_file:
                print(nome_file)
                if nome_file.endswith('.jpg'):
                    name = nome_file[:-4]  # Rimuove ".jpg" dal nome del file
                    lengths.append(len(name))
            min_length = min(lengths)
            max_length = max(lengths)
            suffissi = []
            print("-------------------")
            for nome_file in lista_file:
               if len(nome_file)>min_length:
                nome_file=nome_file[:-4]
                suffisso = taglia_primi_n_caratteri(nome_file,min_length)
                if suffisso!="":
                    suffissi.append(suffisso)
            for s in suffissi:
                print(s + " [nome book]")


                



                


    except zipfile.BadZipFile:
        print("Il file specificato non è un archivio zip valido.")

# Sostituisci 'percorso_del_tuo_file.cbz' con il percorso effettivo del tuo file .cbz
percorso_file_cbz = "C:/Users/Pc/Desktop/UNIFI MAGISTRALE/VISUAL AND MULTIMEDIA RECOGNITION/PROGETTO ASSEGNATO/cbz files/BlackCatMystery42_ctc_JVJ_Geo_ffly.cbz"
lista_file_cbz(percorso_file_cbz)