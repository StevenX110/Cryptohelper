import hashlib

file_path = "/path/to/file"
known_hash = "e7616d94c7a9db82d31af73dbd4d586fe16913631f330109a4b5036fb0fc8cc4"

command = input("Enter command (1 or 2): ")

if command == "1":
    with open(file_path, "rb") as f:
        lines = f.readlines()[0:10]
        for line in lines:
            print(line.decode().rstrip())

elif command == "2":
    password = input("Type in pass: ")
    hash_object = hashlib.sha256(password.encode())
    hash_hex = hash_object.hexdigest()
    print("Hash summarage:", hash_hex)

else:
    print("Invalid command entered")
