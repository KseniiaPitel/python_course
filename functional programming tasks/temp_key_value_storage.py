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

#проверка что был передан только Key

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', '-key', action='store')
    parser.add_argument('--val', '-val', action='store')
    args = parser.parse_args()
    return args.key, args.val


val_check = create_parser()

if val_check[1] is None:
    search_result = frame.get(val_check[0])
    print(search_result)

#запись в файл если было передано два значения key val
else:
    key = val_check[0]
    val = val_check[1]

    if key in frame:
        temp_val = frame.get(key)
        frame.update({key: temp_val + ", " + val})
        with open(storage_path, 'w') as f:
            (f.write(json.dumps(frame, indent=1)))
    else:
        frame[key] = val
        with open(storage_path, 'w') as f:
            (f.write(json.dumps(frame, indent=1)))