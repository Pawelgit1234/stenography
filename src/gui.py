import tkinter as tk


class App:
	def __init__(self, root: tk.Tk, settings: dict):
		self.root = root
		self.root.title("Stenography")
		self.root.geometry(f"{settings['settings']['window_width']}x{settings['settings']['window_height']}")
		self.root.iconbitmap(settings['settings']['icon'])

		self.dict = dict

	def run(self):
		self.root.mainloop()
