import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x200")

        self.length_var = tk.IntVar()

        # Label and entry for password length
        self.length_label = tk.Label(master, text="Enter password length:")
        self.length_label.pack(pady=10)
        self.length_entry = tk.Entry(master, textvariable=self.length_var, width=10)
        self.length_entry.pack(pady=10)

        # Button to generate password
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Label to display the generated password
        self.password_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.password_label.pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length < 1:
            messagebox.showwarning("Warning", "Please enter a valid password length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        self.password_label.config(text=f"Generated Password: {password}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
