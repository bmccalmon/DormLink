#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import Menu, messagebox

import updater

apps_directory = "Apps"
header_size = 30
text_size = 21

def updated_popup(root, n_updates):
    popup = tk.Toplevel(root)
    popup.title("Updater")
    popup_text = ""
    if n_updates > 0:
        popup_text = f"{n_updates} apps were updated. Restart to make changes."
    else:
        popup_text = "You are already up-to-date."
    popup_label = tk.Label(popup, text=popup_text)
    popup_label.pack()
    def set_fullscreen():
        popup.attributes("-fullscreen", True)

    popup.after(100, set_fullscreen)

def main():
    root = tk.Tk()

    settings_shown = False
    def toggle_settings():
        nonlocal settings_shown
        if settings_shown == False:
            root.grid_columnconfigure(0, weight=1)
            root.grid_columnconfigure(1, weight=5)
            settings_label.pack(side="top")
            update_button.pack(pady=50, fill="x")
            settings_shown = True
        else:
            root.columnconfigure(0, weight=1)
            root.columnconfigure(1, weight=5000)
            update_button.pack_forget()
            settings_label.pack_forget()
            settings_shown = False

    # Create grid layout with two columns
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=5000)

    # Initialize frames
    apps_frame = tk.LabelFrame(root, bg="white")
    settings_frame = tk.LabelFrame(root, bg="#d6d6d6")

    # Create app buttons
    app_button_list = list()
    icon_list = list()
    for app in os.listdir(apps_directory):
        icon = tk.PhotoImage(file=f"{apps_directory}/{app}/icon.png")
        icon_list.append(icon)
        button = tk.Label(apps_frame, image=icon, bg="white")
        app_button_list.append(button)

    # Settings buttons
    settings_button = tk.Button(settings_frame, text="", bg="#d6d6d6", relief="flat", borderwidth=0, command=toggle_settings)
    update_button = tk.Button(settings_frame, text="Check for Updates", bg="white", relief="flat", font=("Arial", text_size), command=lambda: updated_popup(root, updater.update_apps()))

    # Create labels
    settings_label = tk.Label(settings_frame, text="Settings", font=("Arial", header_size))

    # Lay them out
    # Apps frame
    apps_frame.grid(row=0, column=1, sticky="snew")
    for app_button in app_button_list:
        app_button.pack(side="left", padx=20, pady=20, fill="x", expand=True)
    # Settings frame
    settings_frame.grid(row=0, column=0, sticky="snew")
    settings_button.pack(side="right", fill="y")

    def set_fullscreen():
        root.attributes("-fullscreen", True)

    root.after(100, set_fullscreen)

    root.mainloop()

if __name__ == "__main__":
    main()

