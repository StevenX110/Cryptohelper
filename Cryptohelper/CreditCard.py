import hashlib

def hash_credit_card_info(credit_card_info):
    sha = hashlib.sha256()
    sha.update(credit_card_info.encode('utf-8'))
    return sha.hexdigest()

credit_card_info = "YourCard"

hashed_credit_card_info = hash_credit_card_info(credit_card_info)

print("Hash data sum of credit card :", hashed_credit_card_info)
