import requests
import customtkinter as tk

class App(tk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.r = requests.get('https://raw.githubusercontent.com/w1n4a/CTkPlus/refs/heads/main/wget-json.json').json()

        self.geometry('700x500')
        self.title('wget')
        self.resizable(False,False)

        self.label = tk.CTkLabel(self,text='WGET',fg_color='#3B8ED0',height=50,font=('JetBrains Mono',30))
        self.label.pack(fill='x')

        self.frame = tk.CTkScrollableFrame(self)
        self.frame.pack(expand=True,fill='both')

        self.upd()

        tk.set_appearance_mode('light')

    def upd(self):
        rows,col = 0,0
        for ind,name in enumerate(self.r):
            if ind % 3 == 0:
                rows += 1
                col = 0
            else:
                col += 1

            self.item = tk.CTkFrame(self.frame,height=200,width=200,fg_color='#DDE2E5')
            self.item.grid(column=col,row=rows,padx=5,pady=5)
            self.item.pack_propagate(False)

            self.name = tk.CTkLabel(self.item,text=name,text_color='black',font=('JetBrains Mono',15))
            self.name.pack(fill='x')

            self.disc = tk.CTkTextbox(self.item,text_color='black',font=('JetBrains Mono',12),height=125,corner_radius=0,wrap='word')
            self.disc.pack()
            self.disc.insert('1.0', self.r[name])
            self.disc.configure(state='disabled')

            self.code = tk.CTkTextbox(self.item,text_color='#4078F2',font=('JetBrains Mono',10),corner_radius=0,wrap='word')
            self.code.pack(fill='x')
            self.code.insert('1.0', f'from ctkplus import {name}')
            self.code.configure(state='disabled')

if __name__ == '__main__':
    App().mainloop()
