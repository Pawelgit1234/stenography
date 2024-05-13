import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re

from utils import dump_json, load_json
from algorithms import *

class App:
	def __init__(self, root: tk.Tk, menu: dict, language: dict):
		self.menu = menu
		self.language = language
		self.last_language = self.menu["settings"]["language"]

		self.root = root
		self.root.title("Stenography")
		self.root.geometry("450x600")
		self.root.iconbitmap(self.menu['settings']['icon'])

		self.menu_bar = tk.Menu(root)

		self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_command(label=self.language[self.last_language]["exit"], command=root.quit)
		self.menu_bar.add_cascade(label=self.language[self.last_language]["file"], menu=self.file_menu)

		self.customization_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.customization_menu.add_command(label=self.language[self.last_language]["dark_theme"], command=lambda: self.change_menu("settings-theme(dark)"))
		self.customization_menu.add_command(label=self.language[self.last_language]["white_theme"], command=lambda: self.change_menu("settings-theme(white)"))
		self.menu_bar.add_cascade(label=self.language[self.last_language]["customization"], menu=self.customization_menu)

		self.algorithm_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.algorithm_menu.add_command(label=self.language[self.last_language]["without_key"], command=lambda: self.change_menu("settings-algorithm(without_key)"))
		self.algorithm_menu.add_command(label=self.language[self.last_language]["with_key"], command=lambda: self.change_menu("settings-algorithm(with_key)"))

		self.menu_bar.add_cascade(label=self.language[self.last_language]["algorithm"], menu=self.algorithm_menu)

		self.language_menu = tk.Menu(self.menu_bar, tearoff=0)

		j = load_json('json/language.json')
		for k in j.keys():
			if k == "choosen":
				continue
			self.language_menu.add_command(label=k, command=lambda lang=k: self.change_menu(f"settings-language({lang})"))
		self.menu_bar.add_cascade(label=self.language[self.last_language]["language"], menu=self.language_menu)

		self.root.config(menu=self.menu_bar)

		self.encode_l = tk.Label(self.root, text="Encode")
		self.encode_l.config(font=("TkDefaultFont", 20))
		self.encode_l.place(x=30, y=50)

		self.file_path = ''

		self.encode_b = tk.Button(root, text="Choose File", command=self.open_file_dialog)
		self.encode_b.place(x=20, y=105)

		self.encode_plus_1 = tk.Label(self.root, text="+")
		self.encode_plus_1.config(font=("TkDefaultFont", 20))
		self.encode_plus_1.place(x=120, y=100)

		self.encode_text_field = tk.Text(root, width=15, height=4)
		self.encode_text_field.place(x=150, y=90)

		self.encode_plus_2 = tk.Label(self.root, text="+")
		self.encode_plus_2.config(font=("TkDefaultFont", 20))
		self.encode_plus_2.place(x=280, y=100)

		self.encode_key_entry = tk.Entry()
		self.encode_key_entry.place(x=305, y=110)

		self.encode_button = tk.Button(text="Do", command=self.encode_text)
		self.encode_button.place(x=200, y=170)

		self.decode_l = tk.Label(self.root, text="Decode")
		self.decode_l.config(font=("TkDefaultFont", 20))
		self.decode_l.place(x=30, y=240)

		self.decode_b = tk.Button(root, text="Choose File", command=self.open_file_dialog)
		self.decode_b.place(x=33, y=295)

		self.decode_plus = tk.Label(self.root, text="+")
		self.decode_plus.config(font=("TkDefaultFont", 20))
		self.decode_plus.place(x=200, y=290)

		self.decode_key_entry = tk.Entry()
		self.decode_key_entry.place(x=305, y=300)

		self.decode_text_field = tk.Text(root, width=15, height=4)
		self.decode_text_field.place(x=150, y=350)

		self.decode_button = tk.Button(text="Do", command=self.decode_text)
		self.decode_button.place(x=200, y=430)

		self.customize()

	def encode_text(self):
		try:
			new_path = self.file_path.split('.')[-2] + "_encoded." + self.file_path.split('.')[-1]

			if self.menu["settings"]["algorithm"] == "with_key":
				encode_with_key(self.file_path, new_path, self.encode_text_field.get("1.0", tk.END), self.encode_key_entry.get())
			else:
				encode_without_key(self.file_path, new_path, self.encode_text_field.get("1.0", tk.END))
		except Exception as e:
			messagebox.showerror("Error", e)

	def decode_text(self):
		try:
			if self.menu["settings"]["algorithm"] == "with_key":
				msg = decode_with_key(self.file_path, self.decode_key_entry.get())
			else:
				msg = decode_without_key(self.file_path)

			self.decode_text_field.insert(tk.END, msg)
		except Exception as e:
			messagebox.showerror("Error", e)

	def change_menu(self, new_menu: str) -> None:
		menu = new_menu.split('-')
		var = re.findall(r'\((.*?)\)', menu[-1])[0]
		menu[-1] = menu[-1][:menu[-1].index('(')]

		self.last_language = self.menu["settings"]["language"]
		self.menu[menu[0]][menu[1]] = var
		dump_json("json/settings.json", self.menu)
		self.customize()

	def customize(self):
		# Theme
		if self.menu["settings"]["theme"] == "dark":
			self.root.config(bg="#2e2e2e")
			self.encode_l.config(bg="#2e2e2e", fg="#d1cbcb")
			self.encode_b.config(bg="#2e2e2e", fg="#d1cbcb")
			self.encode_button.config(bg="#2e2e2e", fg="#d1cbcb")
			self.encode_plus_1.config(bg="#2e2e2e", fg="#d1cbcb")
			self.encode_plus_2.config(bg="#2e2e2e", fg="#d1cbcb")
			self.encode_text_field.config(bg="#1f1e1e", fg="#d1cbcb")
			self.encode_key_entry.config(bg="#1f1e1e", fg="#d1cbcb")
			self.decode_l.config(bg="#2e2e2e", fg="#d1cbcb")
			self.decode_b.config(bg="#2e2e2e", fg="#d1cbcb")
			self.decode_button.config(bg="#2e2e2e", fg="#d1cbcb")
			self.decode_plus.config(bg="#2e2e2e", fg="#d1cbcb")
			self.decode_text_field.config(bg="#1f1e1e", fg="#d1cbcb")
			self.decode_key_entry.config(bg="#1f1e1e", fg="#d1cbcb")
		else:
			self.root.config(bg="#dedede")
			self.encode_l.config(bg="#dedede", fg="#333333")
			self.encode_b.config(bg="#dedede", fg="#333333")
			self.encode_button.config(bg="#dedede", fg="#333333")
			self.encode_plus_1.config(bg="#dedede", fg="#333333")
			self.encode_plus_2.config(bg="#dedede", fg="#333333")
			self.encode_text_field.config(bg="#b5b3b3", fg="#333333")
			self.encode_key_entry.config(bg="#b5b3b3", fg="#333333")
			self.decode_l.config(bg="#dedede", fg="#333333")
			self.decode_b.config(bg="#dedede", fg="#333333")
			self.decode_button.config(bg="#dedede", fg="#333333")
			self.decode_plus.config(bg="#dedede", fg="#333333")
			self.decode_text_field.config(bg="#b5b3b3", fg="#333333")
			self.decode_key_entry.config(bg="#b5b3b3", fg="#333333")
		# Algorithm
		if self.menu["settings"]["algorithm"] == "with_key":
			self.encode_key_entry.config(state="normal")
			self.decode_key_entry.config(state="normal")
		else:
			self.encode_key_entry.config(state="disabled")
			self.decode_key_entry.config(state="disabled")

		# Language
		lan = self.menu["settings"]["language"]
		self.encode_l.config(text=self.language[lan]["encode"])
		self.encode_b.config(text=self.language[lan]["choose_file"])
		self.encode_button.config(text=self.language[lan]["do"])
		self.decode_l.config(text=self.language[lan]["encode"])
		self.decode_b.config(text=self.language[lan]["choose_file"])
		self.decode_button.config(text=self.language[lan]["do"])
		self.menu_bar.entryconfig(self.language[self.last_language]["file"], label=self.language[lan]["file"])
		self.file_menu.entryconfig(self.language[self.last_language]["exit"], label=self.language[lan]["exit"])
		self.menu_bar.entryconfig(self.language[self.last_language]["customization"], label=self.language[lan]["customization"])
		self.customization_menu.entryconfig(self.language[self.last_language]["dark_theme"], label=self.language[lan]["dark_theme"])
		self.customization_menu.entryconfig(self.language[self.last_language]["white_theme"], label=self.language[lan]["white_theme"])
		self.menu_bar.entryconfig(self.language[self.last_language]["algorithm"], label=self.language[lan]["algorithm"])
		self.algorithm_menu.entryconfig(self.language[self.last_language]["without_key"], label=self.language[lan]["without_key"])
		self.algorithm_menu.entryconfig(self.language[self.last_language]["with_key"], label=self.language[lan]["with_key"])
		self.menu_bar.entryconfig(self.language[self.last_language]["language"], label=self.language[lan]["language"])

	def open_file_dialog(self) -> None:
		file_path = tk.filedialog.askopenfilename()
		if file_path:
			self.file_path = file_path

	def run(self) -> None:
		self.root.mainloop()
