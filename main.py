import os
import shutil

def get_jpg_file_name_lengths(directory):
    lengths = []
    for file in os.listdir(directory):
        if file.endswith('.jpg') and os.path.isfile(os.path.join(directory, file)):
            name = file[:-4]  # Rimuove ".jpg" dal nome del file
            lengths.append(len(name))
    return lengths

def check_and_copy_directory(src, dst):
    for root, dirs, files in os.walk(src, topdown=True):
        if not dirs:  # Se non ci sono ulteriori sottocartelle
            lengths = get_jpg_file_name_lengths(root)
            if lengths:
                min_length = min(lengths)
                max_length = max(lengths)
                if max_length - min_length >= 2 and len([l for l in lengths if l >= min_length + 2]) >= 5:
                    dst_path = os.path.join(dst, os.path.relpath(root, src))
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    shutil.copytree(root, dst_path)
                    print(f"Copied: {root} to {dst_path}")

def main():
    src = '/media/andrea/FILMINI/andrea/subset_images'
    dst = '/media/andrea/FILMINI/andrea/booksGood'
    if not os.path.exists(dst):
        os.makedirs(dst)

    check_and_copy_directory(src, dst)

if __name__ == "__main__":
    main()