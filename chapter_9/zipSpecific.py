 #! python3
 # Goes through a directory and archives just files with certain extensions

import zipfile, os, shutil

# TODO: Get folder to archive
folder_dir = (r"C:\Archiver Test")
os.chdir(r"C:\Archiver Test")

# TODO Create ZIP
def archiver(folder, extension):
    extension = extension.lower()

    archiveBase = os.path.basename(folder)
    archiveZip = zipfile.ZipFile(archiveBase+".zip","w") # creates zip to archive

# TODO: Walk through folder
    for root, dir, files in os.walk(folder):
        for file in files:
            file = file.lower()
            if file.endswith("."+extension):
                archiveZip.write(os.path.relpath(os.path.join(root, file)))
    archiveZip.close()
# Copy files with the correct extension into the archive
# Close ZIP

archiver(folder_dir,"png")
