import customtkinter as tk

class CTkEntryButton(tk.CTkFrame):
    def __init__(self, master, command=None, text='', placeholder_text=None, placeholder_text_color=None, width=140, height=28, border_width=1, bg_color="transparent", fg_color="transparent", entry_fg_color=None, border_color=None, text_color=None, font=None, button_fg_color=None, button_hover_color=None, button_text_color=None, **kwargs):
        super().__init__(master, bg_color=bg_color,fg_color=fg_color, **kwargs)

        self.entry = tk.CTkEntry(self, width=width, height=height, corner_radius=0, border_width=border_width, bg_color="transparent", fg_color=entry_fg_color, border_color=border_color, text_color=text_color, placeholder_text_color=placeholder_text_color, font=font, placeholder_text=placeholder_text)
        self.entry.pack(side='left')

        self.button = tk.CTkButton(self, width=20, text=text, font=('Arial', 15), corner_radius=0, border_width=border_width, border_color=border_color, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=command)
        self.button.pack(side='left', fill='y')

    def get(self):
        return self.entry.get()

class CTkSpinBox(tk.CTkFrame):
    def __init__(self, master, command=lambda *args: None, step=1, range=('inf','inf'), start_num=0, width=140, height=28, border_width=1, bg_color="transparent", fg_color="transparent", entry_fg_color=None, border_color=None, text_color=None, font=None, button_fg_color=None, button_hover_color=None, button_text_color=None, **kwargs):
        super().__init__(master, bg_color=bg_color, fg_color=fg_color, **kwargs)

        self.range = range

        self.string = tk.StringVar(value=str(start_num))
        self.string.trace_add('write',command)

        self.entry = tk.CTkEntry(self, width=width, height=height, corner_radius=0, border_width=border_width, bg_color="transparent", fg_color=entry_fg_color, border_color=border_color, text_color=text_color, font=font, textvariable=self.string)
        self.entry.pack(side='left')

        self.frame = tk.CTkFrame(self)
        self.frame.pack(side='left')

        self.button = tk.CTkButton(self.frame, width=15, height=self.entry._current_height/2, text='▲', font=('Impact', 5, 'bold'), bg_color='transparent', corner_radius=0, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=lambda: self.plus(step))
        self.button.pack(side='top',pady=0)

        self.button2 = tk.CTkButton(self.frame, width=15, height=self.entry._current_height/2, text='▼', font=('Impact', 5, 'bold'), bg_color='transparent', corner_radius=0, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=lambda: self.minus(step))
        self.button2.pack(side='bottom',pady=0)

    def plus(self, *args: any):
        try:
            r = self.string.get()
            if self.range[1] == 'inf' or int(r) + sum(args) <= self.range[1]:
                self.string.set(str(int(r)+sum(args)))
                return self.string.get()
            else:
                self.string.set(self.range[1])
                return self.string.get()
        except:
            raise TypeError

    def minus(self, *args: any):
        try:
            r = self.string.get()
            if self.range[0] == 'inf' or int(r) - sum(args) >= self.range[0]:
                self.string.set(str(int(r)-sum(args)))
                return self.string.get()
            else:
                self.string.set(self.range[0])
                return self.string.get()
        except:
            raise TypeError

    def get(self):
        return self.string.get()

    def set(self, pos: int):
        if type(pos) == type(1):
            self.string.set(str(pos))
            return self.string.get()
        else:
            raise TypeError()

class CTkEntry(tk.CTkEntry):
    def __init__(self, master, command_type = 'write', text='', width = 140, height = 28, corner_radius = None, border_width = 1, bg_color = "transparent", fg_color = None, border_color = None, text_color = None, placeholder_text_color = None, placeholder_text = None, font = None, command=lambda *args: None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, text_color, placeholder_text_color, placeholder_text, font, **kwargs)

        self.string = tk.StringVar(value=text)
        self.string.trace_add(command_type,command)
        self.configure(textvariable=self.string)

class CTkSelector(tk.CTkFrame):
    def __init__(self, master, current=0, values=[], command=lambda *args: None, width=140, height=28, border_width=1, bg_color="transparent", fg_color="transparent", entry_fg_color=None, border_color=None, text_color=None, font=None, button_fg_color=None, button_hover_color=None, button_text_color=None, **kwargs):
        super().__init__(master,bg_color=bg_color,fg_color=fg_color)

        self.cur = current
        self.val = list(map(str,values))

        self.string = tk.StringVar(value=self.val[self.cur])
        self.string.trace_add('write',command)

        self.entry = tk.CTkEntry(self, width=width, height=height, corner_radius=0, border_width=border_width, bg_color="transparent", fg_color=entry_fg_color, border_color=border_color, text_color=text_color, font=font, textvariable=self.string, state='disabled')
        self.entry.pack(side='left')

        self.frame = tk.CTkFrame(self)
        self.frame.pack(side='left')

        self.button = tk.CTkButton(self.frame, width=15, height=self.entry._current_height/2, text='▲', font=('Impact', 5, 'bold'), corner_radius=0, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=lambda: self.up(1))
        self.button.pack(side='top',pady=0)

        self.button2 = tk.CTkButton(self.frame, width=15, height=self.entry._current_height/2, text='▼', font=('Impact', 5, 'bold'), corner_radius=0, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=lambda: self.down(1))
        self.button2.pack(side='bottom',pady=0)

    def up(self, args: int):
        for i in range(args):
            if (self.cur + 1) < len(self.val):
                self.cur += 1
                self.string.set(self.val[self.cur])
            else:
                self.cur = 0
                self.string.set(self.val[self.cur])

        return self.string.get()

    def down(self, args: int):
        for i in range(args):
            if (self.cur - 1) > -1:
                self.cur -= 1
                self.string.set(self.val[self.cur])
            else:
                self.cur = len(self.val)-1
                self.string.set(self.val[self.cur])

        return self.string.get()

    def set(self, pos: int):
        if type(pos) == type(1) and pos < len(self.val):
            self.cur = pos
            self.string.set(self.val[self.cur])
            return self.string.get()
        else:
            raise TypeError()

    def get(self):
        return self.string.get()

class CTkMultiList(tk.CTkFrame):
    def __init__(self, master, text='', values=[], command=lambda: None, width=200, height=150, fg_color=None, text_color='white', label_fg_color='transparent', checkbox_fg_color=None, checkbox_hover_color=None, border_width=1, border_color=None, checkbox_text_color='white', **kwargs):
        super().__init__(master=master, width=width, height=height, fg_color=fg_color, **kwargs)

        self.checkbox_fg_color = checkbox_fg_color
        self.checkbox_hover_color = checkbox_hover_color
        self.checkbox_text_color = checkbox_text_color

        self.pack_propagate(False)

        self.result = []
        self.values = values
        self.command = command

        self.label = tk.CTkLabel(self, text=text, text_color=text_color, fg_color=label_fg_color,border_color=border_color, border_width=border_width)
        self.label.pack(fill='x')

        self.slideframe = tk.CTkScrollableFrame(self, fg_color=fg_color, scrollbar_fg_color='transparent', border_color=border_color, border_width=border_width, scrollbar_button_color=fg_color, scrollbar_button_hover_color=fg_color)
        self.slideframe.pack(pady=2)

        self.update()

    def update(self):
        for i in self.slideframe.winfo_children():
            i.destroy()
        for i in self.values:
            a = tk.CTkCheckBox(self.slideframe,text=i)
            a = tk.CTkCheckBox(self.slideframe, text=i, fg_color=self.checkbox_fg_color, hover_color=self.checkbox_hover_color, text_color=self.checkbox_text_color)
            a.pack(pady=2)

    def get(self):
        return self.result

    def change(self, name: str, act: str):
        if act == 1 or act == 'add':
            self.result.append(name)
        elif act == 0 or act == 'remove':
            self.result.remove(name)
        else:
            raise ValueError(f'Invalid action: {act}')

        self.command()
