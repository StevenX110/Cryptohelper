import hashlib
import hmac
import binascii

private_key = b"my_private_key"
message = input("Message: ")
hash_object = hashlib.sha256(message.encode())
hash_hex = hash_object.hexdigest()
signature = hmac.new(private_key, hash_hex.encode(), hashlib.sha256)
signature_hex = binascii.hexlify(signature.digest()).decode()

command = input("Enter command (1 or 2): ")

if command == "1":
    print("Hash-summa message:", hash_hex)
    print("Digital signature:", signature_hex)

elif command == "2":
    password_file = "passwords.txt"

    def hash_password(password):
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()

    def save_password(hash):
        with open(password_file, "a") as f:
            f.write(hash + "\n")

    def check_password(password):
        hash = hash_password(password)
        with open(password_file, "r") as f:
            saved_hashes = f.read().splitlines()
        if hash in saved_hashes:
            print("Pass is correct!")
        else:
            print("Pass is incorrect.")

    new_password = input("Type in new pass: ")
    hash = hash_password(new_password)
    save_password(hash)
    print("Hash summ saved in file", password_file)

    check_password_input = input("Type in pass for scan: ")
    check_password(check_password_input)

else:
    print("Invalid command entered")
