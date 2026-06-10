import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False

            for category, extensions in FILE_TYPES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    category_folder = os.path.join(folder_path, category)

                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)

                    shutil.move(file_path, os.path.join(category_folder, file))
                    print(f"Moved: {file} -> {category}")
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")

                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)

                shutil.move(file_path, os.path.join(others_folder, file))
                print(f"Moved: {file} -> Others")

folder = input('Enter folder path to organize: ')
organize_files(folder)
print('Files organized successfully!')
