from tkinter import *

window = Tk()
window.geometry('360x360')
window.title('Крестики и нолики')

w = 120
xod = 0
Button_list = []
kre_num = []
li_way = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


class Btn():
    global w, Button_list

    def __init__(self, x0, y0, idd):
        self.idd = idd
        self.x0 = x0
        self.y0 = y0
        self.Button1 = Button(bg='green', bd=10, fg='white', font=('Comic Sans MS', 24, 'bold'))
        self.Button1.place(x=self.x0, y=self.y0, width=w, height=w)
        self.Button1.bind('<Button-1>', self.click)

    def unbind1(self, event):
        self.Button1.unbind('<Button-1>')

    def cfg(self):
        self.Button1.config(fg='blue')

    def show(self):
        idd = 0
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                Button_list.append(Btn(x, y, idd))
                x += w
                idd += 1
            x = 0
            y += w

    def click(self, event):
        print(self.idd)
        global xod, li_way, kre_num
        win = False
        if xod % 2 == 0:
            char = 'X'
            kre_num.append(self.idd)
        else:
            char = '0'
        self.Button1.config(text=char)
        xod += 1
        # Проверка
        k = 0
        for i in range(8):
            for j in range(3):
                if li_way[i][j] in kre_num:
                    k += 1
            if k == 3:
                print('norm')
                win = True
                break
            else:
                k = 0
        self.Button1.unbind('<Button-1>')
        if win:
            for g in range(9):
                Button_list[g].unbind1('<Button-1>')
            for g in range(3):
                Button_list[li_way[i][g]].cfg()


Btn.show(0)
window.mainloop()