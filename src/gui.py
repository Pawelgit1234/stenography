import tkinter as tk


class App:
	def __init__(self, root: tk.Tk, settings: dict):
		self.root = root
		self.root.title("Stenography")
		self.root.geometry("400x600")
		self.root.iconbitmap(settings['window']['icon'])

		self.dict = settings

		self.menu_bar = tk.Menu(root)
		self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_command(label="Exit", command=root.quit)
		self.menu_bar.add_cascade(label="File", menu=self.file_menu)

		self.root.config(menu=self.menu_bar)

	def run(self):
		self.root.mainloop()
