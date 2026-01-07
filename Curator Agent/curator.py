import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# AUTOMATICALLY FIND DOWNLOADS FOLDER
DOWNLOADS_DIR = os.path.expanduser('~/Downloads')

DESTINATIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Software": [".exe", ".msi", ".dmg", ".pkg"],
    "Zips": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".js", ".html", ".css"],
    "Video": [".mp4", ".mkv", ".mpeg", ".avi", ".mov", ".wmv"],
    "Audio": [".wav", ".mp3", ".aac", ".m4a", ".flac", ".ogg", ".wma", ".m3a", ".mpa", ".opus"]
}

class JanitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.clean_folder()

    def clean_folder(self):
        for filename in os.listdir(DOWNLOADS_DIR):
            file_path = os.path.join(DOWNLOADS_DIR, filename)
            
            if os.path.isdir(file_path) or filename.startswith('.'):
                continue

            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            for category, extensions_list in DESTINATIONS.items():
                # Convert all extensions in the list to lowercase for comparison
                lowercase_extensions = [ext.lower() for ext in extensions_list]
                if extension in lowercase_extensions:
                    self.move_file(file_path, filename, category)
                    break

    def move_file(self, source, filename, category):
        dest_dir = os.path.join(DOWNLOADS_DIR, category)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        dest_path = os.path.join(dest_dir, filename)
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(dest_dir, f"{base}({counter}){ext}")):
                counter += 1
            dest_path = os.path.join(dest_dir, f"{base}({counter}){ext}")

        try:
            shutil.move(source, dest_path)
            print(f"Moved: {filename} -> {category}")
        except Exception:
            pass

if __name__ == "__main__":
    print(f"Watching folder: {DOWNLOADS_DIR}")
    handler = JanitorHandler()
    handler.clean_folder()
    observer = Observer()
    observer.schedule(handler, DOWNLOADS_DIR, recursive=False)
    observer.start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()