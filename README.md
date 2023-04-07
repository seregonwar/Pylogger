# Keylogger-by-seregon
Keylogger
A Python script that logs keystrokes and uploads them to Dropbox.

Disclaimer
This code is provided for educational and informational purposes only. The author does not condone any illegal or unethical activities. The use of this code for any malicious or unlawful purpose is strictly prohibited. The author shall not be liable for any direct, indirect, or consequential damages arising from the use of this code. Users are solely responsible for compliance with all applicable laws, including but not limited to privacy laws such as the Italian Legislative Decree no. 196/2003 and Law no. 675/1996.

Installation
1. Clone the repository: git clone https://github.com/yourusername/keylogger.git
2. Install the required packages: pip install -r requirements.txt
3. Add your Dropbox access token to the TOKEN variable in keylogger.py.
4. Usage
5. Run the script: python keylogger.py
6. The script will create a new file named keylogger1.txt in the same directory as the script.
7. The script will log all keystrokes until the file size reaches 1 MB, then upload the file to Dropbox and create a new file named keylogger2.txt.
8. The script will continue to log keystrokes every 30 minutes and upload the files to Dropbox.

Notes
The script uses the pynput library to monitor keystrokes. Make sure to run the script with administrative privileges to allow access to keyboard input.
The script requires a Dropbox access token to upload files. You can obtain an access token from the Dropbox Developer Console.
The script logs keystrokes in plain text, so be careful not to enter sensitive information while the script is running.

