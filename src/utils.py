import json

def load_settings(path: str) -> dict:
	with open(path, "r") as file:
		text = file.read()

	return json.loads(text)