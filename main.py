#luncher of GUI
import os
import sys
text='==============================\n|Select GUI:                 |\n|"0" for Beta version        |\n|"1" for Origin version      |\n=============================='
print(text)
Select = int(input())
while 1:
    if Select == 0:
        os.system('python GUI.py')
    elif Select == 1:
        os.system('python Interface.py')
    else:
        print('pls try again\n',text)
    try:
        Select = int(input())
    except Exception:
        sys.exit(0)
        