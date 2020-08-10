import json
import argparse
import tempfile
import os.path

def output_func(*args):
	print(", ".join(*args))

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
# Обработка аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument("--key", '-k', help="choose the key")
parser.add_argument("--val", '-v', help="choose the value to add")
args = parser.parse_args()

# Загрузка данных из фалйа
if os.path.isfile(storage_path):
	f = open(storage_path,'r')
	_dict = json.load(f)
	f.close()
else:
	_dict = {}

# Проверка аргументов командной строки
if args.key and args.val:
	if args.key not in _dict:
		_dict[args.key] = [args.val]
	else:
		_dict[args.key].append(args.val)
	with open(storage_path, 'w') as f:
		json.dump(_dict, f)
elif args.key:
	if os.path.isfile(storage_path):
		with open(storage_path, 'r') as f:
			if args.key in _dict:
				output_func(_dict[args.key])
				#print(_dict[args.key])
			else:
				print("None")
	else:
		print("None")
else:
	print("Input error")