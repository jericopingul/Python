import os

def renameFiles():
    # get file names from folder
    files_path = "C:\Users\jericopingul\Dropbox\Udacity\OOP Python\Lesson 1\prank"
    os.chdir(files_path)
    file_list = os.listdir(rfiles_path)
    print(file_list)

    # for each file, rename filename, remove numbers
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
