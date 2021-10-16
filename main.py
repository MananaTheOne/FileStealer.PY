"""
Made By Manana.

This program steals your files.
and does nothing but just copy it in a folder.
"""
import os
import random

datalist = "1234567890abcdef"

"""
NOTE :
    Setting this to True
    will delete the file upon copy
    so it means it just cut + pastes it.
"""
delete_on_copy = False

"""
NOTE :
    Setting this to True
    will override the file on copy
    it means it will replace the content with a random 32-bit data.
"""
corrupt_on_copy = False
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
            if corrupt_on_copy:
                x = 0
                randomdata = ""
                while not x == 2 :
                    x+=1
                    randomdata+=random.choice(datalist)
                randomdata = eval(f"0x{randomdata}")
                with open(filename, "wb") as file:
                    file.write(randomdata)
            with open(f"copies/{filename}", "wb") as copy: # Opens the contents of file and writes it as a copy
                copy.write(contents)
