import tkinter as tk
from tkinter import ttk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class AutoClicker(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       widget_frame_clicker = tk.Frame(self, bg='gray')
       widget_frame_clicker.pack(side="top", fill="both", expand=True)

class AutoScroll(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       widget_frame_scroll = tk.Frame(self, bg='white')
       widget_frame_scroll.pack(side="top", fill="both", expand=True)


class AutoFisher(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       widget_frame_fisher = tk.Frame(self, bg='gray')
       widget_frame_fisher.pack(side="top", fill="both", expand=True)


class Settings(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       widget_frame_setting = tk.Frame(self, bg='white')
       widget_frame_setting.pack(side="top", fill="both", expand=True)

# class switch_bg_color(btn_bg_color):
#     global btnState
#     def __init__(self, *args, **kwargs):
#         switch_bg_color.__init__(self,*args, **kwargs)
#         if btnState:
#             btn.config(bg='white', activebackground='white')
#             root.config(bg='white')
#             # txt.config(text="Dark Mode off!", bg='white')
#             btnState = False
#         else:
#             btn.config(bg='black', activebackground='black')
#             root.config(bg='black')
#             # txt.config(text="Dark Mode on!", bg='black')
#             btnState = True
#
#     btn = tk.Button()
#


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = AutoClicker(self)
        p2 = AutoScroll(self)
        p3 = AutoFisher(self)
        p4 = Settings(self)

        sidebar = ttk.Frame(self,  relief="sunken", borderwidth=2)
        container = tk.Frame(self)
        sidebar.pack(side="left", fill="y", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(sidebar, text="AutoClicker", command=p1.show)
        b2 = tk.Button(sidebar, text="AutoScroll", command=p2.show)
        b3 = tk.Button(sidebar, text="AutoFisher", command=p3.show)
        b4 = tk.Button(sidebar, text="Day/Night")
        b5 = tk.Button(sidebar, text="Settings", command=p4.show)

        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")
        b5.pack(side="bottom")
        b4.pack(side="bottom")

        p1.show()



if __name__ == "__main__":
    root = tk.Tk()
    root.title('Pigorscho`s Minecraft Tools')
    root.resizable(width=False, height=False)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("700x500")
    btnState = False
    root.mainloop()