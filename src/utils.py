import json

def load_json(path: str) -> dict:
	try:
		with open(path, "r", encoding="utf-8") as file:
			text = file.read()

		return json.loads(text)
	except FileNotFoundError:
		print(f"{path} not found.")
		return {}