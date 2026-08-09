import os # os module for file and directory operations
import shutil # shutil module for moving files

#folder path you want to organize
folder_path = os.getcwd() # Current working directory

# file type mapping
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.odt','.csv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],     
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}
# Create folders if they don't exist
for folder in file_types.keys(): # create folders for each file type
    folder_dir = os.path.join(folder_path, folder)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

#organize files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
  #skip folder
    if os.path.isdir(file_path):
        continue
    
    #move files to respective folders
    for folder, extensions in file_types.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(folder_path, folder, filename))
            


