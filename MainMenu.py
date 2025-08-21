import tkinter as tk
from File_Encryption import * # import my file encryption/decryption module
from File_Integrity_Checker import * # import my file integrity checker
from Password_Strength_Meter import * # import my password strength meter

def on_click1():
    main_scramble()

def on_click2():
    password_meter()

def on_click3():
    file_integrity()

def on_click4():
    exit()

# Create the main window
root = tk.Tk()
root.title("Cyber Security Toolkit") #Give the title of the menu screen
root.geometry("500x400")
root.attributes("-topmost", True) #Make the menu screen always stay on top

# Create a button

button1 = tk.Button(root, text="Data Scrambling", command=on_click1)
comment1 = tk.Label(root, text="A module for transposition cipher.", fg="gray")
button2 = tk.Button(root, text="Password strength Meter", command=on_click2)
comment2 = tk.Label(root, text="A score system for measuring the strength of password.", fg="gray")
button3 = tk.Button(root, text="File Integrity Check", command=on_click3)
comment3 = tk.Label(root, text="A module for file integrity check by comparing the hash value", fg="gray")
button4 = tk.Button(root, text="Exit", command=on_click4)
button1.pack(anchor="w", padx=10, pady=10)
comment1.pack(anchor="w", padx=10, pady=2)  # 10 pixels indentation
button2.pack(anchor="w", padx=10, pady=20)
comment2.pack(anchor="w", padx=10, pady=2)
button3.pack(anchor="w", padx=10, pady=20)
comment3.pack(anchor="w", padx=10, pady=2)
button4.pack(anchor="w", padx=10, pady=20)



# Run the application
root.mainloop()


