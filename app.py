"""
Fake Bsod Tool By Zoda

28/04/2023

TODO:
    * Block Windows Key (https://code.activestate.com/recipes/553270-using-pyhook-to-block-windows-keys/) [test]
    * Add Different Operating Systems Crash
"""
from win32api import GetSystemMetrics
from tkinter import messagebox
from pathlib import Path
from tkinter import ttk
import os,sys,platform
import tkinter as tk
import threading
import pygame
import time

SOURCEPATH = Path(__file__).parents[0]

def sp(path):
    """Orginal Function -> https://github.com/kadir014/heat2d/blob/master/heat2d/libs/utils.py"""
    return os.path.abspath(os.path.join(SOURCEPATH, path))

monitor_width=GetSystemMetrics(0)
monitor_height=GetSystemMetrics(1)

os.environ["PYGAME_HIDE_SUPPORT_TEXT"]="hide"
pygame.init()


bsod_list={
    "windows":{
        "10":sp("bsod_win10.png")
    }
}

settted_time=None


class Bsod:
    """
    Bsod Screen
    """
    def __init__(self):
        self.wn=pygame.display.set_mode((monitor_width,monitor_height))
        self.done=False
        

        self.bsod_image=bsod_list[platform.system().lower()][platform.release()]
        self.count=0
        self.loop()
    def loop(self):
        pygame.mouse.set_visible(False)
        while not self.done:
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    pass #We don't want them to exit by pressing ALT+F4, do we?
                    
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_LCTRL:
                        if self.count!=2:
                            self.count+=1
                        
                        if self.count==2:
                            pygame.quit()
                            pygame.display.quit()
                            self.done=True

            if not self.done:
                self.wn.fill("blue")
                self.wn.blit(pygame.image.load(self.bsod_image),(0,0))
                pygame.display.update()

        pygame.mouse.set_visible(True)

    
class MainUi:
    """
    Main Ui
    """
    def __init__(self):
        self.wn=tk.Tk()
        self.center_x = int(monitor_width/2 - 500 / 2)
        self.center_y = int(monitor_height/2 - 300 / 2)

        self.wn.wm_title("Fake Bsod Tool By Zoda")
        self.wn.iconbitmap(False,tk.PhotoImage(sp("logo.ico")))
        self.wn.geometry(f"500x300+{self.center_x}+{self.center_y}")
        self.wn.resizable(False,False)

        self.settted_time_tkvar=tk.IntVar()
        #####################################################################

        tk.Label(self.wn,text="Fake Bsod Tool By Zoda",font=('Times 20')).pack()
        tk.Label(self.wn,text="Press 2 Times to 'Control' Key For Ending Fake Bsod",font=("Arial 10")).pack()
        self.setted_time_spinbox=ttk.Spinbox(self.wn,from_=0,to=9**9,textvariable=self.settted_time_tkvar)
        self.button=tk.Button(self.wn,text="Start The Timer",command=self.start_timer)
        
        #####################################################################

        self.button.pack()
        self.setted_time_spinbox.pack(pady=20)
        self.wn.mainloop()

    def start_timer(self):
        try:
            int(self.setted_time_spinbox.get())
        except ValueError:
            messagebox.showerror("ERROR","Please enter numbers or numbers only, not text!")
        else:
            self.wn.withdraw()
            setted_time=int(self.setted_time_spinbox.get())
            time.sleep(setted_time)
            self.wn.deiconify()
            bsod=Bsod()
            

if __name__=="__main__":
    mainui=MainUi()

