import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import os

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Trigger the upload process here
        if not event.is_directory:
            file_path = event.src_path
            is_file_access_allowed = self.is_file_access_allowed(file_path)
            print(f"New file created: {file_path}")
            print(f"File access allowed: {is_file_access_allowed}")
            self.upload_file(file_path)

    def on_modified(self, event):
        # Trigger the update process here
        if not event.is_directory:
            file_path = event.src_path
            is_file_access_allowed = self.is_file_access_allowed(file_path)
            print(f"File modified: {file_path}")
            self.upload_file(file_path)

    def on_deleted(self, event):
        # Trigger the deletion process here
        if not event.is_directory:
            file_path = event.src_path
            is_file_access_allowed = self.is_file_access_allowed(file_path)
            
            print(f"File deleted: {file_path}")
            self.delete_file(file_path)
    
    def is_file_access_allowed(self, file_path):
        # Check if the file exists
        if os.path.exists(file_path):
            # Check if the file is readable
            if os.access(file_path, os.R_OK):
                # File exists and is readable
                print("File exists and is readable.")
                return True
                # Perform the desired operations on the file
            else:
                # File is not readable
                print("Permission denied: File is not readable.")
        else:
            # File does not exist
            print("File does not exist.")
        return False

    def upload_file(self, file_path):
        # Prepare the API request
        url = "http://your-api-endpoint"  # Replace with your API endpoint
        files = {"file": open(file_path, "rb")}  # Open the file in binary mode

        # Send the HTTP POST request
        # response = requests.post(url, files=files)

        # # Check the response status
        # if response.status_code == 200:
        #     print("File uploaded successfully!")
        # else:
        #     print("Error uploading file:", response.text)

        print("File uploaded successfully!")
    
    def delete_file(self, file_path):
        # Prepare the API request
        url = "http://your-api-endpoint"
        data = {"file_path": file_path}

        # Send the HTTP POST request
        # response = requests.delete(url, data=data)

        # # Check the response status
        # if response.status_code == 200:
        #     print("File deleted successfully!")
        # else:
        #     print("Error deleting file:", response.text)

        print("File deleted successfully!")


