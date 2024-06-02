#!/bin/bash

# Verifica che siano passati 5 argomenti
if [ "$#" -ne 5 ]; then
    echo "Uso: $0 <utente_remoto> <host_remoto> <directory_remota> <directory_locale> <numero_di_cartelle>"
    exit 1
fi

utente_remoto=$1
host_remoto=$2
directory_remota=$3
directory_locale=$4
numero=$5

# Crea la directory locale se non esiste
mkdir -p "$directory_locale"

# Ottieni la lista delle prime N cartelle dal server remoto
cartelle=$(ssh "$utente_remoto@$host_remoto" "ls -d $directory_remota/*/ | head -n $numero")

# Copia ciascuna cartella in locale
for cartella in $cartelle; do
    scp -r "$utente_remoto@$host_remoto:$cartella" "$directory_locale"
done

echo "Copiate le prime $numero cartelle da $utente_remoto@$host_remoto:$directory_remota a $directory_locale."
