import json
import tempfile
import os

key = int(input("Key: "))
val = input("Val: ")
frame = {key: val}


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'a+b') as f:
    f.write(bytes(json.dumps(frame, allow_nan=True, indent=None), 'UTF-8'))
    f.seek(0)
    print(f.read().decode())

    print(storage_path)


