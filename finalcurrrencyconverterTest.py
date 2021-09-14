from forex_python.converter import CurrencyRates
from tkinter import *
import tkinter.messagebox

#GUI Window
root = Tk() 
root.title("Currency Converter")
root.geometry("495x420") 
root.configure(bg = '#44318D')

ip1 = StringVar(root) 
ip2 = StringVar(root) 
 
ip1.set("Select") 
ip2.set("Select") 

#function to convert currency
def RealTimeCurrencyConversion(): 
    
    c=CurrencyRates()
    
    from_currency = ip1.get() 
    to_currency = ip2.get()
    
    if (value.get()==""):
        tkinter.messagebox.showerror("Error","Amount Not Entered.\n Please a valid amount.")
        
    elif (from_currency=="Select" or to_currency=="Select"):
        tkinter.messagebox.showerror("Error","Currency Not Selected.\n Please select the currencies to be converted")
        
    else:
        new_amt = c.convert(from_currency,to_currency,float(value.get()))
        new_amount = float("{:.4f}".format(new_amt))
        output.insert(0, str(new_amount)) 

#reset function
def clear():
    value.delete(0, END)
    output.delete(0, END)
    ip1.set("Select")
    ip2.set("Select")
       
CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "GBP", "IDR", "JPY", "BGN", "ILS", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY","TRY", "HRK", "NZD", "THB", "NOK", "RUB", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]

label0 = Label(root,font=('Helvetica', 25,'bold','underline'),text="REAL TIME CURRENCY CONVERTER",bg="#44318D",fg="orange" )
label0.place(x=20, y=5)

label1 = Label(root,font=('Helvetica', 15,'bold'), text = " Enter Amount : ",bg="#3500D3",fg = "red") 
label1.place(x=20, y=65)

label2 = Label(root,font=('Helvetica', 15,'bold'), text = " From : ",bg="#3500D3",fg = "red") 
label2.place(x=20, y=140)

label3 = Label(root,font=('Helvetica', 15,'bold'), text = " To : ",bg="#3500D3",fg = "red") 
label3.place(x=250, y=140)

label4 = Label(root,font=('Helvetica', 15,'bold'), text = " Converted Amount : ",bg="#3500D3",fg = "red") 
label4.place(x=20, y=300)

# * is used for unpacking the container as list type here.
FromCurrency_option = OptionMenu(root, ip1, *CurrencyCode_list)
FromCurrency_option.place(x=100, y=140) 

ToCurrency_option = OptionMenu(root, ip2, *CurrencyCode_list) 
ToCurrency_option.place(x=310, y=140) 
 
value = Entry(root) 
value.place(x=250, y=65)

output = Entry(root)
output.place(x=250, y=298) 

convert =Button(root, font=('Arial', 15,'bold'), text="CONVERT",height=2,width=40,padx=2,pady=2, bg="red",fg = "green",command=RealTimeCurrencyConversion)
convert.place(x=50, y=220)

reset =Button(root, font=('arial', 21,'bold'), text="Reset",height=1,width=17,padx=2,pady=2, bg="white",fg = "blue",command=clear)
reset.place(x=120, y=350)

root.mainloop()
