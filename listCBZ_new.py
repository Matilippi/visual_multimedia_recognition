import os
import zipfile
from collections import defaultdict

def get_variable_parts(file_names):
    variable_parts = defaultdict(list)
    common_prefix = os.path.commonprefix(file_names)
    for file_name in file_names:
        variable_part = file_name[len(common_prefix):-4]  # Rimuove il prefisso comune e ".jpg"
        if variable_part:  # Evita stringhe vuote
            variable_parts[variable_part].append(file_name)
    return variable_parts

def process_cbz_file(cbz_path):
    try:
        with zipfile.ZipFile(cbz_path, 'r') as zip_ref:
            jpg_files = [f for f in zip_ref.namelist() if f.endswith('.jpg')]
            if len(jpg_files) < 5:
                return None
            variable_parts = get_variable_parts(jpg_files)
            if len(variable_parts) >= 5:
                return variable_parts
            else:
                return None
    except zipfile.BadZipFile:
        print(f"Warning: {cbz_path} is not a valid zip file.")
        return None

def process_main_folder(main_folder):
    cbz_dict = {}
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.cbz'):
                cbz_path = os.path.join(root, file)
                result = process_cbz_file(cbz_path)
                if result:
                    cbz_dict[cbz_path] = result
    return cbz_dict

def write_dict_to_txt(result_dict, output_file):
    with open(output_file, 'w') as f:
        for cbz_file, differences in result_dict.items():
            f.write(f"File CBZ: {cbz_file}\n")
            for variable_part, file_names in differences.items():
                f.write(f"  Parte variabile: {variable_part}\n")
                for file_name in file_names:
                    f.write(f"    File: {file_name}\n")
            f.write("\n")

# Esempio di utilizzo
main_folder = '../../../../dune/DATASETS/PSS_DCM/dcm_22k/cbz'
output_file = './dictionary.txt'

result_dict = process_main_folder(main_folder)
write_dict_to_txt(result_dict, output_file)

print(f"Risultati salvati in {output_file}")