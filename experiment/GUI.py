import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize main window
root = tk.Tk()
root.title = ("File Organizer")
root.geometry("500x400")

# Global Variables to store the folder path
source_path = ""
destination_path = ""

# GUI Component
source_label = tk.Label(root, text="Source Folder: Not selected")
source_label.pack(pady=5)