import customtkinter as tk

class CTkEntryButton(tk.CTkFrame):
    def __init__(self, master, command=None, text='✔️', placeholder_text=None, bg_color="transparent", fg_color="transparent", **kwargs):
        super().__init__(master, bg_color=bg_color,fg_color=fg_color, **kwargs)
        
        self.entry = tk.CTkEntry(self, placeholder_text=placeholder_text)
        self.entry.pack(side='left')
        
        self.button = tk.CTkButton(self,width=5,text=text,font=('Classic',15),command=command)
        self.button.pack(padx=2,side='left')
        
    def get(self):
        return self.entry.get()
    
class CTkSpinBox(tk.CTkFrame):
    def __init__(self, master,command=lambda *args: None,step=1,range=(0,'inf'),start_num=0,bg_color="transparent", fg_color="transparent", **kwargs):
        super().__init__(master,bg_color=bg_color,fg_color=fg_color)
        
        self.range = range
        
        self.string = tk.StringVar(value=str(start_num))
        self.string.trace_add('write',command)
        
        self.entry = tk.CTkEntry(self,textvariable=self.string,corner_radius=0)
        self.entry.pack(side='left')
        
        self.frame = tk.CTkFrame(self)
        self.frame.pack(side='left')
        
        self.button = tk.CTkButton(self.frame,width=15,height=14,text='▲',font=('Impact',5,'bold'),corner_radius=0,command=lambda: self.plus(step))
        self.button.pack(side='top',pady=0)
        
        self.button2 = tk.CTkButton(self.frame,width=15,height=14,text='▼',font=('Impact',5,'bold'),corner_radius=0,command=lambda: self.minus(step))
        self.button2.pack(side='bottom',pady=0)
        
    def plus(self,*args):
        try:
            r = self.string.get()
            if self.range[1] == 'inf' or int(r) + sum(args) <= self.range[1]:
                self.string.set(str(int(r)+sum(args)))
                return self.string.get()
            else:
                self.string.set(self.range[1])
                return self.string.get()
        except:
            pass
    
    def minus(self, *args):
        try:
            r = self.string.get()
            if int(r) - sum(args) >= self.range[0]:
                self.string.set(str(int(r)-sum(args)))
                return self.string.get()
            else:
                self.string.set(self.range[0])
                return self.string.get()
        except:
            pass
        
    def get(self):
        return self.string.get()
    
    def set(self, pos: int):
        if type(pos) == type(1):
            self.string.set(str(pos))
            return self.string.get()
        else:
            return TypeError()
    
class CTkEntry(tk.CTkEntry):
    def __init__(self, master, width = 140, height = 28, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, text_color = None, placeholder_text_color = None, textvariable = None, placeholder_text = None, font = None, command=lambda *args: None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, text_color, placeholder_text_color, textvariable, placeholder_text, font, **kwargs)
        
        self.string = tk.StringVar()
        self.string.trace_add('write',command)
        self.configure(textvariable=self.string)
        
class CTkCelector(tk.CTkFrame):
    def __init__(self, master,current=0,values=[],command=lambda *args: None,start_num=0,bg_color="transparent", fg_color="transparent", **kwargs):
        super().__init__(master,bg_color=bg_color,fg_color=fg_color)
        
        self.cur = current
        self.val = list(map(str,values))
        
        self.string = tk.StringVar(value=self.val[self.cur])
        self.string.trace_add('write',command)
        
        self.entry = tk.CTkEntry(self,textvariable=self.string,corner_radius=0,state='disabled')
        self.entry.pack(side='left')
        
        self.frame = tk.CTkFrame(self)
        self.frame.pack(side='left')
        
        self.button = tk.CTkButton(self.frame,width=15,height=14,text='▲',font=('Impact',5,'bold'),corner_radius=0,command=lambda: self.up(1))
        self.button.pack(side='top',pady=0)
        
        self.button2 = tk.CTkButton(self.frame,width=15,height=14,text='▼',font=('Impact',5,'bold'),corner_radius=0,command=lambda: self.down(1))
        self.button2.pack(side='bottom',pady=0)
        
    def up(self, args):
        for i in range(args):
            if (self.cur + 1) < len(self.val):
                self.cur += 1
                self.string.set(self.val[self.cur])
            else:
                self.cur = 0
                self.string.set(self.val[self.cur])
            
        return self.string.get()
    
    def down(self, args):
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
            return TypeError()

    def get(self):
        return self.string.get()