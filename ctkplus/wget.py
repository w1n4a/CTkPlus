import requests
import customtkinter as tk

class App(tk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.r = requests.get('https://raw.githubusercontent.com/w1n4a/CTkPlus/refs/heads/main/wget-json.json').json()

        self.geometry('700x500')
        self.title('wget')
        self.resizable(False,False)

        self.label = tk.CTkLabel(self,text='WGET',fg_color='#3B8ED0',height=50,font=('Segoe UI',30))
        self.label.pack(fill='x')

        self.frame = tk.CTkScrollableFrame(self)
        self.frame.pack(expand=True,fill='both')

        self.upd()

    def upd(self):
        rows,col = 0,0
        for i in range(len(self.r)):
            if i % 3 == 0:
                rows += 1
                col = 0
            else:
                col += 1

            self.item = tk.CTkFrame(self.frame,fg_color='white')
            self.item.grid(column=col,row=rows,padx=5,pady=5)

if __name__ == '__main__':
    App().mainloop()
