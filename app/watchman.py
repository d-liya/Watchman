import time
from watchdog.observers import Observer
import tkinter as tk
from tkinter import filedialog
import threading
import requests
import pystray
from PIL import Image
import os
from tkinter import ttk
from ttkbootstrap import Style
from observer import FileEventHandler


class WatchmanApp:
    def __init__(self):
        try:
            self.window = tk.Tk()
            self.window.title("Watchman")
            self.window.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)
            self.window.bind("<Map>", self.on_window_deiconify)
            self.style = Style(theme='flatly')

            # Set the window size and center it on the screen
            window_width = 500
            window_height = 300
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            x_coordinate = int((screen_width / 2) - (window_width / 2))
            y_coordinate = int((screen_height / 2) - (window_height / 2))
            self.window.geometry(
                f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

            # Create a frame for the inputs
            self.frame = ttk.Frame(self.window, padding=40, style="TFrame")
            self.frame.pack(pady=20)

            # Heading label
            heading_label = ttk.Label(
                self.frame, text="Watchman", style="THeading")
            heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

            # Function to truncate text if it exceeds the specified length
            def truncate_text(text, length):
                if len(text) > length:
                    return "..." + text[-length+3:]
                return text

            # Define the width for all input fields
            input_width = 30

            # Username input
            username_label = ttk.Label(self.frame, text="Username:")
            username_label.grid(row=1, column=0, sticky="e", padx=10)
            self.username_entry = ttk.Entry(
                self.frame, width=input_width, style="TEntry")
            self.username_entry.grid(row=1, column=1)

            # Password input
            password_label = ttk.Label(self.frame, text="Password:")
            password_label.grid(row=2, column=0, sticky="e", padx=10)
            self.password_entry = ttk.Entry(
                self.frame, show="*", width=input_width, style="TEntry")
            self.password_entry.grid(row=2, column=1)

            # Agency dropdown
            agency_label = ttk.Label(self.frame, text="Agency:")
            agency_label.grid(row=3, column=0, sticky="e", padx=10)
            # Replace with your agency options
            agency_options = ["Option 1", "Option 2", "Option 3"]
            self.agency_selection = tk.StringVar()
            self.agency_dropdown = ttk.Combobox(
                self.frame, textvariable=self.agency_selection, values=agency_options, width=input_width-2, style="TCombobox")
            self.agency_dropdown.grid(row=3, column=1)

            # Folder path input
            folder_label = ttk.Label(self.frame, text="Folder Path:")
            folder_label.grid(row=4, column=0, sticky="e", padx=10)
            self.folder_name = tk.StringVar()
            self.folder_entry = ttk.Entry(
                self.frame, textvariable=self.folder_name, width=input_width, style="TEntry")
            self.folder_entry.grid(row=4, column=1)
            self.select_folder_button = ttk.Button(
                self.frame, text="Select Folder", command=self.select_folder, style="TButton")
            self.select_folder_button.grid(row=4, column=2, padx=(10, 0))

            # Start the main event loop
            self.window.mainloop()
        except Exception as e:
            print(e)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_name.set(folder_path)
        self.start_monitoring_thread(folder_path)

    def start_file_monitoring(self, folder_path):
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, folder_path, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

    def start_monitoring_thread(self, folder_path):
        monitoring_thread = threading.Thread(
            target=self.start_file_monitoring, args=(folder_path,))
        monitoring_thread.daemon = True
        monitoring_thread.start()

    def on_quit_callback(self, icon, item):
        icon.stop()
        self.window.quit()

    def minimize_to_tray(self):
        self.window.withdraw()

        def on_open(icon, item):
            self.window.after(0, self.window.deiconify)
            icon.stop()

        def on_quit(icon, item):
            icon.stop()
            self.window.quit()

        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Relative path to the icon image file
        icon_path = os.path.join(current_directory, "icon.png")

        image = Image.open(icon_path)
        menu = (pystray.MenuItem("Open", on_open),
                pystray.MenuItem("Quit", on_quit))

        icon = pystray.Icon("Watchman", image, "Watchman", menu)
        icon.run()

    def on_window_deiconify(self, event):
        self.window.deiconify()
        self.window.update()
