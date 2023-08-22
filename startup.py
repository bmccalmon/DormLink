#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import Menu, messagebox

apps_directory = "Apps"

def main():
    root = tk.Tk()
    root.attributes("-fullscreen", True)

    settings_shown = False

    def toggle_settings():
        nonlocal settings_shown
        if settings_shown == False:
            root.grid_rowconfigure(0, weight=1)
            root.columnconfigure(0, weight=5)
            root.columnconfigure(1, weight=1)
            settings_frame.grid(row=0, column=1, sticky="snew") # sticky="snew"
            settings_shown = True
        else:
            settings_frame.grid_forget()
            root.columnconfigure(1, weight=0)
            settings_shown = False

    def button_pressed(info):
        print("Button pressed")

    # Create grid layout with two columns
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create frames
    app_list_frame = tk.LabelFrame(root)
    settings_frame = tk.LabelFrame(root)

    # Create buttons
    app_button_list = list()
    icon_list = list()
    for app in os.listdir(apps_directory):
        icon = tk.PhotoImage(file=f"{apps_directory}/{app}/icon.png")
        icon_list.append(icon)
        #button = tk.Button(app_list_frame, image=icon, bg="white", relief="flat", command=lambda app=app: print(f"{app} clicked")) # in each app folder, there is an icon.png
        button = tk.Label(app_list_frame, image=icon)
        button.bind("<Button-1>", button_pressed)
        app_button_list.append(button)

    settings = tk.Button(app_list_frame, text="Settings", bg="white", relief="flat", command=toggle_settings)
    check_for_updates = tk.Button(settings_frame, text="Check for Updates", bg="white", relief="flat")

    # Lay them out
    app_list_frame.grid(row=0, column=0, sticky="snew") # sticky="snew"
    for app_button in app_button_list:
        app_button.pack(side="left", padx=20, pady=20, fill="x", expand=True)
    settings.pack(side="left", padx=20, pady=20, fill="x", expand=True)
    check_for_updates.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()

