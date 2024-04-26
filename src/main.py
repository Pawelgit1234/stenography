import tkinter as tk

from utils import load_json
from gui import App

def main() -> None:
	settings = load_json("json/settings.json")
	root = tk.Tk()
	app = App(root, settings)
	app.run()

if __name__ == '__main__':
	main()