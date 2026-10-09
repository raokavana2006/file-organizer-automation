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
                print(f"[+] Moved: {filename} -> {category}/")
                break

if __name__ == "__main__":
    # Create a test folder called 'demo_folder' inside current directory
    demo_dir = os.path.join(os.getcwd(), "demo_folder")
    os.makedirs(demo_dir, exist_ok=True)

    # Create sample files to sort
    sample_files = ["sample_doc.pdf", "photo1.png", "archive.zip", "notes.txt"]
    for file in sample_files:
        file_path = os.path.join(demo_dir, file)
        if not os.path.exists(file_path):
            open(file_path, "w").close()

    print(f"[*] Created sample files inside: {demo_dir}")
    print("[*] Running File Organizer...\n")

    # Run the organizer function on demo_folder
    organize(demo_dir)

    print("\n[✔] Success! Check 'demo_folder' on your computer to see sorted subfolders.")