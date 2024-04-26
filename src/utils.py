import json

def load_json(path: str) -> dict:
	try:
		with open(path, "r") as file:
			text = file.read()
	except FileNotFoundError:
		print(f"{path} not found.")
		return {}

	return json.loads(text)