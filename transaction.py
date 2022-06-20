import imp
from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
#from matplotlib.pyplot import title
#import Scanner


class Transaction:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("Transaction System!")
        self.root.resizable(False, False)
        nameVar = open("name_str.txt", "r")
        title = Label(self.root, text="     Welcome " + (nameVar.read()), font=(
            "times new roman", 40), bg='#4A1474', fg='white', anchor='w').place(x=0, y=0, relwidth=1)

        # variables
        self.var_bank_name = StringVar()
        self.var_user_name = StringVar()
        self.var_acc_no = StringVar()
        # Bank details here

        bank_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        bank_frame.place(x=50, y=100, width=500, height=380)
        bank_title = Label(bank_frame, text="    Bank Details: ", font=(
            "goudy old style", 20), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)
        lbl_bank_acc = Label(bank_frame, text="    Account Number: ", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=18, y=60)
        lbl_bank_name = Label(bank_frame, text="    Bank Name: ", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=18, y=120)
        lbl_owner_name = Label(bank_frame, text="    Owner name: ", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=18, y=180)

        txt_bank_acc = Entry(bank_frame, font=(
            "times new roman", 15), textvariable=self.var_acc_no, bg='light yellow').place(x=220, y=60)
        txt_bank_name = Entry(bank_frame, font=(
            "times new roman", 15), textvariable=self.var_bank_name, bg='light yellow').place(x=220, y=120)
        txt_owner_name = Entry(bank_frame, font=(
            "times new roman", 15), textvariable=self.var_user_name, bg='light yellow').place(x=220, y=180)

        btn_generate = Button(bank_frame, text='Generate QR code', command=self.generate, font=(
            'times new roman', 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=250, height=30, width=200)
        btn_clear = Button(bank_frame, text='Clear', command=self.clear, font=(
            'times new roman', 18, 'bold'), bg='white', fg='red').place(x=300, y=250, height=30, width=90)

        self.msg = ''
        self.lbl_msg = Label(bank_frame, text=self.msg, font=(
            "times new roman", 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # Qr window goes here
        Qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Qr_frame.place(x=520, y=100, width=250, height=380)
        Qr_title = Label(Qr_frame, text="Account QR code: ", font=(
            "goudy old style", 20, ), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)
        self.qr_code = Label(Qr_frame, text='QR Unavailable', font=(
            "times new roman", 15), bg='#3f51b5', fg='white')
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_bank_name.set('')
        self.var_user_name.set('')
        self.var_acc_no.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_acc_no.get() == '' or self.var_bank_name.get() == '' or self.var_user_name.get() == '':
            self.msg = 'All fields required!'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr_data = (
                f"Account num : {self.var_acc_no.get()}\nUser name : {self.var_user_name.get()}\nBank Name : {self.var_bank_name.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])

            # qr image update

            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            # update notif

            self.msg = 'QR Generated Successfully!'
            self.lbl_msg.config(text=self.msg, fg='green')


root = Tk()
obj = Transaction(root)
root.mainloop()
