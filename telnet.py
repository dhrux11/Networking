import os
with open('G:/tanvi/docs.txt.txt') as file:
    dump=file.read()
    dump=dump.splitlines()

    for ip in dump:
        os.system('telnet '+ip)
