from tkinter import Button, Entry, Frame, Label, OptionMenu, StringVar, Tk, messagebox
from Email import Email
from Email_GUI import Email_GUI

class Authentication:
    def __init__(self, master):
        self.frame = Frame(master)
        master.minsize(width=150, height=150)
        master.config(bg='yellow')
        master.title('Login')
        self.title = Label(master, text = 'PyMail Authentication', font = ("Century Gothic", 40), fg = 'black', bg = 'red')
        self.title.pack()
        
        text1 = 'Login to the email system! \nSupported Services: Gmail, Outlook, Yahoo'
        self.detail = Label(master, text = text1, font = ("Century Gothic", 15), fg = 'black', bg = 'green')
        self.detail.pack()


        #email Client
        self.client = StringVar(master)
        self.client.set('Choose One')
        #option to choose across various platforms 
        self.w = OptionMenu(master, self.client, 'Choose One', 'Gmail', 'Outlook', 'Yahoo')
        self.w.pack()
        
        
        #Username
        self.rec_title = Label(master, text = '\nEmail Address/Username', font = ("Century Gothic", 18), bg = 'cyan')
        self.rec_title.pack()
        self.rec_email = Entry(master, width = 40)
        self.rec_email.pack()
        
        
        #Password
        self.password_title = Label(master, text = '\nPassword', font = ("Century Gothic", 18), bg = 'cyan')
        self.password_title.pack()
        self.password_entry = Entry(master, show='*', width = 40)
        self.password_entry.pack()
        
        
        #button
        self.button = Button(master, text='Authenticate', command = self.make_connection)
        self.button.pack()
        master.bind("<Return>", self.make_connection) # click handler when user presses Enter(Return) key
        self.master = master

    def make_connection(self):
        client = self.client.get()
        if client == 'Choose One': # user didn't select an email client from the dropdown
            messagebox.showerror('Invalid Email Client.' ,'Please choose a valid email client.')
        else:
            user = self.rec_email.get()
            password = self.password_entry.get()

            connect = Email(user, password, client)
            x = connect.login()

            if x != False and client != 'Choose One':
                messagebox.showinfo('Connection Successful!', f'Connected to: \n{user}\nOK to proceed')
                self.master.destroy()
                root = Tk()
                Email_GUI(root, connect)
            else:
                messagebox.showerror('Connection Fail, try again', 'Invalid Username, Password, or Client, Please Try Again.')
