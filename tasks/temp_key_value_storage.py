import json
import tempfile
import os
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


if is_non_zero_file(storage_path) == False:
    frame = {}

else:
    with open(storage_path, 'r') as f:
        frame = json.load(f)

parser = argparse.ArgumentParser()
key = parser.add_argument('-1', '--key', action='store')
val = parser.add_argument('-1', '--val', action='store')
#key = input("Key: ")
#val = input("Val: ")

#frame[key] = val

if key in frame:
    temp_val = frame.get(key)
    frame.update({key: temp_val + ", " + val})
    with open(storage_path, 'w') as f:
        (f.write(json.dumps(frame, indent=1)))
else:
    frame[key] = val
    with open(storage_path, 'w') as f:
        (f.write(json.dumps(frame, indent=1)))

print(frame)

search_key=input("Search key: ")
search_result = frame.get(search_key)
print("Searched values: ", search_result)


