import json
import tempfile
import os
import sys
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
print(storage_path)


def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


if is_non_zero_file(storage_path) == False:
    frame = {}

else:
    with open(storage_path, 'r') as f:
        frame = json.load(f)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-k', '--key', required=True)
   # parser.add_argument('-n', '--name', '--val')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    key=str(namespace.name)

# key = input("Key: ")
# val = input("Val: ")
val = "test"
# frame[key] = val

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

search_key = input("Search key: ")
search_result = frame.get(search_key)
print("Searched values: ", search_result)
