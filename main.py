import os

# All File Extensions, You Can Replace It If You Want.
file_extensions = [
    '.pdf',
    '.mp4',
    '.avi',
    '.mp3',
    '.wav',
    '.ogg',
    '.mov',
    '.gif',
    '.txt',
    '.png',
    '.jpeg',
    '.jpg',
]

# Makes A Folder If It Does Not Exist In The Current Directory.
if not os.path.exists("copies"):
    os.mkdir("copies")

for i in os.listdir(): # Lists all the files in the directory where the python file is placed
    for e in file_extensions:
        if i.endswith(e): # Checks for file
            with open(i, "rb") as file: # Opens the file
                contents = file.read()
                filename = i.split("/")[-1] # Gets the filename by splitting the directory to a list and getting the last entry.
            with open(f"copies/{filename}", "wb") as copy: # Opens the contents of file and writes it as a copy
                copy.write(contents)
