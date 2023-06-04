# Keylogger-by-seregon

## Keylogger
A Python script that logs keystrokes and uploads them to Dropbox.

## Installation
1. Clone the repository: `git clone https://github.com/seregonwar/keylogger.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Add your Dropbox access token to the `TOKEN` variable in `keylogger.py`.

## Usage
4. Run the script: `python keylogger.py`
5. The script will create a new file named `keylogger1.txt` in the same directory as the script.
6. The script will log all keystrokes until the file size reaches 1 MB, then upload the file to Dropbox and create a new file named `keylogger2.txt`.
7. The script will continue to log keystrokes every 30 minutes and upload the files to Dropbox.

## Notes
- The script uses the pynput library to monitor keystrokes. Make sure to run the script with administrative privileges to allow access to keyboard input.
- The script requires a Dropbox access token to upload files. You can obtain an access token from the Dropbox Developer Console.
- The script logs keystrokes in plain text, so be careful not to enter sensitive information while the script is running.

## Disclaimer

<details>
<summary>Disclaimer:</summary>

  1. The information and code provided in this repository are for educational and informational purposes only. They are not intended to be used in production environments without proper testing and validation.

  2. The code and files in this repository are provided "as is," without warranty of any kind, express or implied. The author and contributors of this repository shall not be held liable for any damages or losses arising from the use of the code or information provided.

  3. The code in this repository may not be complete or up to date. While the author and contributors strive to provide accurate and reliable information, they make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the code or information contained within.

  4. Users of this repository are solely responsible for the usage and implementation of the code and information provided. They should exercise caution and perform their own testing and validation before using the code in any critical or production environments.

  5. Any reliance you place on the code or information provided in this repository is strictly at your own risk. The author and contributors shall not be liable for any direct, indirect, or consequential damages or losses arising from the use or misuse of the code or information provided.

  6. This repository may include third-party libraries, frameworks, or other components. The licenses and terms of use for these dependencies may apply. Users are responsible for complying with the licenses and terms of use associated with such dependencies.

  7. The author and contributors reserve the right to modify, update, or remove any part of this repository without prior notice. They also reserve the right to reject any contributions or suggestions from users.

  8. This repository may contain links to external websites or resources for additional information. The author and contributors do not endorse the content or accuracy of these external resources and are not responsible for any damages or losses resulting from their use.

  9. By using the code or information provided in this repository, you agree to these terms and conditions and acknowledge that you have read and understood the disclaimer.
</details>

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgements

This Keylogger was created by [Seregonwar](https://github.com/seregonwar) as a project for [Course/Workshop/Personal Learning].

If you have any questions or need assistance, feel free to contact  [Seregonwar](https://github.com/seregonwar).
