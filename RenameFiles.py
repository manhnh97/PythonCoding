from pathlib import Path

def rename_photos():
    # Folder contains files need rename
    DIR_PATH = Path("F:\Images_Test")
    # Group file need replace
    EXTENSION_FILES = "."+"jpg"
    # Set file name need replace
    FILE_NAME = "Test1"
    # Set number start to replace
    counter = 5
    
    for file in DIR_PATH.iterdir():
        if file.suffix.lower() == EXTENSION_FILES.lower():
            new_file = FILE_NAME + str(counter) + file.suffix
            file.rename(DIR_PATH / new_file)
            counter += 1
            
    print("Rename Success!!!")

if __name__ == "__main__":
    rename_photos()