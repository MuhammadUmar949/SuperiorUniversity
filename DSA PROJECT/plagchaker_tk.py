import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

class plagchaker:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.text_label1 = tk.Label(self.frame, text="Text 1:")
        self.text_box1 = tk.Text(self.frame, wrap=tk.WORD, width=40, height=10)
        self.text_label2 = tk.Label(self.frame, text="Text 2:")
        self.text_box2 = tk.Text(self.frame, wrap=tk.WORD, width=40, height=10)
        self.file_entry1 = tk.Entry(self.frame, width=50)
        self.load_button1 = tk.Button(self.frame, text="Load File 1", command=lambda: self.load_file(self.file_entry1, self.text_box1))
        self.file_entry2 = tk.Entry(self.frame, width=50)
        self.load_button2 = tk.Button(self.frame, text="Load File 2", command=lambda: self.load_file(self.file_entry2, self.text_box2))
        self.compare_button = tk.Button(root, text="Compare", command=self.show_similarity)
        self.text_boxdiff = tk.Text(root, wrap=tk.WORD, width=80, height=1)

    def load_file(self, entry, text_widget):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        with open(file_path, 'r') as file:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, file.read())

    def compare_text(self, text1, text2):
        similarity = SequenceMatcher(None, text1, text2).ratio()
        return similarity

    def show_similarity(self):
        text1 = self.text_box1.get(1.0, tk.END).strip()
        text2 = self.text_box2.get(1.0, tk.END).strip()
        similarity = self.compare_text(text1, text2)
        self.text_boxdiff.delete(1.0, tk.END)
        self.text_boxdiff.insert(tk.END, f"Similarity: {similarity:.2%}")

root = tk.Tk()
plagchaker = plagchaker(root)
plagchaker.frame.pack()
plagchaker.text_label1.grid(row=0, column=0, padx=5, pady=5)
plagchaker.text_box1.grid(row=0, column=1, padx=5, pady=5)
plagchaker.text_label2.grid(row=1, column=0,padx=5, pady=5)
plagchaker.text_box2.grid(row=1 ,column=1,padx=5, pady=5)
plagchaker.file_entry1.grid(row=2, column=0, padx=5, pady=5)
plagchaker.load_button1.grid(row=2, column=1,padx=5, pady=5)
plagchaker.file_entry2.grid(row=3,column=0, padx=5,pady=5)
plagchaker.load_button2.grid(row=3, column=1, padx=5, pady=5)
plagchaker.compare_button.pack(pady=10)
plagchaker.text_boxdiff.pack(pady=10)
root.mainloop()
