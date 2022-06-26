import tkinter as tk
from tkinter import ttk


class Example():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoClicker GUI")

        # click interval widget
        self.click_interval = tk.Frame(self.root, bg="red", height=75)
        hours_input = tk.Entry(self.click_interval, width=5)
        mins_input = tk.Entry(self.click_interval, width=5)
        secs_input = tk.Entry(self.click_interval, width=5)
        millisecs_input = tk.Entry(self.click_interval, width=5)

        click_intervall_label = tk.Label(self.click_interval, text='Click Intervall :')

        hours_label = tk.Label(self.click_interval, text='hours')
        mins_label = tk.Label(self.click_interval, text='mins')
        secs_label = tk.Label(self.click_interval, text='secs')
        millisecs_label = tk.Label(self.click_interval, text='milliseconds')

        click_intervall_label.grid(row=1, column=1)
        hours_input.grid(row=2, column=1)
        hours_label.grid(row=2, column=2)
        mins_input.grid(row=2, column=3)
        mins_label.grid(row=2, column=4)
        secs_input.grid(row=2, column=5)
        secs_label.grid(row=2, column=6)
        millisecs_input.grid(row=2, column=7)
        millisecs_label.grid(row=2, column=8)

        self.click_interval.pack(fill='both', expand=True)



        # center click options
        self.center_click_options = tk.Frame(self.root, width=150, height=75, bg="cyan")
        ## click options
        self.click_options = tk.Frame(self.center_click_options, width=150, height=75, bg='yellow')
        ## click repeat
        self.click_repeat = tk.Frame(self.center_click_options, width=150, bg='green')
        ### click options content
        click_options_header_label = tk.Label(self.click_options, text='Click Options :')
        click_options_header_label.grid(row=0, column=1)

        mouse_button_label = tk.Label(self.click_options, text='Mouse Button :')
        mouse_button_label.grid(row=2, column=1)

        mouse_button_combo_box = ttk.Combobox(self.click_options, values=['Left',
                                                                          'Right',
                                                                          'Mousewheel'])
        mouse_button_combo_box.grid(row=2, column=2)
        mouse_button_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)
        click_type_header_label = tk.Label(self.click_options, text='Click Type :')
        click_type_header_label.grid(row=3, column=1)

        click_type_combo_box = ttk.Combobox(self.click_options, values=['Single',
                                                                        'Double'])
        click_type_combo_box.grid(row=4, column=2)
        click_type_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)

        click_type_label = tk.Label(self.click_options, text='Mouse Button :')
        click_type_label.grid(row=4, column=1)

        self.click_options.pack(side="left", fill="both", expand=True)
        self.click_repeat.pack(side="right", fill="both", expand=True)



        # makro
        self.makro = tk.Frame(self.root, width=200, height=250, bg='blue')




        # special eff
        self.special_effects = tk.Frame(self.root, width=150, height=60, bg='orange')




        self.click_interval.grid(row=0, columnspan=2, rowspan=1, sticky='ew')
        self.center_click_options.grid(row=1, column=1, rowspan=2, sticky='nsew')
        self.makro.grid(row=0, column=2, rowspan=3, sticky='nsew')
        self.special_effects.grid(row=3, columnspan=3, rowspan=1, sticky='ew')



        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


        self.root.mainloop()


Example()