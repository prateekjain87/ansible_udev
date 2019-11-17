# Create a directory and place "mail.yml" and "password.txt" in that directory. Change the password file path and Ansible playbook path in final command in "udev.sh".
# Place the files "udev.sh", "device_added.sh" and "device_removed.sh" in /bin directory and make them executable.
# Place the file "80-usb.rules" in /etc/udev/rules.d directory
# Make a ansible vault file "secret.yml" to store your email password in dictionary format:
password: your_password
# Make a file "password.txt" to store your vault's password and make sure to have necessary access control over it. I changed its permissions to read-only by root user using "chmod 400 password.txt".
# Make sure to enable "Less secure app access" from your gmail in order to allow Ansible to send mails.
# Python script "photo.py" should be made executable and webcam should be available to allow it to take pictures.
