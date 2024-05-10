import json

def load_json(path: str) -> dict:
	try:
		with open(path, "r", encoding="utf-8") as file:
			text = file.read()

		return json.loads(text)
	except FileNotFoundError:
		print(f"{path} not found.")
		return {}


def dump_json(path: str, data: dict) -> None:
	try:
		with open(path, "w", encoding="utf-8") as file:
			file.write(json.dumps(data, indent=4, ensure_ascii=False))

	except FileNotFoundError:
		print(f"{path} not found.")