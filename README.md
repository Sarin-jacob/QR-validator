# QR Validator

## Description

The QR Validator is a Python script designed to validate QR codes and perform actions based on the QR code content. It can be used for tasks such as coupon validation and email notifications.

## Getting Started

To use this script, follow these steps:

1. Run the script, and it will attempt to load a configuration file named "Validator.conf."

2. If the configuration file is not found, the script will guide you through setting up the necessary configurations.

3. You will be prompted to select a CSV file that contains the following headers: Name, Email, Count, Secret. The Count represents the number of coupons purchased, and Secret is the alpha-numeric text of the QR code.

4. You can choose to enable email sending by entering 1 or disable it by entering 0. If enabled, you will be prompted to provide the email configuration details.

5. The script allows you to customize email messages for different scenarios, such as when a coupon is redeemed or when a QR code is invalid.

6. After setting up the configurations, the script will run and validate QR codes based on the provided CSV file.

## Email Sending

If you enable email sending, make sure to follow these steps:

1. Generate an app password and enable two-step verification for your Google account. You can refer to [this link](https://www.febooti.com/products/automation-workshop/tutorials/enable-google-app-passwords-for-smtp.html) for instructions.

2. When prompted, enter the email address from which messages will be sent.

3. Enter the generated app password when prompted.

4. Customize the email messages to be sent for different scenarios.
5. Customize email messages using placeholders like {name}, {cop}, {purchased}, and {timedate}.

## Usage

- The script will open camera feed, when qr detected a alert will show the status of coupon. For QR with multiple coupons an input will be shown and appropriate number can be entered and guide the user based on the configured messages.
- If qr is not getting detected or clear pressing space will open a input box where you can enter the email id linked to coupon.

- The input field shown after pressing space also accept hidden codes to do hidden function:
    - **reconfig** : deletes the config file  
    - **saveconfig** : backup the current config file as .save
    - **entryleft** : Tabulates coupons left
    - **scansdone** : Tabulate numebr of coupons scanned 
    - **savecsv** : save the current state(updated csv by substaracting used coupons) with time and date
    - **exit** : exit the scripy
## Configuration File

The script uses a configuration file named "Validator.conf" to store settings. You can manually edit this file to make changes if needed.

## Dependencies

This script may require external Python packages. Please refer to the `requirements.txt` file for a list of dependencies.

## License

This project is licensed under the [License Name] License - see the [LICENSE.md](LICENSE.md) file for details.

## Author

- Sarin C Jacob
- Contact: sarin.c.jacob2001@gmail.com

Feel free to contact the author for any questions or issues related to this script.

