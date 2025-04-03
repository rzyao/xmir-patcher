#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

import xmir_base
import gateway
from gateway import die
from gateway import main as gateway_main
from connect import main as connect_main
from read_info import main as read_info_main
from create_backup import main as create_backup_main
from install_lang import main as install_lang_main
from install_ssh import main as install_ssh_main
from install_fw import main as install_fw_main
from reboot import main as reboot_main
from passw import main as passw_main
from read_dmesg import main as read_dmesg_main
from activate_boot import main as activate_boot_main
from install_bl import main as install_bl_main
                                                                                      
gw = gateway.Gateway(detect_device = False, detect_ssh = False)

def get_header(delim, suffix = ''):
  header = delim*58 + '\n'
  header += '\n'
  header += 'Xiaomi MiR Patcher {} \n'.format(suffix)
  header += '\n'
  return header

def menu1_show():
  gw.load_config()
  print(get_header('='))
  print(' 1 - Set IP-address (current value: {})'.format(gw.ip_addr))
  print(' 2 - Connect to device (install exploit)')
  print(' 3 - Read full device info')
  print(' 4 - Create full backup')
  print(' 5 - Install EN/RU languages')
  print(' 6 - Install permanent SSH')
  print(' 7 - Install firmware (from directory "firmware")')
  print(' 8 - {{{ Other functions }}}')
  print(' 9 - [[ Reboot device ]]')
  print(' 0 - Exit')

def menu1_process(id):
  if id == 1: 
    ip_addr = input("Enter device IP-address: ")
    gateway_main(ip_addr)
    return [ "gateway.py", ip_addr ]
  if id == 2: 
    connect_main()
    return "connect.py"
  if id == 3: 
    read_info_main()
    return 'read_info.py'
  if id == 4: 
    create_backup_main()
    return "create_backup.py"
  if id == 5: 
    install_lang_main()
    return "install_lang.py"
  if id == 6: 
    install_ssh_main()
    return "install_ssh.py"
  if id == 7: 
    install_fw_main()
    return "install_fw.py"
  if id == 8: return "__menu2"
  if id == 9: 
    reboot_main()
    return "reboot.py"
  if id == 0: sys.exit(0)
  return None

def menu2_show():
  print(get_header('-', '(extended functions)'))
  print(' 1 - Set IP-address (current value: {})'.format(gw.ip_addr))
  print(' 2 - Change root password')
  print(' 3 - Read dmesg and syslog')
  print(' 4 - Create a backup of the specified partition')
  print(' 5 - Uninstall EN/RU languages')
  print(' 6 - Set kernel boot address')
  print(' 7 - Install Breed bootloader')
  print(' 8 - __test__')
  print(' 9 - [[ Reboot device ]]')
  print(' 0 - Return to main menu')

def menu2_process(id):
  if id == 1:
    ip_addr = input("Enter device IP-address: ")
    return [ "gateway.py", ip_addr ]
  if id == 2: 
    passw_main()
    return "passw.py"
  if id == 3: 
    read_dmesg_main()
    return "read_dmesg.py"
  if id == 4: 
    create_backup_main()
    return [ "create_backup.py", "part" ]
  if id == 5: 
    install_lang_main()
    return [ "install_lang.py", "uninstall" ]
  if id == 6: 
    activate_boot_main()
    return "activate_boot.py"
  if id == 7: 
    install_bl_main("breed")
    return [ "install_bl.py", "breed" ]
  if id == 8: return "test.py"
  if id == 9: 
    reboot_main()
    return "reboot.py"
  if id == 0: return "__menu1" 
  return None

def menu_show(level):
  if level == 1:
    menu1_show()
    return 'Select: '
  else:
    menu2_show()
    return 'Choice: '

def menu_process(level, id):
  if level == 1:
    return menu1_process(id)
  else:
    return menu2_process(id)

def menu():
  level = 1
  while True:
    print('')
    prompt = menu_show(level)
    print('')
    select = input(prompt)
    print('')
    if not select:
      continue
    try:
      id = int(select)
    except Exception:
      id = -1
    if id < 0:
      continue
    try:
      cmd = menu_process(level, id)
    except Exception as e:
      print(f"Error: {e}")
      continue
    if not cmd:
      continue
    if cmd == '__menu1':
      level = 1
      continue
    if cmd == '__menu2':
      level = 2
      continue
    #print("cmd2 =", cmd)

def main():
    try:
        # 你的主程序逻辑
        menu()
    except Exception as e:
        print(f"发生错误: {e}")
        input("按任意键退出...")  # 等待用户输入

if __name__ == "__main__":
    main()


