import tkinter as tk
from tkinter import filedialog

class App:
	def __init__(self, root: tk.Tk, menu: dict):
		self.menu = menu

		self.root = root
		self.root.title("Stenography")
		self.root.geometry("450x600")
		self.root.iconbitmap(self.menu['window']['icon'])

		self.menu_bar = tk.Menu(root)

		self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_command(label="Exit", command=root.quit)
		self.menu_bar.add_cascade(label="File", menu=self.file_menu)

		self.customization_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.customization_menu.add_command(label="Background color", command=lambda: self.change_menu("window-background_color"))
		self.customization_menu.add_command(label="Button color", command=lambda: self.change_menu("window-button_color"))
		self.menu_bar.add_cascade(label="Customization", menu=self.customization_menu)

		self.algorithm_menu = tk.Menu(self.menu_bar, tearoff=0)

		self.algorithm_menu.add_checkbutton(label="Use self-written algorithms", command=lambda: self.change_menu("algorithms-self_written(true)"))
		self.algorithm_menu.add_checkbutton(label="Use modul algorithms", command=lambda: self.change_menu("algorithms-self_written(false)"))

		self.algorithm_menu.add_separator()

		self.img_algorithm_menu = tk.Menu(self.algorithm_menu, tearoff=0)
		self.algorithm_menu.add_cascade(label="Image", menu=self.img_algorithm_menu)
		self.audio_algorithm_menu = tk.Menu(self.algorithm_menu, tearoff=0)
		self.algorithm_menu.add_cascade(label="Audio", menu=self.audio_algorithm_menu)
		self.video_algorithm_menu = tk.Menu(self.algorithm_menu, tearoff=0)
		self.algorithm_menu.add_cascade(label="Video", menu=self.video_algorithm_menu)

		self.menu_bar.add_cascade(label="Algorithm", menu=self.algorithm_menu)

		self.language_menu = tk.Menu(self.menu_bar, tearoff=0)
		for k in self.menu["language"].keys():
			self.language_menu.add_command(label=k, command=lambda: self.change_menu(f"language-{k}"))
		self.menu_bar.add_cascade(label="Language", menu=self.language_menu)

		self.root.config(menu=self.menu_bar)

		l = tk.Label(self.root, text="Encode")
		l.config(font=("TkDefaultFont", 20))
		l.place(x=30, y=50)

		self.file_path = ''

		b = tk.Button(root, text="Choose File", command=self.open_file_dialog)
		b.place(x=33, y=90)

		options = ["Audio", "Video", "Image"]

		self.encode_selected_option = tk.StringVar(root)
		self.encode_selected_option.set(options[0])

		encode_option_menu = tk.OptionMenu(root, self.encode_selected_option, *options)
		encode_option_menu.place(x=31, y=120)

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
		b.place(x=33, y=280)

		self.decode_selected_option = tk.StringVar(root)
		self.decode_selected_option.set(options[0])

		encode_option_menu = tk.OptionMenu(root, self.decode_selected_option, *options)
		encode_option_menu.place(x=31, y=310)

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
		pass

	def open_file_dialog(self) -> None:
		file_path = tk.filedialog.askopenfilename()
		if file_path:
			self.file_path = file_path

	def run(self) -> None:
		self.root.mainloop()
