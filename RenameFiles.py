from pathlib import Path

def rename_photos(directory, extension_file, new_name):
    # Folder contains files need rename
    DIR_PATH = Path(directory)
    # Set number start to replace
    counter = 10
    
    for file in DIR_PATH.iterdir():
        if file.suffix.lower() == '.'+extension_file.lower():
            try:
                new_file = f"{new_name}{counter}{file.suffix}"
                file.rename(DIR_PATH / new_file)
                print(f"Renaming {file.stem} to {new_file}")
                counter += 1
            except FileExistsError as e:
                print(f"- File name \"{file.stem}\" already exists")
            finally:
                print("========== Rename Success!!! ==========")

if __name__ == "__main__":
    rename_photos("F:\images_IT", "jpg", "TestRename")