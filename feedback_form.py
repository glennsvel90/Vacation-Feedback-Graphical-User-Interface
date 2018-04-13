from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import smtplib


class FeedbackApp:


    def __init__(self, master):


        master.title('California Vacation Feedback')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font=('Helvetica',11))
        self.style.configure('Header.TLabel',font=('Helvetica',18, 'bold'))

        self.frameheader = ttk.Frame(master)
        self.frameheader.pack()

        self.logo = PhotoImage(file ='/home/ubun/Dropbox/dropubun/Vacation-Feedback-Graphical-User-Interface/tour_logo.gif')

        ttk.Label(self.frameheader, image = self.logo).grid(row = 0, column= 0, rowspan= 3, padx=(15, 0))
        ttk.Label(self.frameheader,text='Thank You For Vacationing With Us!', style= 'Header.TLabel').grid(row=0, column=1, pady= 5, padx=(3, 15))
        ttk.Label(self.frameheader, wraplength=400,
                  text=("We would like to improve our future services to you.\n "
                        "To do so, please fill out this feedback form. \n "
                        "We greatly appreciate all that you do!"),
                  justify = CENTER).grid(row=1, column=1, padx=(0,40), pady=(0, 15))


        self.framebody = ttk.Frame(master)
        self.framebody.pack()



        ttk.Label(self.framebody, text= 'Name:').grid(row=0, column=0, padx= 5, sticky='sw')
        ttk.Label(self.framebody, text= 'Email:').grid(row=0, column=1, padx= 5, sticky='sw')
        ttk.Label(self.framebody, text= 'Comments:').grid(row=2, column= 0, padx=5,pady= (5,0), sticky='sw')


        self.entry_name = ttk.Entry(self.framebody, width=27, font=('Helvetica', 10))
        self.entry_email = ttk.Entry(self.framebody, width=27, font=('Helvetica', 10))
        self.textbox_comments = Text(self.framebody, width=57, height=10, font=('Helvetica', 10))

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.textbox_comments.grid(row=3, column=0, padx=5, columnspan=2)


        ttk.Button(self.framebody, text='Submit', command=self.submit).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        #
        # self.SERVER = "localhost"
        #
        # self.FROM = "california@vacations.com"
        # self.TO = ["sonyericson718@gmail.com"] # must be a list
        #
        # self.SUBJECT = "Feedback from {}".format(self.entry_name.get())
        #
        # self.TEXT = 'Name: {}\n'.format(self.entry_name.get()),\
        #             'Email: {}\n'.format(self.entry_email.get()),\
        #             'Comment: {}\n'.format(self.textbox_comments.get(1.0, 'end'))
        #
        # # Prepare actual message
        #
        # self.message = """\
        #             From: {}
        #             To: {}
        #             Subject: {}
        #
        #             {}
        #             """.format(self.FROM, ", ".join(self.TO), self.SUBJECT, self.TEXT)
        #
        # # Send the mail
        #
        # self.server = smtplib.SMTP(self.SERVER)
        # self.server.sendmail(self.FROM, self.TO, message)




    def submit(self):
        print('Feedback Form has been submitted ')
        # 'Name: {}'.format(self.entry_name.get()),
        # 'Email: {}'.format(self.entry_email.get()),
        # 'Comment: {}'.format(self.textbox_comments.get(1.0,END)))

        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comment: {}'.format(self.textbox_comments.get(1.0, 'end')))


        self.clear()

        messagebox.showinfo(title= 'Feedback Form has been submitted',
                            message=('Feedback Form has been submitted. Thank you so much!'))

    def clear(self):
        self.textbox_comments.delete('1.0', 'end')
        self.entry_email.delete(0, END)
        self.entry_name.delete(0, END)


        self.server.quit()


def main():

    root = Tk()

    app = FeedbackApp(root)

    root.mainloop()



if __name__ == "__main__": main()
