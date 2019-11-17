# Create a directory and place "photo.yml", "mail.yml" and "password.txt" in that directory. Change the password file path and Ansible playbook path in ansible command in "udev.sh". Change path of "photo.yml" in Ansible script.

 
# Place the files "udev.sh", "device_added.sh" and "device_removed.sh" in /bin directory and make them executable.


# Place the file "80-usb.rules" in /etc/udev/rules.d directory and don't forget to reload the "udevadm" using:
* udevadm control --reload


# You can change the default allowed device in the system by changing "ATTR{serial}" value in the rule which can be found using command:
* udevadm info -a -n /dev/device_name | grep ATTR{serial}
* "lsblk" command can be used to know the device_name 


# Make a ansible vault file "secret.yml" to store your email password in given dictionary format:
password: your_password
and provide the path in "include_vars" attribute in "mail.yml".


# Make a file "password.txt" to store your vault's password and make sure to have necessary access control over it. I changed its permissions to read-only by root user using "chmod 400 password.txt".


# Make sure to enable "Less secure app access" from your gmail in order to allow Ansible to send mails.


# Python script "photo.py" should be made executable and webcam should be available to allow it to take pictures.

# Fill all the necessary details for mailing in "mail.yml". Both options 'from' and 'username' will/can have sender's email.
