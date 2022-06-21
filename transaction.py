import imp
import os
from operator import mod
from tkinter import *
import qrcode
from PIL import Image, ImageTk, ImageDraw, ImageFont
from resizeimage import resizeimage
# from matplotlib.pyplot import title
# import Scanner
import random
import pandas as pd
from scipy import rand
from fpdf import FPDF
from datetime import datetime
from tkPDFViewer import tkPDFViewer as pdf
from pdf2image import convert_from_path
global fileCSV
fileCSV = pd.read_csv('transaction_history.csv')
type(fileCSV)


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
        self.var_amount = IntVar()
        self.pincode = IntVar()
        self.var_amount.set('')
        self.pincode.set('')
        global loc
        loc = 'C:\\Users\\Shayan\\OneDrive\\Desktop\\Coding prac\\receipt'
        # updateCsv = pd.DataFrame([[self.pincode, self.var_amount]])
        # self.var_acc_no = StringVar()
        # Bank details here

        tf_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        tf_frame.place(x=50, y=100, width=500, height=380)
        tf_title = Label(tf_frame, text="    Transaction details: ", font=(
            "goudy old style", 20), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)
        lbl_amount = Label(tf_frame, text="   Enter Amount : ", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=18, y=60)
        lbl_Pin_code = Label(tf_frame, text="    Pin Code : ", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=18, y=120)
        # lbl_owner_name = Label(tf_frame, text="    Owner name: ", font=(
        # "times new roman", 15, 'bold'), bg='white').place(x=18, y=180)

        txt_amount = Entry(tf_frame, font=(
            "times new roman", 15), textvariable=self.var_amount, bg='light yellow').place(x=220, y=60)
        txt_pincode = Entry(tf_frame, show="*", font=(
            "times new roman", 15), textvariable=self.pincode, bg='light yellow').place(x=220, y=120)
        # self.var_amount = self.var_amount + txt_amount
        # self.pincode = self.pincode + int(txt_pincode)
        # txt_owner_name = Entry(tf_frame, font=(
        # "times new roman", 15), textvariable=self.var_user_name, bg='light yellow').place(x=220, y=180)

        btn_transact = Button(tf_frame, text='Withdraw Cash', command=self.print_details, font=(
            'times new roman', 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=250, height=30, width=200)
        btn_clear = Button(tf_frame, text='Clear', command=self.clear, font=(
            'times new roman', 18, 'bold'), bg='white', fg='red').place(x=300, y=250, height=30, width=90)

        self.msg = 'Please Enter the Amount!'
        self.lbl_msg = Label(tf_frame, text=self.msg, font=(
            "times new roman", 20, 'bold'), bg='white')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # PDF display goes here
        pdf_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        pdf_frame.place(x=520, y=100, width=250, height=380)
        # pdf_title = Label(pdf_frame, text=" Receipt ", font=(
        #   "goudy old style", 20, ), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)
        # self.qr_code = Label(pdf_frame, text='Please Make a transaction', font=(
        #    "times new roman", 12), bg='#3f51b5', fg='white')
        #self.qr_code.place(x=35, y=100, width=180, height=180)

        self.canvas = Canvas(pdf_frame, width=250, height=380)
        self.canvas.pack()

    def clear(self):
        self.var_amount.set('')
        self.pincode.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.canvas.delete(imgon)

    def print_details(self):
        isSuccess = False
        global bank_balance

        pincode = self.pincode.get()
        filename = 'transaction_history.csv'
        df = pd.read_csv(filename)
        pCode = df['Pincode'].tolist()
        amt = df['Balance'].tolist()
        if self.pincode.get() not in pCode:
            bank_balance = random.randrange(0, 100000)
            updateCsv = pd.DataFrame([[pincode, bank_balance]])
            updateCsv.to_csv('transaction_history.csv',
                             mode='a', index=False, header=False)
        else:
            for index, value in enumerate(pCode):
                if self.pincode.get() == value:
                    bank_balance = amt.__getitem__(index)

        if self.var_amount.get() > bank_balance:
            self.msg = 'Your Balance is Low!'
            self.lbl_msg.config(text=self.msg, fg='red')
        elif len(str(self.pincode.get())) > 6:
            self.msg = 'PinCode cannot exceed 6 characters'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            print('Bank balance : ' + str(bank_balance))
            bank_balance = bank_balance - self.var_amount.get()
            print(self.var_amount.get())
            print(self.pincode.get())
            print('Transaction is : ' + str(bank_balance))
            self.msg = 'Transaction Successful!'
            self.lbl_msg.config(text=self.msg, fg='green')
            isSuccess = True
        if isSuccess:
            self.receipt_gen()

    def receipt_gen(self):
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)

        # create a cell
        # amount=self.var_amount
        success_msg = "THANK YOU"
        fail_msg = "Sorry! Transaction failed"

        pdf.cell(200, 10, txt="Transaction amount : "+str(self.var_amount.get()),
                 ln=1, align='C')

        # add another cell
        pdf.cell(200, 10, txt="Transaction Time: "+str(datetime.now()),
                 ln=2, align='C')
        pdf.cell(200, 10, txt="Remaining Balance : " +
                 str(bank_balance), ln=3, align='C')
        pdf.cell(200, 10, txt="Thank You", ln=4, align='C')
        # saving the unique pdf with name .pdf
        global rand_subscript
        rand_subscript = random.randint(0, 1000)
        global pdf_name
        pdf_name = "receipt"+str(rand_subscript)+".pdf"
        pdf.output(pdf_name)
        filename = 'receipt_img.jpg'
        fnt = ImageFont.truetype('arial.ttf', 17)
        paymentImage = Image.new(mode="RGB", size=(370, 370), color="white")
        draw = ImageDraw.Draw(paymentImage)
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S\n%d/%m/%Y")
        draw.text((10, 10), "Transaction Amount : " +
                  str(self.var_amount.get()), font=fnt, fill=(0, 0, 0))

        draw.text((10, 60), "Transaction Time: " + str(dt_string),
                  font=fnt, fill=(0, 0, 0))
        draw.text((10, 110), "Remaining Balance : " +
                  str(bank_balance), font=fnt, fill=(0, 0, 0))
        draw.text((10, 160), "Thank You!", font=fnt, fill=(0, 0, 0))
        paymentImage.save(filename)
        # os.system(filename)
        #self.im = ImageTk.PhotoImage(filename)
        self.img = ImageTk.PhotoImage(Image.open("receipt_img.jpg"))
        global imgon
        imgon = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        # self.qr_code.config(image=self.im)


root = Tk()
obj = Transaction(root)
root.mainloop()
