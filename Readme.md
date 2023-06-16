# Watchman

Watchman is a file monitoring application that allows you to track changes in a specified folder and receive real-time notifications. It helps you stay updated on any modifications made to files within the monitored directory.

## Installation

To install and run Watchman, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/d-liya/Watchman.git
   ```

2. Navigate to the project directory:

   ```
   cd Watchman
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Ensure that you have the necessary permissions to access the files in the monitored folder.

5. Run the application:

   ```
   python main.py
   ```

## Current Issues

1. **Permission Error:** When running the application, you may encounter a `PermissionError` if the application doesn't have sufficient permissions to access the monitored folder. Please ensure that the user running the application has the necessary read and write permissions for the specified folder.

   - If you're using Windows, run the application with administrative privileges or grant appropriate access permissions to the folder.
   - On Linux or macOS, ensure that the user running the application has the required permissions for the folder.

   If you're still experiencing issues, please refer to the documentation or seek assistance from the support team.

2. **Tray Icon Styling:** The current version of the application uses basic styling for the system tray icon menu items. Customizing the styling of menu items, such as adding themes or changing colors, is a work in progress.

   We are actively working to enhance the styling options and provide a more customizable user interface in future updates.
