import tkinter as tk

from Beta.data import *
from Beta.Service import *
from Beta.config import *

if __name__ == '__main__':

    SearchFrame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    ButtonFrame.pack(expand=True, fill=tk.BOTH)
    ListFrame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

    SearchButton.pack(in_=SearchFrame,
                      side=tk.RIGHT,
                      expand=tk.NO,
                      ipadx=30, ipady=10,
                      anchor=tk.NE)

    InputBox.pack(in_=SearchFrame,
                  side=tk.TOP,
                  expand=tk.NO,
                  ipady=20,
                  fill=tk.X,
                  anchor=tk.N)

    

    BookAddButton.pack(in_=ButtonFrame,
                       side=tk.LEFT,
                       expand=tk.YES, fill=tk.Y,
                       ipadx=20, ipady=5,
                       # anchor=tk.W
                       )

    

    BookDeclineButton.pack(in_=ButtonFrame,
                           side=tk.RIGHT,
                           expand=tk.YES, fill=tk.Y,
                           ipadx=20, ipady=5,
                           # anchor=tk.E
                           )

    lb.pack(in_=ListFrame,
            side=tk.LEFT,
            expand=tk.YES,
            # anchor=tk.NW,
            fill=tk.Y,
            ipady=160
            )

    
    lb2.pack(in_=ListFrame,
             side=tk.RIGHT,
             expand=tk.YES,
             # anchor=tk.NE,
             fill=tk.Y,
             ipady=160
             )

    sb.config(command=lb.yview)
    sb2.config(command=lb2.yview)

    window.mainloop()