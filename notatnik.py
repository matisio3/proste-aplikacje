import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get("1.0", tk.END))

def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())

root = tk.Tk()
root.title("Notatnik")

text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Otwórz", command=open_file)
file_menu.add_command(label="Zapisz", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Zamknij", command=root.quit)

menu.add_cascade(label="Plik", menu=file_menu)

root.mainloop()
