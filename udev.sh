#!/bin/bash
/bin/device_added.sh
ansible-playbook --vault-password-file=/ansi/password.txt /ansi/mail.yml
