import tkinter as tk
from tkinter import filedialog
import re

from utils import dump_json, load_json

class App:
	def __init__(self, root: tk.Tk, menu: dict):
		self.menu = menu

		self.root = root
		self.root.title("Stenography")
		self.root.geometry("450x600")
		self.root.iconbitmap(self.menu['settings']['icon'])

		self.menu_bar = tk.Menu(root)

		self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_command(label="Exit", command=root.quit)
		self.menu_bar.add_cascade(label="File", menu=self.file_menu)

		self.customization_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.customization_menu.add_checkbutton(label="Dark Theme", command=lambda: self.change_menu("settings-background_theme(dark)"))
		self.customization_menu.add_checkbutton(label="White Theme", command=lambda: self.change_menu("settings-background_theme(white)"))
		self.menu_bar.add_cascade(label="Customization", menu=self.customization_menu)

		self.algorithm_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.algorithm_menu.add_checkbutton(label="Without key", command=lambda: self.change_menu("settings-algorithm(without_key)"))
		self.algorithm_menu.add_checkbutton(label="With key", command=lambda: self.change_menu("settings-algorithm(with_key)"))

		self.menu_bar.add_cascade(label="Algorithm", menu=self.algorithm_menu)

		self.language_menu = tk.Menu(self.menu_bar, tearoff=0)

		j = load_json('json/language.json')
		for k in j.keys():
			if k == "choosen":
				continue
			self.language_menu.add_checkbutton(label=k, command=lambda lang=k: self.change_menu(f"settings-language({lang})"))
		self.menu_bar.add_cascade(label="Language", menu=self.language_menu)

		self.root.config(menu=self.menu_bar)

		l = tk.Label(self.root, text="Encode")
		l.config(font=("TkDefaultFont", 20))
		l.place(x=30, y=50)

		self.file_path = ''

		b = tk.Button(root, text="Choose File", command=self.open_file_dialog)
		b.place(x=33, y=105)

		l = tk.Label(self.root, text="+")
		l.config(font=("TkDefaultFont", 20))
		l.place(x=120, y=100)

		self.text_encode = tk.Text(root, width=15, height=4)
		self.text_encode.place(x=150, y=90)

		l = tk.Label(self.root, text="+")
		l.config(font=("TkDefaultFont", 20))
		l.place(x=280, y=100)

		self.encode_key_entry = tk.Entry()
		self.encode_key_entry.place(x=305, y=110)

		self.encode_button = tk.Button(text="Do", command=self.encode_text)
		self.encode_button.place(x=200, y=170)

		l = tk.Label(self.root, text="Decode")
		l.config(font=("TkDefaultFont", 20))
		l.place(x=30, y=240)

		b = tk.Button(root, text="Choose File", command=self.open_file_dialog)
		b.place(x=33, y=295)

		l = tk.Label(self.root, text="+")
		l.config(font=("TkDefaultFont", 20))
		l.place(x=200, y=290)

		self.decode_key_entry = tk.Entry()
		self.decode_key_entry.place(x=305, y=300)

		self.text_decode = tk.Text(root, width=15, height=4)
		self.text_decode.place(x=150, y=350)

		self.decode_button = tk.Button(text="Do", command=self.decode_text)
		self.decode_button.place(x=200, y=430)

	def encode_text(self):
		pass

	def decode_text(self):
		pass

	def change_menu(self, new_menu: str) -> None:
		menu = new_menu.split('-')
		var = re.findall(r'\((.*?)\)', menu[-1])[0]
		menu[-1] = menu[-1][:menu[-1].index('(')]

		self.menu[menu[0]][menu[1]] = var
		dump_json("json/settings.json", self.menu)

	def open_file_dialog(self) -> None:
		file_path = tk.filedialog.askopenfilename()
		if file_path:
			self.file_path = file_path

	def run(self) -> None:
		self.root.mainloop()
