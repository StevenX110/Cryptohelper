import hashlib
import requests

file_url = "https://example.com/files/file.txt"

response = requests.get(file_url)
file_contents = response.content

file_hash = hashlib.sha256(file_contents).hexdigest()

# Проверка соответствия хеш-суммы оригинальной хеш-сумме
if file_hash == "6a2e0f8835c56c9515b5a0719d7c0e9c79a89c7b5a678d7d54b8d5d2ccf3a8fc":
    print("Hash sum of file does not matching with original sum")
  
else:
    print("Hash sum of file does not matching with original sum")
    
