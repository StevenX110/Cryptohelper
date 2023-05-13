import hashlib
import os

files_to_check = [
    {'name': 'C:/Windows/System32/cmd.exe', 'hash': '7b7a548f1d5c5683aafd5b2761ceed6a02581c6a30b65a21d85f094ee8b8e0a3'},
    {'name': 'C:/Windows/System32/notepad.exe', 'hash': '1b3c3c8c88f7c34c3878a88e46b4ebed43c10da1a4dd1e918fa97798c7cbe9c5'}
]

def calculate_file_hash(file_path):
    sha = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

for file in files_to_check:
    if os.path.exists(file['name']):
        file_hash = calculate_file_hash(file['name'])
        if file_hash == file['hash']:
            print(f"Hash sum of file {file['name']} is correct")
        else:
            print(f"Hash sum of file {file['name']} incorrect")
    else:
        print(f"File {file['name']} is not found")
