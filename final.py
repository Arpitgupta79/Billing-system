from tkinter import *
from tkinter import ttk
import datetime
import os


date = datetime.date.today()
root = Tk()
root.title('RECEIPT APP')
root.configure(bg='#070F2B')
root.geometry("644x344")


def getvals():
    print("Submitting form")
    customer_data = {
        "Name": namevalue.get(),
        "Phone": phonevalue.get(),
        "ID": idvalue.get(),
        "Email": emailvalue.get(),
        "Payment Mode": paymentmodevalue.get()
    }
    print(customer_data)
    with open("records.txt", "a") as f:
        f.write(str(customer_data) + "\n")


def submit_close():
    getvals()
    root.destroy()
    on_closing()

Label(root, text="Welcome to abc shop", font="comicsansms 13 bold", pady=15, fg='white', bg='#070F2B').grid(row=0, column=3)

name = Label(root, text="Customer Name", bg='#070F2B', fg='white')
phone = Label(root, text="Customer  Phone Number", bg='#070F2B', fg='white')
id_label = Label(root, text="Customer ID (optional)", bg='#070F2B', fg='white')
email = Label(root, text="Email Address", bg='#070F2B', fg='white')
paymentmode = Label(root, text="Payment Mode", bg='#070F2B', fg='white')

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
id_label.grid(row=3, column=2)
email.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
idvalue = StringVar()
emailvalue = StringVar()
paymentmodevalue = StringVar()


nameentry = Entry(root, textvariable=namevalue, bg='#070F2B', fg='white')
phoneentry = Entry(root, textvariable=phonevalue, bg='#070F2B', fg='white')
identry = Entry(root, textvariable=idvalue, bg='#070F2B', fg='white')
emailentry = Entry(root, textvariable=emailvalue, bg='#070F2B', fg='white')
paymentmodeentry = Entry(root, textvariable=paymentmodevalue, bg='#070F2B', fg='white')

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
identry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

Button(root, text="Submit", bg='white', fg='#070F2B', command=submit_close).grid(row=7, column=3)

def  on_closing():
    win = Tk()
    win.title('DETAIL')
    win.configure(bg= '#070F2B')
    win.geometry("644x344")
    Label(win,text="Enter item details ", font="arial 13 bold", pady=15,fg='white',bg= '#070F2B').grid(row=0, column=3)
    def getitem():
        print("Submitting detail of item ")
        item_data = {
        "Item Name": itemvalue.get(),
        "Quantity": qtyvalue.get(),
        "Rate": ratevalue.get(),
        "GST": gstvalue.get()
        }
        print(item_data)

        with open("details.txt", "a") as g:
            g.write(str(item_data) + "\n")

    item = Label(win, text="Item Name",bg= '#070F2B',fg='white')
    qty = Label(win, text="Quantity",bg= '#070F2B',fg='white')
    rate= Label(win,text= "Rate(per pc's)",bg= '#070F2B',fg='white')
    gst = Label(win, text="GST (in %)",bg= '#070F2B',fg='white')

    item.grid(row=1, column=2)
    qty.grid(row=2, column=2)
    rate.grid(row=3, column=2)
    gst.grid(row=4, column=2)

    itemvalue = StringVar()
    qtyvalue = IntVar()
    ratevalue = IntVar()
    gstvalue = IntVar()

    itementry = Entry(win, textvariable=itemvalue,bg= '#070F2B',fg='white')
    qtyentry = Entry(win, textvariable=qtyvalue,bg= '#070F2B',fg='white')
    rateentry = Entry(win, textvariable=ratevalue,bg= '#070F2B',fg='white')
    gstentry = Entry(win, textvariable=gstvalue,bg= '#070F2B',fg='white')

    itementry.grid(row=1, column=3)
    qtyentry.grid(row=2, column=3)
    rateentry.grid(row=3, column=3)
    gstentry.grid(row=4, column=3)

    Button(win,text="Add item",bg= 'white',fg='#070F2B', command=getitem).grid(row=7, column=3)
    def next():
        win.destroy()
        final()
        
    Button(win,text="Next",command=next).grid(row=8,column=3)
    win.mainloop()


def final():
    import tkinter as tk
    from tkinter import ttk
    final=tk.Tk()
    
    final.attributes("-fullscreen",True)
    final.title("Final receipt")
    lbl = Label(final, bg='black')
    customer_frame = ttk.Frame(final, padding="20")
    customer_frame.pack(pady=20)
   
    screen_width=final.winfo_screenwidth()
    screen_height=final.winfo_screenheight()

    exitbutton=tk.Button(final,text='X',bg="red",width=4,command=final.destroy)
    exitbutton.place(x=screen_width-40,y=3)
    tk.Label(customer_frame, text="Customer Details", font=("Arial", 20), fg='black').grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(customer_frame, text="Customer Name:", font=("Arial", 14), fg='black').grid(row=1, column=0, sticky="e")
    tk.Label(customer_frame, text=namevalue.get(), font=("Arial", 14), fg='black').grid(row=1, column=1, sticky="w")

    tk.Label(customer_frame, text="Customer Phone:", font=("Arial", 14), fg='black').grid(row=2, column=0, sticky="e")
    tk.Label(customer_frame, text=phonevalue.get(), font=("Arial", 14), fg='black').grid(row=2, column=1, sticky="w")

    tk.Label(customer_frame, text="Customer ID:", font=("Arial", 14) ,fg='black').grid(row=3, column=0, sticky="e")
    tk.Label(customer_frame, text=idvalue.get(), font=("Arial", 14), fg='black').grid(row=3, column=1, sticky="w")

    tk.Label(customer_frame, text="Email:", font=("Arial", 14), fg='black').grid(row=4, column=0, sticky="e")
    tk.Label(customer_frame, text=emailvalue.get(), font=("Arial", 14), fg='black').grid(row=4, column=1, sticky="w")

    tk.Label(customer_frame, text="Date:", font=("Arial", 14), fg='black').grid(row=5, column=0, sticky="e")
    tk.Label(customer_frame, text=datetime.date.today(), font=("Arial", 14), fg='black').grid(row=5, column=1, sticky="w")

    tree_frame = ttk.Frame(final)
    tree_frame.pack(pady=10)
    columns = ("item_name", "qty", "rate", "amount", "sgst", "cgst", "amount_with_gst")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    tree.heading("item_name", text="Item Name")
    tree.heading("qty", text="Quantity")
    tree.heading("rate", text="Rate")
    tree.heading("amount", text="Amount")
    tree.heading("sgst", text="SGST")
    tree.heading("cgst", text="CGST")
    tree.heading("amount_with_gst", text="Amount (incl. GST)")

    total_amount_with_gst = 0
    with open("details.txt", "r") as f:
        for line in f:
            item_data = eval(line.strip())  
            qty = item_data["Quantity"]
            rate = item_data["Rate"]
            gst = item_data["GST"]
            amount = qty * rate
            sgst = gst / 2
            cgst = gst / 2
            gst_amount = (amount * gst) / 100
            amount_with_gst = amount + gst_amount
            total_amount_with_gst += amount_with_gst
            int(total_amount_with_gst)
            tree.insert("", "end", values=(item_data["Item Name"], qty, rate, amount, sgst, cgst, amount_with_gst))

    tree.pack()

    total_frame = ttk.Frame(final, padding="20")
    total_frame.pack(pady=20, side="left")

    Label(total_frame, text=f"Total Amount (incl. GST): {'{:.2f}'.format(total_amount_with_gst)}", font=("Arial", 14), fg='black').pack()
    Label(total_frame, text=f"Mode of Payment: {paymentmodevalue.get()}", font=("Arial", 14)).pack()

    def delete_file(detials):
      os.remove(detials)
    delete_file("details.txt")
    delete_file("records.txt")
    final.mainloop()
    
root.mainloop()