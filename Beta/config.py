#config of GUI

import tkinter as tk

# version information
TitleName = 'BetaDemo'
Version = '0.1.4'
# 谢邀，本人代码是逆练出来的，请谅解

# define Window
window = tk.Tk()
window.title(f'{TitleName}  {Version}')
window.geometry('800x600')


SearchFrame = tk.Frame(window)
ButtonFrame = tk.Frame(window)
ListFrame = tk.Frame(window)

