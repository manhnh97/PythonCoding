from pathlib import Path

def rename_photos(directory, extension_file, new_name):
    # Folder contains files need rename
    DIR_PATH = Path(directory)
    # Set number start to replace
    counter = 1
    
    for file in DIR_PATH.iterdir():
        if file.suffix.lower() == '.'+extension_file.lower():
            new_file = new_name + str(counter) + file.suffix
            file.rename(DIR_PATH / new_file)
            counter += 1
            
    print("Rename Success!!!")

if __name__ == "__main__":
    rename_photos("F:\images_IT", "jpg", "TestRename")