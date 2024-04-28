import tkinter as tk

from utils import load_json
from gui import App

def main() -> None:
	settings = load_json("json/settings.json")
	language = load_json("json/language.json")
	menu = settings | language
	root = tk.Tk()
	app = App(root, menu)
	app.run()

if __name__ == '__main__':
	main()