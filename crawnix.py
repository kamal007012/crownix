#import win_unicode_console , colorama
import os , subprocess

#width = os.get_terminal_size().columns


def banner():
    print("""
                _________                              _________  __
                __  ____/____________ ___      ___________(_)_  |/ /
                _  /    __  ___/  __ `/_ | /| / /_  __ \_  /__    / 
                / /___  _  /   / /_/ /__ |/ |/ /_  / / /  / _    |  
                \____/  /_/    \__,_/ ____/|__/ /_/ /_//_/  /_/|_|  v1.0\n""" )




def crawl():
    from modules import crawler

#The main routine
def main():
    banner()
    a = 1
    if a == a:
        crawl()

try:
    main()
except Exception as e:
    print("fucking bitch")
