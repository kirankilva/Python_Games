#Importing libraries
from tkinter import *
import random
from tkinter import messagebox as msg

#Code goes from here
class NumberGuess:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400+500+100')
        self.root.title('Number Guessing Game')

    #All variables
        val = 0
        self.num_var = IntVar()
        self.chance_var = IntVar()
        self.from_var = IntVar()
        self.to_var = IntVar()
        self.res_var = StringVar()

        self.chance_var.set(5)
        self.res_var.set('Hello User!..')

    #Title
        Label(self.root, text='NUMBER GUESSING GAME', width=30, height=1, font=('Times New Roman',15,'bold')).place(x=10, y=10)

        #Enter the number label
        num_lbl = Label(self.root, text='Enter the number : ', width=15, height=1, font=('Times New Roman',11))
        num_lbl.place(x=25, y=100)

        num_entry = Entry(self.root, width=10, background='white', bd=1, textvariable=self.num_var)
        num_entry.place(x=145, y=103)

        #Chances label
        chance_lbl = Label(self.root, text='Chances left : ', width=15, height=1, font=('Times New Roman',11))
        chance_lbl.place(x=35, y=160)

        chance_entry = Entry(self.root, width=10, background='white', bd=1, textvariable=self.chance_var)
        chance_entry.place(x=145, y=163)

        #Result label
        res_lbl = Label(self.root, text='Result will appear here : ', width=20, height=1, font=('Times New Roman',11))
        res_lbl.place(x=20, y=220)

        res_entry = Entry(self.root, width=55, background='white', bd=1, textvariable=self.res_var)
        res_entry.place(x=30, y=245)

        #Range from
        from_lbl = Label(self.root, text='From : ', width=5, height=1, font=('Times New Roman',11))
        from_lbl.place(x=250, y=100)

        from_entry = Entry(self.root, width=10, background='white', bd=1, textvariable=self.from_var)
        from_entry.place(x=300, y=103)

        #Range to
        to_lbl = Label(self.root, text='To : ', width=5, height=1, font=('Times New Roman',11))
        to_lbl.place(x=255, y=160)

        to_entry = Entry(self.root, width=10, background='white', bd=1, textvariable=self.to_var)
        to_entry.place(x=300, y=163)

        #Designer
        Label(self.root, text="designed by", fg="grey").place(x=170, y=360)
        Label(self.root, text="KIRAN KILVA", font="Helvetica 10").place(x=165, y=378)

    #buttons
        #Start button
        start_btn = Button(self.root, text='S T A R T', width=10, bd=1, bg='orange', activebackground='orange', fg='white', activeforeground='black', font=('',9,'bold'), cursor='hand2', command=self.start_func)
        start_btn.place(x=30, y=300)

        #Reset button
        reset_btn = Button(self.root, text='R E S E T', width=10, bd=1, bg='blue', activebackground='blue', fg='white', activeforeground='black', font=('',9,'bold'), cursor='hand2', command=self.reset_func)
        reset_btn.place(x=115, y=300)

        #Guess button
        guess_btn = Button(self.root, text='G U E S S', width=10, bd=1, bg='green', activebackground='green', fg='white', activeforeground='black', font=('',9,'bold'), cursor='hand2', command=self.guess_func)
        guess_btn.place(x=200, y=300)

        #Clear button
        clear_btn = Button(self.root, text='E X I T', width=10, bd=1, bg='grey', activebackground='grey', fg='white', activeforeground='black', font=('',9,'bold'), cursor='hand2', command=self.exit_func)
        clear_btn.place(x=285, y=300)
        

    #Start button function
    def start_func(self):
        try:
            if (self.from_var.get() == 0 and self.to_var.get() == 0) or (self.from_var.get() == '' and self.to_var.get() == ''):
                msg.showwarning('Warning', 'Please select the range.')
            else:
                self.res_var.set(f'Guess the Number between {self.from_var.get()} and {self.to_var.get()}')
                global val
                num = random.randint(self.from_var.get(), self.to_var.get())
                val = num
        except:
            msg.showerror('ERROR', 'Invalid Entries. Please try again')

            
    #Reset button function  
    def reset_func(self):
        self.num_var.set(0)
        self.chance_var.set(5)
        self.from_var.set(0)
        self.to_var.set(0)
        self.res_var.set('Hello User!..')

    #Guess button function
    def guess_func(self):
        if self.res_var.get() == 'Hello User!..':
            msg.showwarning('WARNING', 'Please click the START button')
        else:
            if self.num_var.get() > val:
                self.res_var.set(f'Wrong!. {self.num_var.get()} is Greater than the Number')
            elif self.num_var.get() < val:
                self.res_var.set(f'Wrong!. {self.num_var.get()} is Less than the Number')
            else:
                self.res_var.set('Congragulations!.. You WON the game')
                ans = msg.askquestion('Congragulations', 'You Won the game!!\nDo you want to play again?')
                if ans == 'yes':
                    self.reset_func()
                    self.chance_var.set(self.chance_var.get()+1)
                else:
                    self.root.destroy()
            
            self.chance_var.set(self.chance_var.get()-1)
            if self.chance_var.get() == 0:
                msg.showinfo('BETTER LUCK NEXT TIME', 'Sorry!! You Lost The Game')
                self.reset_func()
            
    #Exit button function
    def exit_func(self):
        ask = msg.askquestion('EXIT', 'Do you really want to exit the game?')
        if ask == 'yes':
            self.root.destroy()


            
root = Tk()
obj = NumberGuess(root)
root.mainloop()
