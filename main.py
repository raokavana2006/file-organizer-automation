import os
import shutil

EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Archives': ['.zip', '.tar', '.gz']
}

def organize(target_dir):
    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        if os.path.isdir(filepath):
            continue
        
        ext = os.path.splitext(filename)[1].lower()
        for category, exts in EXTENSION_MAP.items():
            if ext in exts:
                dest_dir = os.path.join(target_dir, category)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_dir, filename))
                print(f"Moved: {filename} -> {category}/")
                break

if __name__ == "__main__":
    print("File Organizer Script Initialized.")