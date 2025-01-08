import shutil
import os

alphabet_list = []  
for i in range(97, 123):  
    alphabet_list.append(chr(i))
#misc category is for files that do not start with alphabetical letters
alphabet_list.append('misc')  

filetypes = [
    # Text and Document Files
    ".txt", ".doc", ".docx", ".pdf", ".rtf", 

    # Image Files
    ".jpg", ".jpeg", ".png", ".gif",

    # Audio Files
    ".mp3", ".wav",

    # Video Files
    ".mp4", ".mkv",

    # Compressed Files
    ".zip", ".rar"
]

def create_folders(choice):
    #Creates folders in the target directory to organize into, either folders with the file extension names or folders in alphabetical order
    if choice == '0':
        for filetype in filetypes:
            folder_name = filetype[1:]
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
    if choice == '1':
        for letter in alphabet_list:
            folder_name = letter
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
def move_files(choice):
    #moves files into their designated folders, checks either the file extension to move into folders or checks the first character of the filename to sort into folders
    if choice == '0':
        dir_list = os.listdir()
        folder_list = [folder for folder in dir_list if not os.path.isfile(folder)]
        file_list = [file for file in dir_list if os.path.isfile(file)]
        for file in file_list:
            root, ext = os.path.splitext(file)
            for folder in folder_list:
                if ext[1:] == folder:
                    shutil.move(file, folder)

    elif choice == '1':
        dir_list = os.listdir()
        folder_list = [folder for folder in dir_list if not os.path.isfile(folder)]
        file_list = [file for file in dir_list if os.path.isfile(file)]
        for file in file_list:
            root, ext = os.path.splitext(file)
            for folder in folder_list:
                if root[0].lower() == folder.lower():
                    shutil.move(file, folder)
        remaining_files = [file for file in dir_list if os.path.isfile(file)]
        for file in remaining_files:
            shutil.move(file,'misc')
                         

def file_manager(choice):
    create_folders(choice)
    move_files(choice)

#Retrieves directory to organize
targetdir = input('What is the directory that you want to be organized?\n')
os.chdir(targetdir)

#Allows for choice between file type organization or alphabetical organization
organization_choice = input('How would you like the files to be organized by?\n Type 0 for by file type \n Type 1 for alphabetical\n')
file_manager(organization_choice)


