# Mini project
# Name - Nijay Kumar Jena - 190310126

import string
import random
import os
import shutil

# list containing the extensions
extension = [".jpg", ".png", ".txt", ".pdf"]
file_name = []

# empty string to append the file name
temp_str = ''

# making "all_files" directory to contain all types of files
os.makedirs("all_files", exist_ok=True)

# changing directory to "all_files" from the default directory
os.chdir("all_files")


# generating 25 random files with random extensions
def create_Files():
    for i in range(25):
        # generating name (5 characters)
        file_name.append(temp_str.join(random.choice(string.hexdigits)
        for j in range(5)))

        # adding extension to the file names
        file_name[i] = file_name[i] + random.choice(extension)

        # creating the files
        file_open = open(file_name[i], 'x')

        # closing the file object to avoid unwanted exceptions
        file_open.close()


# function to create respective folders for files with different extensions
def make_Folders(name_file):
    if name_file.endswith(".jpg"):
        try:
            os.makedirs("jpg_folder", exist_ok=True)
        except FileExistsError:
            print("\nFolder already exists moving on...")
            return

    if name_file.endswith(".png"):
        try:
            os.makedirs("png_folder", exist_ok=True)
        except FileExistsError:
            print("\nFolder already exists moving on...")
            return

    if name_file.endswith(".txt"):
        try:
            os.makedirs("txt_folder", exist_ok=True)
        except FileExistsError:
            print("\nFolder already exists moving on...")
            return

    if name_file.endswith(".pdf"):
        try:
            os.makedirs("pdf_folder", exist_ok=True)
        except FileExistsError:
            print("\nFolder already exists moving on...")
            return


# function to organise the random files into respective folders
def classify_Files():
    for name in os.listdir(os.getcwd()):
        if name.endswith(".jpg"):
            print(name)
            make_Folders(name)
            try:
                shutil.move(name, "jpg_folder")
            except:
                print("\nCould not move the file. Moving on with the others ..")
                continue

        elif name.endswith(".png"):
            print(name)
            make_Folders(name)
            try:
                shutil.move(name, "png_folder")
            except:
                print("\nCould not move the file. Moving on with the others ..")
                continue

        elif name.endswith(".txt"):
            print(name)
            make_Folders(name)
            try:
                shutil.move(name, "txt_folder")
            except:
                print("\nCould not move the file. Moving on with the others ..")
                continue

        elif name.endswith(".pdf"):
            print(name)
            make_Folders(name)
            try:
                shutil.move(name, "pdf_folder")
            except:
                print("\nCould not move the file. Moving on with the others ..")
                continue


create_Files()
classify_Files()