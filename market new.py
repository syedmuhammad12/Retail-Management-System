
# ************************************ Importing Modules ****************************************

import csv
from tkinter import *
from tkinter.messagebox import showinfo,showerror,askyesno,askokcancel,showwarning
from tkinter import ttk
from datetime import *
from time import *
import os
from csv import *
from functools import reduce
import tempfile 
import random
from PIL import ImageTk,Image

# ************************************** Main Window Class *******************************************

class Main(Tk):
    
    # ================================= Login System ========================================
    
    def login(self):
       
        self.a = self.select.get()
        self.user = self.user_id.get()
        self.pas = self.user_pass.get()
        
        if self.a == "Admin":
            
            if self.user == "admin" and self.pas == "admin":
                self.admin()
            else:
                showerror("Error","Write correct password")
        
        elif self.a == "Employee":
          
            if os.path.exists("Employees.csv"):
               
                self.emp_rec = Employee.emp_data()
                self.record = list(map(lambda x:[x[1],x[8],x[4]],self.emp_rec[1:])) #return list [[emp id,pass,emp name]] 
                count = 0
                
                for i in self.record:
                
                    if i[0]==self.user:
                    
                        if i[1]==self.pas:
                            
                            self.user_logged_in = i
                            self.billing_screen = self.billing()
                       
                    else:
                        
                        showinfo("Wrong Password","Please enter the correct password")
                    
                    count+=1
                    
                    if count==0:
                    
                        showerror("Credential Error","No Employee found") 
                    
            else:
                
                showerror("File Error","No file found for Employee")
            
    
        
        else:
            
            showerror("Error","Please select the login type")
        
    # ================================= Info Function =======================================
    
    def info(self):
        showinfo("Info","This program is developed by Syed Muhammad")
    
    # ================================= Logout System ========================================
    
    def logout(self):
        self.destroy()
        Main()
    
    # ================================= Employee Entry Screen ================================ 
       
    def employee(self):
        a = Employee()
        a.mainloop()
    
    # ================================= Supplier Entry Screen ================================ 
      
    def supplier(self):
        Supplier()
    
    # ================================= Category Entry Screen ================================ 
      
    def category(self):
        Category()
    
    # ================================= Product Entry Screen ================================
    
    def products(self):
        Products()
    
    # ================================= Sales Entry Screen ================================== 
      
    def sales(self):
        Sales()
    
    # ================================= Creating Calculator ===============================================
    
    @staticmethod
    def calculator(frame):
         
        # ========================== Method for Button ===============================
    
        def click(event):
            t =  event.widget.cget("text")
            if t=="=":
                if scrval.get().isdigit():
                    val = int(scrval.get())
                else:
                    try:
                        val = eval(scrval.get())
                    except:
                        val = "Error"
                scrval.set(val)
            elif t=="C":
                scrval.set("")
            else:
                scrval.set(scrval.get()+t)
                
        # =========================== Main Calculator =================================
       
        scrval = StringVar()
        screen = Entry(frame,textvar=scrval,font="lucida 22 bold",relief=RIDGE,borderwidth=5,width=10)
        screen.pack(fill=X,side=TOP,pady=3,padx=10)
        screen.configure(state="readonly",bg="white")
        f = Frame(frame,relief=RIDGE)
        number = 9
        for i in range(3):
            for j in range(3):
                b = Button(f,text=f"{number}",font="lucida 22 bold", borderwidth=3,width=3)
                b.grid(row=i,column=j)
                b.bind("<Button-1>",click)
                number-=1
        a = ""   
        for i in range(4):
            if i==0:
                a = "+"
            elif i==1:
                a = "-"
            elif i==2:
                a="*"
            else:
                a = "/"
            b = Button(f,text=f"{a}",font="lucida 22 bold", borderwidth=3,width=3)
            b.grid(row=i,column=3)
            b.bind("<Button-1>",click)
        a = None
        for i in range(3):
            if i==0:
                a = "C"
            elif i==1:
                a = "0"
            elif i==2:
                a = "="
            b = Button(f,text=f"{a}",font="lucida 22 bold", borderwidth=3,width=3)
            b.grid(row=3,column=i)
            b.bind("<Button-1>",click) 
        f.pack(fill=X,padx=10,pady=5)

    # ================================== Creating Funtion for Supplier finding ==============================
    
    def sup_find(self,*args):
    
        self.data_prod = Products.data_pro(self.category.get())
        self.suppliers = list(map(lambda x:x[2],self.data_prod[1:]))
        self.supp.set("Select Supplier")
        self.opt2.destroy()
        self.opt2 = OptionMenu(self.f3, self.supp, *self.suppliers,command=self.pro_find)
        self.opt2.grid(row=1,column=1,pady=15,padx=10)
        self.opt2["menu"].config(bg="white",fg="black",font=("goudy old style", 12, "bold"))
        self.opt2.config(bg="white",fg="black",font=("goudy old style", 12, "bold"),width=17)

    # ====================================== Function for Product finding ====================================
    
    def pro_find(self,*args):
        self.products = list(map(lambda x:x[3],list(filter(lambda x:x[2]==self.supp.get(),self.data_prod[1:]))))
        self.opt3.destroy()
        self.prod.set("Select Product")
        self.opt3 = OptionMenu(self.f3,self.prod,*self.products,command=self.quant_find)
        self.opt3.grid(row=2,column=1,padx=20,pady=15)
        self.opt3.config(bg="white",fg="black",font=("goudy old style", 12, "bold"),width=17)
        self.opt3["menu"].config(bg="white",fg="black",font=("goudy old style", 12, "bold"))
    
    # ===================================== Function for Quantity ===========================================
    
    def quant_find(self,*args):
        quan = list(map(lambda x:[x[4],x[5]],list(filter(lambda x:(x[2]==self.supp.get() and x[3]==self.prod.get()),self.data_prod[1:])))) 
        try:
            self.unit_price = quan[0][0]
            self.quantity = quan[0][1]
            self.l11["text"] = f"  In Stock: {self.quantity}"
            self.l12["text"] = f"Unit Price: {self.unit_price}"
        except:
            self.l11["text"] = ""
            self.l12["text"] = ""
        
    # ===================================== Cart Addition Function ==========================================

    def add_cart(self):
       
        if self.quant.get() != "" and self.quant.get() != " " and self.prod.get() != "Select Supplier First" and self.prod.get() != "" :
            
            if self.quant.get().isdigit():
                
                if int(self.quant.get()) <= int(self.quantity):
            
                    try:
                        Cart(self.bill_no.get(),self.date_today,self.user_logged_in[0],self.customer_name.get(),self.customer_phone.get(),self.prod.get(),self.category.get(),self.unit_price,self.quant.get())
                    
                    except:
                        showerror("Missing Error","Please select all the options and complete all fields",parent=self)
        
                else:
                    
                    showerror("Quantity Error","Please enter the availabe number of quanitity",parent=self)
                    
            else:
                
                showerror("Quantity Error","Plase enter the appropriate value for quantity",parent=self)
       
        else:
            
            showinfo("Incomplete Field","Please enter the quantity of the product you want to buy",parent=self)
    
    # ======================================= Function to see Cart ==========================================
    
    def see_cart(self):
        
        See_Cart()

    # ======================================= Function to Calculate Price ================================
    
    def calculate_price(self):
        
        self.total_price = Cart.calculate()
        self.total_price = round(self.total_price,1)
       
        if type(self.total_price)==float:
          
            self.price.set(str(self.total_price))
            self.discount.set("10%")
            self.tax.set("4%")
            self.total_pri = round((self.total_price + (self.total_price*0.04)) - (self.total_price*0.1),2)
            self.total_bill_price.set(str(self.total_pri))
        
    # ======================================= Function to Generate bill ==============================
    
    def generate_bill(self):
       
        self.paid = self.customer_paid.get()
        
        if len(Cart.cart) > 1 and self.total_bill_price.get() != "" and self.total_bill_price.get() != " ":
        
            try:
            
                if self.paid != "" and self.paid != " ":
                    self.return_price.set(f"{round((float(self.paid) - float(self.total_bill_price.get())),2)}")
                else:
                    raise Exception()
                
                try:
                    
                    self.cart_items = list(map(lambda x:[x[12],x[16],x[18],f"Rs.{str(float(x[16][3:])*float(x[18]))}"] ,Cart.cart[1:]))
                    self.total_quantities = sum(list(map(lambda x: int(x[2]),self.cart_items)))
                    
                    self.text.config(state="normal")
                    self.text.insert(END,"\t\t\tSyed Super Mart")
                    self.text.insert(END,"\n\nBill No: {}\t\t\t\t        Date / Time: {}    {}".format(self.bill_no.get(),self.date_today,self.date.strftime('%I:%M:%S %p')))
                    self.text.insert(END,f"\nCustomer Name: {'N/A' if self.customer_name.get()=='' else self.customer_name.get()}\t\t\t\t               Customer Number: {'N/A' if self.customer_phone.get()=='' else self.customer_phone.get()}")
                    self.text.insert(END,"\n")
                    
                    for i in range(60):
                        self.text.insert(END,"=")
                    
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"{'Product Name'}\t\t\tUnit Price\t\tUnits\t\tTotal Price")
                    self.text.insert(END,"\n")
                    
                    for i in range(60):
                        self.text.insert(END,"=")
                    
                    self.text.insert(END,"\n")
                    
                    for  i in self.cart_items:
                    
                        if i!=self.cart_items[-1]:
                        
                            self.text.insert(END,f"{i[0]}\t\t\t{i[1]:10}\t\t{i[2]:5}\t\t{i[3]}")
                            self.text.insert(END,"\n")
                            self.text.insert(END,f"{100*'-'}")
                            self.text.insert(END,"\n")
                        
                        else:
                            
                            self.text.insert(END,f"{i[0]}\t\t\t{i[1]:10}\t\t{i[2]:5}\t\t{i[3]}")
                        
                    self.text.insert(END,"\n")
                    
                    for i in range(67):
                        self.text.insert(END,"_")
                    
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"{'Total'}\t\t\t\t\t{self.total_quantities}\t\tRs.{self.total_price}")
                    self.text.insert(END,"\n")
                    
                    for i in range(67):
                        self.text.insert(END,"_")
                    
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"Tax: {'4%'}\t\t\tDiscount: {'10%'}\t\t             Total Price: Rs.{self.total_pri}")
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"\t\t\t\t\t       Cash Recieved: Rs.{self.customer_paid.get()}")
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"{100*'-'}")
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"\t\t\t\t\t\tBalance: Rs.{self.return_price.get()}")
                    self.text.insert(END,"\n")
                    self.text.insert(END,"\n")
                    self.text.insert(END,f"{'*'*28} Thank You {'*'*29}")

                    self.text.config(state=DISABLED)
                    
                    Cart.add_to_file(self)
                    
                except:
                    showinfo("Error","Please add items in the cart first")
            
            except:
                showerror("Value Error","Please write the appropriate value of return")
                
        else: 
            
            showinfo("No Product Found","Please add some products in the cart and calculate price first")

    # ======================================= Function to Print Bill =================================
    
    def print_bill(self):
    
        self.text.config(state="normal")
        self.bill = self.text.get(1.0,END)
       
        try:
        
            if self.bill != "" and self.bill != " " and self.bill != "\n" :
            
                self.file = tempfile.mktemp(".txt")
                
                with open(self.file,"w") as f:
                
                    f.write("\t\t\tSyed Super Mart")
                    f.write("\n\nBill No: {:<25}  Date / Time: {}     {}".format(self.bill_no.get(),self.date_today,self.date.strftime('%I:%M:%S %p')))
                    f.write(f"\nCustomer Name: {'N/A' if self.customer_name.get()=='' else self.customer_name.get():<20} Customer Number: {'N/A' if self.customer_phone.get()=='' else self.customer_phone.get()}")
                    f.write("\n")
                    f.write(f"{'='*64}")
                    f.write("\n")
                    f.write(f"{'Product Name':<26}{'Unit Price':<10}\t\t{'Units':<5}\t\t{'Total Price':<11}")
                    f.write("\n")
                    f.write(f"{'='*64}")
                    f.write("\n")
                
                    for  i in self.cart_items:
                    
                        if i!=self.cart_items[-1]:
                        
                            f.write(f"{i[0]:<26}{i[1]:<10}\t\t{i[2]:<5}\t\t{i[3]:<11}")
                            f.write("\n")
                            f.write(f"{'-'*90}")
                            f.write("\n")
                    
                        else:
                            
                            f.write(f"{i[0]:<26}{i[1]:<10}\t\t{i[2]:<5}\t\t{i[3]:<11}")
                    
                    f.write("\n")
                    f.write(f"{'_'*64}")
                    f.write("\n")
                    f.write(f"{'Total':<40}\t\t{self.total_quantities:<5}\t\tRs.{self.total_price}")
                    f.write("\n")
                    f.write(f"{'_'*64}")
                    f.write("\n")
                    f.write(f"{'Tax: 4%':15}\t{'Discount: 10%':20}\t\tTotal: Rs.{self.total_pri}")
                    f.write("\n")
                    f.write(f"\t\t\t\t  Cash Received: Rs.{self.customer_paid.get()}")
                    f.write("\n")
                    f.write(f"{'-'*90}")
                    f.write("\n")
                    f.write(f"\t\t\t\t                Balance: Rs.{self.return_price.get()}")
                    f.write("\n")
                    f.write("\n")
                    f.write(f"{'*'*27}  Thank You  {'*'*27}")
            
                os.startfile(self.file,"print")
            
            else:
                
                showinfo("Bill Not Found","Please generate bill first",parent=self)
            
            self.text.config(state=DISABLED)
        
        except:
            
            showinfo("Nothing found","Please buy some products then print bill",parent=self)
        
        
    # ======================================== Function for Clear All ================================
    
    def clear_all(self):
        
        self.category.set("Select Category")
        self.supp.set("Select Category First") 
        self.prod.set("Select Supplier First") 
        Cart.remove_cart()
        self.quant.set("")
        self.price.set("")
        self.tax.set("")
        self.discount.set("")
        self.total_bill_price.set("")
        self.customer_paid.set("")
        self.return_price.set("")
        self.bill_no.set(f"{random.randint(100000000000,999999999999)}")
        self.customer_name.set("")
        self.customer_phone.set("")
        self.text.config(state="normal")
        self.text.delete(1.0,END)
        self.text.config(state=DISABLED)
        self.l11["text"] = ""
        self.l12["text"] = ""
  
    # ======================================= Function to Calculate Total Record =====================
    
    def total_record(self):
        
        # Finding total number Employees
        self.total_employees_number = str(len(Employee.emp_data()[1:])) if os.path.exists("Employees.csv") else "0"
        
        # Finding total number Suppliers
        self.total_supplier_number = str(len(Supplier.supp_data()[1:])) if os.path.exists("Suppliers.csv") else "0"
       
        # Finding total category file number
        
        self.category_file_names = list(map(lambda x:x[:-4],list(filter(lambda x:x.endswith(".csv")  and (x!="Suppliers.csv" and x!="Employees.csv" and x!="Sales.csv"),os.listdir(".")))))
        self.total_category_number = "0" if (len(self.category_file_names) == 0) else str(len(self.category_file_names))
        
        # Finding products from seperate category
        self.total_products_list = []
       
        for i in self.category_file_names:
            
            if type(i)==str:
                product_list = Products.data_pro(i)
                
                for j in product_list:
                   
                    if j != []:
                        self.total_products_list.append(j)
       
        self.total_products_number = "0" if (len(self.category_file_names) == 0) else str(len(list(filter(lambda x: x != ["S.No","Category of Product","Supplier Name","Name of Product","Price of the Product","Quantity Available"] ,self.total_products_list))))
        
        #Finding total number of sales
        self.total_sales_number = str(len(list(filter(lambda x: x != ["S.No","Bill No","Date","Emp ID","Customer Name","Customer Number","Product Name","Category","Unit Price","Units"] ,Products.data_pro("Sales"))))) if os.path.exists("Sales.csv") else "0"
 
        
# ************************************** Creating Main Program ***************************************            
  
    # ====================================== Main Screen =============================================
        
    def __init__(self):
        
        # ================================ Main Screen ========================================
        
        super().__init__()
        super().geometry("700x500+330+100")
        super().state("zoomed")
        super().title("Retail Management System")
        super().iconbitmap("icon.ico")
        
        # =============================== Back Ground ==========================
        
        #images
        self.background_image = PhotoImage(file="Main Background.png")
        self.login_image = PhotoImage(file="login.png")
        self.user_image = PhotoImage(file="user icon.png")
        self.pass_image = PhotoImage(file="pass icon.png")
        
        
        #Background
        self.background_pic = Label(self,image=self.background_image).pack()
    
        #Credits
        self.credit = Label(self,text="IMS - Inventory Management Syestem | Developed By: Syed Muhammad",fg="white",bg="grey").place(x=0,y=685,relwidth=1)
        
        # Management Label
        self.l1 = Label(self,text="Retail Management",font=("Times New Roman","30","bold"),fg="black",bg="#ff00ff").place(x=0,y=0,relwidth=1)
        
        # ========================== Setting Variables =============================
        
        self.select = StringVar()
        self.values = ("Admin","Employee")
        self.user_id = StringVar()
        self.user_pass = StringVar()
        
        # ======================= Combobox for Login Type ==========================
        
        self.cb = ttk.Combobox(self,textvar=self.select,values=self.values,font=("goudy old style",13),state="readonly",justify=CENTER).place(x=590,y=100)
        self.select.set(f"{self.values[0]}")
       
        # ======================= Setting Entries ==============================
       
        self.f = Frame(self,background="white",width="500",height="300")
        self.l1 = Label(self.f,image=self.login_image,bg="white").pack(anchor=CENTER,pady=10)
        
        self.f2 = Frame(self.f,bg="white")
        self.l2 = Label(self.f2,text="User ID  ",image=self.user_image,compound=LEFT,font=("Times New Roman",13),bg = "white").grid(padx=20,pady=25,row=1,column=0)
        self.e1 = Entry(self.f2,bg = "white",textvar=self.user_id,font=("Times New Roman",12),relief=SOLID).grid(padx=30,pady=25,row=1,column=4)
        self.l3 = Label(self.f2,text="Password",image=self.pass_image,compound=LEFT,font=("Times New Roman",13),bg = "white").grid(padx=20,row=2,column=0)
        self.e2 = Entry(self.f2,bg = "white",textvar=self.user_pass,show="*",font="lucida 11",relief=SOLID).grid(padx=30,row=2,column=4)
        self.f2.pack(padx=10)
        
        self.button = Button(self.f,text = "Login",font=("Times New Roman",12,"bold"),relief = "raised",borderwidth=2,bg='green',width=12,command=self.login).pack(pady=15,anchor=CENTER)
        self.f.place(x=500,y=250)
       
        # ======================= Comman attributes ==============================
       
        self.date = datetime.now()
        self.date_today = f"{self.date.day}/{self.date.month}/{self.date.year}"
        self.user_logged_in = []
       
        # ========================================================================
        self.mainloop()

    # ====================================== Admin Panel ===============================================

    def admin(self):
        
        # ============================= Destroying Parent Screen =============================
        
        self.destroy()
        
        # ============================== Creating Screen ================================
       
        super().__init__()
        super().geometry("700x500+330+100")
        super().state("zoomed")
        super().config(bg="white")
        super().title("Retail Management System - Admin Panel")
        super().iconbitmap("icon.ico")
       
        # =================================== Image =======================================
        
        self.admin_image = ImageTk.PhotoImage(Image.open("admin panel.jpg"))
        self.shopping_cart_image = PhotoImage(file="shopping cart.png")
      
        # =============================== Heading =========================================
        
        self.f1 = Frame(self,bg="#483d8b")
        self.l1 = Label(self.f1,image=self.shopping_cart_image,text="Inventory Management",bg="#483d8b",fg="white",compound=LEFT,font=("Times New Roman","35","bold")).pack(side=LEFT,pady=5,padx=20)
        self.b1 = Button(self.f1,text="Logout",width=9,font=("Times New Roman",11),bg="yellow",command=self.logout).pack(side=RIGHT,anchor=N,pady=20,padx=50)
        self.f1.pack(fill=X,side=TOP)
        
        # ============================== Date & Time =======================================
       
        self.f2 = Frame(self,bg="grey")
        self.l1 = Label(self.f2,text="Welcome to inventory management",bg="grey",fg="white").grid(row=0,padx=300,column=0)
        self.l2 = Label(self.f2,text=f"Date: {self.date_today}",bg="grey",fg="white",anchor="n").grid(row=0,column=5)
        self.l3 = Label(self.f2,text=f"Login Time: {self.date.strftime('%I:%M:%S %p')}",bg="grey",fg="white",anchor="n").grid(row=0,column=8,padx=200)
        self.f2.pack(fill=X,side=TOP)
        
        # =================================== Credits ====================================
       
        self.credit = Label(self,text="IMS - Inventory Management Syestem | Developed By: Syed Muhammad",fg="white",bg="grey").pack(side=BOTTOM,fill=X)
        
        # ================================== Side Bar =====================================
       
        self.f3 = Frame(self,bg="white")
        
        self.l1 = Label(self.f3,image=self.admin_image,text="        Menu        ",compound=TOP,font="lucida 20 bold",fg="white",bg="#4bdd9e",relief="flat",borderwidth=10).pack()
        
        self.f4 = Frame(self.f3)
        self.b1 = Button(self.f4,text=" >> Employee",font="lucida 20 bold",relief="solid",bg="white",width=13,borderwidth=3,command=self.employee).grid(row=0,column=0)
        self.b2 = Button(self.f4,text=" >> Supplier",font="lucida 20 bold",relief="solid",bg="white",width=13,borderwidth=3,command=self.supplier).grid(row=1,column=0)
        self.b3 = Button(self.f4,text=" >> Category",font="lucida 20 bold",relief="solid",bg="white",width=13,borderwidth=3,command=self.category).grid(row=2,column=0)
        self.b4 = Button(self.f4,text=" >> Products",font="lucida 20 bold",relief="solid",bg="white",width=13,borderwidth=3,command=self.products).grid(row=3,column=0)
        self.b5 = Button(self.f4,text=" >> Sales",font="lucida 20 bold",relief="solid",bg="white",width=13,borderwidth=3,command=self.sales).grid(row=4,column=0)
        self.f4.pack(side=LEFT,anchor=N)
        
        self.f3.pack(side=LEFT,fill=Y)
       
        # ================================== Total Records Number ==========================
        
        self.total_record()
        
        # ================================== Middle Frame =====================================
       
        self.f5 = Frame(self,bg="white")
        
        self.l1 = Label(self.f5,text=f"Total Eployees\n\n[{self.total_employees_number}]",font="lucida 15",width=20,height=6,relief="sunken",bg="#7193ff",fg="white").grid(row=0,column=0,padx=10,pady=30)
        self.l2 = Label(self.f5,text=f"Total Suppliers\n\n[{self.total_supplier_number}]",font="lucida 15",width=20,height=6,relief="sunken",bg="#fb9731",fg="white").grid(row=0,column=1,pady=30)
        self.l3 = Label(self.f5,text=f"Total Categories\n\n[{self.total_category_number}]",font="lucida 15",width=20,height=6,relief="sunken",bg="#119066",fg="white").grid(row=0,column=2,pady=30,padx=10)
        self.l4 = Label(self.f5,text=f"Total Products\n\n[{self.total_products_number}]",font="lucida 15",width=20,height=6,relief="sunken",bg="#71857e",fg="white").grid(row=1,column=0,pady=20,padx=10)
        self.l5 = Label(self.f5,text=f"Total Sales\n\n[{self.total_sales_number}]",font="lucida 15",width=20,height=6,relief="sunken",bg="#ccb113",fg="white").grid(row=1,column=1,pady=20)
        
        self.f5.pack() 
      
       # ==============================================================================================
       
        self.mainloop()
    
    # ====================================== Billing Panel =============================================
    
    def billing(self):
        
        # ============================= Destroying Parent Screen =============================
        
        self.destroy()
        
        # ============================ Creating Screen =============================
        
        super().__init__()
        super().geometry("700x500+330+100")
        super().state("zoomed")
        super().config(bg="white")
        super().title("Retail Management System - Billing Panel")
        super().iconbitmap("icon.ico")
        
        # ============================ Image Variable ================================
        
        self.billing_image = PhotoImage(file="billing machine.png")
        
        # ============================ Setting Header ==================================
        
        self.f1 = Frame(self,bg="#000080")
        
        self.l1 = Label(self.f1,image=self.billing_image,text="Billing Management",bg="#000080",fg="white",compound=LEFT,font=("Times New Roman","30","bold")).pack(side=LEFT,pady=5,padx=20)
        self.b = Button(self.f1,text="Logout",width=9,font=("Times New Roman",11),bg="yellow",command=self.logout).pack(side=RIGHT,anchor=N,pady=20,padx=50)
        
        self.f1.pack(fill=X)
        
        # ============================= Credits =========================================
        
        self.credit = Label(self,text="IMS - Inventory Management Syestem | Developed By: Syed Muhammad",fg="white",bg="grey").pack(side=BOTTOM,fill=X)
        
        # ============================= Setting Variables =================================
        
        self.employ = self.user_logged_in[2]
        
        self.bill_no = StringVar()
        self.bill_no.set(f"{random.randint(100000000000,999999999999)}")
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        
        self.category = StringVar() #for category menu
        self.category.set("Select Category")
        self.categories = list(map(lambda x:x[:-4],list(filter(lambda x:x.endswith(".csv")  and (x!="Suppliers.csv" and x!="Employees.csv" and x!="Sales.csv"),os.listdir("."))))) 
        
        self.supp = StringVar() #for supplier menu
        self.supp.set("Select Category First") 
        self.suppliers = [""]
        
        self.prod = StringVar() #for product option menu
        self.prod.set("Select Supplier First") 
        self.products = [""]
        
        self.quant = StringVar()
        self.price = StringVar()
        self.tax = StringVar()
        self.discount = StringVar()
        self.total_bill_price = StringVar()
        self.customer_paid = StringVar()
        self.return_price = StringVar()
        
        # ============================== Date & Time ========================================
        
        self.f2 = Frame(self,bg="grey")
        self.l1 = Label(self.f2,text=f"Employee Name: {self.employ}",bg="grey",fg="white").grid(row=0,padx=150,column=0)
        self.l1 = Label(self.f2,text="Welcome to Billing management",bg="grey",fg="white").grid(row=0,padx=65,column=1)
        self.l2 = Label(self.f2,text=f"Date: {self.date_today}",bg="grey",fg="white",anchor="n").grid(row=0,column=2,padx=50)
        self.l3 = Label(self.f2,text=f"Login Time: {self.date.strftime('%I:%M:%S %p')}",bg="grey",fg="white",anchor="n").grid(row=0,column=3,padx=100)
        self.f2.pack(fill=X,side=TOP)
        
        # ============================= Adjusting Customer Information ===========================
        
        self.f2 = LabelFrame(self,text="Customer Details",font=("Times New Roman","15"),relief=GROOVE,bg="white")
        
        self.l4 = Label(self.f2,text="Billing No :",font="lucida 15",bg="white").grid(row=0,column=0,padx=10,pady=5)
        self.e10 = Entry(self.f2,textvar=self.bill_no,font="lucida 13 bold",bg="lightyellow",relief=SOLID,state="readonly").grid(row=0,column=1,padx=20,pady=5)
        
        self.l5 = Label(self.f2,text="Customer Name :",font="lucida 15",bg="white").grid(row=0,column=2,padx=10,pady=5)
        self.e1 = Entry(self.f2,textvar=self.customer_name,font="lucida 13 bold",bg="lightyellow",relief=SOLID).grid(row=0,column=3,padx=20,pady=5)
        
        self.l6 = Label(self.f2,text="Contact No :",font="lucida 15",bg="white").grid(row=0,column=4,padx=10,pady=5)
        self.e2 = Entry(self.f2,textvar=self.customer_phone,font="lucida 13 bold",bg="lightyellow",relief=SOLID).grid(row=0,column=5,padx=20,pady=5)
        
        self.f2.pack(fill=X,pady=5,padx=3)
        
        # ============================= Main Frame ===================================
        
        self.f = Frame(self,bg="white")
        
        # ============================= Setting Entries ===============================
        
        try:
                
            self.f3 = LabelFrame(self.f,text="Products",relief=GROOVE,font=("Times New Roman","15"),bg="white")
            
            self.l7 = Label(self.f3,text="Select Category",font="lucida 15",bg="white").grid(row=0,column=0,padx=20,pady=15)
            if self.categories != []:
                self.opt1 = OptionMenu(self.f3,self.category,*self.categories,command=self.sup_find) 
                self.opt1.grid(row=0,column=1,pady=15,padx=10)
                self.opt1.config(bg='white',fg="black",font=("goudy old style", 12, "bold"),width=17)
                self.opt1["menu"].config(bg="white",fg="black",font=("goudy old style", 12, "bold"))
            else:
                self.opt1 = OptionMenu(self.f3,self.category,"Please add category") 
                self.opt1.grid(row=0,column=1,pady=15,padx=10)
                self.opt1.config(bg='white',fg="black",font=("goudy old style", 12, "bold"),width=17)
                self.opt1["menu"].config(bg="white",fg="black",font=("goudy old style", 12, "bold"))
                
            self.l8 = Label(self.f3,text="Select Supplier ",font="lucida 15",bg="white").grid(row=1,column=0,padx=20,pady=15)
            self.opt2 = OptionMenu(self.f3, self.supp, *self.suppliers)
            self.opt2.grid(row=1,column=1,pady=15,padx=10)
            self.opt2["menu"].config(bg="white",fg="black",font=("goudy old style", 12, "bold"))
            self.opt2.config(bg="white",fg="black",font=("goudy old style", 12, "bold"),width=17)
            
            self.l9 = Label(self.f3,text="Product           ",font="lucida 15",bg="white").grid(row=2,column=0,padx=20,pady=15)
            self.opt3 = OptionMenu(self.f3,self.prod,*self.products)
            self.opt3.grid(row=2,column=1,padx=20,pady=15)
            self.opt3.config(bg="white",fg="black",font=("goudy old style", 12, "bold"),width=17)
            self.opt3["menu"].config(bg="white",fg="black",font=("goudy old style", 12, "bold"))
            
            self.l10 = Label(self.f3,text="QTY               ",font="lucida 15",bg="white").grid(row=3,column=0,padx=20,pady=15)
            self.e3 = Entry(self.f3,textvar=self.quant,font="lucida 13 bold",bg="lightyellow",relief=SOLID).grid(row=3,column=1,padx=20,pady=15)
            
            self.f20 = Frame(self.f3,bg="white")
            
            self.l11 = Label(self.f20,text="",font=("goudy old style",12,"bold"),bg="white")
            self.l11.grid(row=0,column=0,padx=5,sticky=W)
            
            self.l12 = Label(self.f20,text="",font=("goudy old style",12,"bold"),bg="white")
            self.l12.grid(row=0,column=1,padx=5,sticky=W)
            
            self.f20.grid(row=4,column=0,columnspan=3,padx=20,sticky=W)
            
            self.f15 = Frame(self.f3,bg="white")
            
            self.b1 = Button(self.f15,text="Add to Cart",font=("goudy old style",13,"bold"),bg="cyan",width=13,command=self.add_cart).grid(row=0,column=0)
            self.b2 = Button(self.f15,text="See Cart",font=("goudy old style",13,"bold"),bg="#a23efa",width=13,command=self.see_cart).grid(row=0,column=1,padx=30)
            
            self.f15.grid(row=5,column=0,padx=20,pady=11,columnspan=2)
            
            self.f3.grid(row=0,column=0,padx=3,sticky="n")
        
        except:
            
            showinfo("File Error","No product found, Please add suppliers,categories and products before billing.")
        
        # ================================ Calculator ======================================
        
        self.f4 = LabelFrame(self.f,relief=RIDGE,borderwidth=3)
        Main.calculator(self.f4)
        self.f4.grid(row=0,column=1,padx=3,pady=10,sticky="n")
        
        # ================================ Bill Area =======================================
        
        self.f5 = LabelFrame(self.f,text="Bill Area",font="ariel 15",bg="white")
        
        self.y_scrollbar = Scrollbar(self.f5,orient="vertical")
        self.text = Text(self.f5,width=67,height=17,yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.pack(side=RIGHT,fill=Y)
        self.y_scrollbar.config(command=self.text.yview)
        self.text.pack(pady=5)
        
        self.text.config(font=("Times New Roman","13","bold"),state=DISABLED)
        
        self.f5.grid(row=0,column=2,padx=3)
        
        # ================================= Main Frame Ends =========================================
        
        self.f.pack(fill=X,side=TOP,pady=5)
        
        # ================================= Adjusting Billing Menu =================================

        self.f6 = LabelFrame(self,text="Billing Menu",font=("Times New Roman", "15"),bg="white")
        
        self.f7 = Frame(self.f6,bg="white")
        
        self.l13 = Label(self.f7,text="Price",font="lucida 15",bg="white").grid(row=0,column=0,pady=2,padx=10)
        self.e4 = Entry(self.f7,textvar=self.price,font="lucida 15",bg="lightyellow",relief=SOLID,state="readonly").grid(row=0,column=1,pady=2,padx=5)
       
        self.l14 = Label(self.f7,text="Tax %",font="lucida 15",bg="white").grid(row=1,column=0,pady=2,padx=10)
        self.e5 = Entry(self.f7,textvar=self.tax,font="lucida 15",bg="lightyellow",relief=SOLID,state="readonly").grid(row=1,column=1,pady=2,padx=5)
        
        self.l15 = Label(self.f7,text="       Discount %",font="lucida 15",bg="white").grid(row=2,column=0,pady=2,padx=10)
        self.e6 = Entry(self.f7,textvar=self.discount,font="lucida 15",bg="lightyellow",relief=SOLID,state="readonly").grid(row=2,column=1,pady=2,padx=5)
        
        self.l16 = Label(self.f7,text="Total Price",font="lucida 15",bg="white").grid(row=0,column=2,pady=2,padx=10)
        self.e6 = Entry(self.f7,textvar=self.total_bill_price,font="lucida 15",bg="lightyellow",relief=SOLID,state="readonly").grid(row=0,column=3,pady=2,padx=5)
        
        self.l17 = Label(self.f7,text="      Customer Paid",font="lucida 15",bg="white").grid(row=1,column=2,pady=2,padx=10)
        self.e7 = Entry(self.f7,textvar=self.customer_paid,font="lucida 15",bg="lightyellow",relief=SOLID).grid(row=1,column=3,pady=2,padx=5)
        
        self.l18 = Label(self.f7,text="Return      ",font="lucida 15",bg="white").grid(row=2,column=2,pady=2,padx=10)
        self.e8 = Entry(self.f7,textvar=self.return_price,font="lucida 15",bg="lightyellow",relief=SOLID,state="readonly").grid(row=2,column=3,pady=2,padx=5)
        
        self.f7.pack(side=LEFT)
        
        self.f8 = Frame(self.f6,bg="white")
        
        self.b3 = Button(self.f8,text="Calculate Price",font=("goudy old style",13,"bold"),bg="#2f9aed",width=13,command=self.calculate_price).grid(row=0,column=0,pady=7,padx=30)
        self.b4 = Button(self.f8,text="Generate Bill",font=("goudy old style",13,"bold"),bg="#1ceb61",width=13,command=self.generate_bill).grid(row=0,column=1,pady=7,padx=30)
        self.b5 = Button(self.f8,text="Print Bill",font=("goudy old style",13,"bold"),bg="#e08d28",width=13,command=self.print_bill).grid(row=1,column=0,pady=7,padx=30)
        self.b6 = Button(self.f8,text="Clear All",font=("goudy old style",13,"bold"),bg="#f12df7",width=13,command=self.clear_all).grid(row=1,column=1,pady=7,padx=30)
        
        self.f8.pack(padx=30)
        
        self.f6.pack(fill=X,anchor="nw",padx=5,pady=5)

        # =================================================================================================
        
        super().mainloop()


# ************************************** Class for Employees ******************************************** 
                
class Employee(Toplevel):
    
    def __init__(self):
        
        #======================= Creating Screen =========================

        super().__init__()
        super().geometry("1110x530+235+132")
        super().wm_minsize(1110,530)
        super().wm_maxsize(1110,530)
        super().title("Employee Database")
        super().config(bg="white")
        super().iconbitmap("icon.ico")

        #========================= Setting Variables ======================

        self.search = StringVar()
        self.emp_no = StringVar()
        self.gender = StringVar()
        self.contact_no = StringVar()
        self.name = StringVar()
        self.dob = StringVar()
        self.doj = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.salary = StringVar()
        self.address = StringVar()

        # ========================= Adjusting Search ========================

        self.f = LabelFrame(self,text="Searh Employee",font=("Times New Roman","15"),bg="white")
       
        self.lab = Label(self.f,text="Enter Employee ID",font="lucida 13",bg="white").grid(row=0,column=0,padx=15,pady=5)
        self.e = Entry(self.f,textvar=self.search,font="lucida 13",bg="lightyellow",relief=SOLID).grid(row=0,column=1,padx=5,pady=5)
        self.b = Button(self.f,text="Search",font="lucida 13",bg="#4caf50",width=12,command=self.search_emp).grid(row=0,column=2,padx=15,pady=5)
        
        self.f.pack(pady=5,side=TOP,ipadx=10)
        
        # ====================== Label for Details ===============================
        
        self.l = Label(self,text="Employee Details",font="lucida 15",bg="#000080",fg="white").pack(fill=X,pady=5,padx=90)

        # ====================== Setting Mid-page Frame ======================

        self.f1 = Frame(self,bg="white")
        self.l1 = Label(self.f1,text="Employee ID  ",font="lucida 13",bg="white").grid(row=0,column=0,pady=10)
        self.e1 = Entry(self.f1,textvar=self.emp_no,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=0,column=1,padx=18,pady=10)
        self.l2 = Label(self.f1,text="Gender",font="lucida 13",bg="white").grid(row=0,column=2,pady=10)
        self.e2 = Entry(self.f1,textvar=self.gender,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=0,column=3,padx=19,pady=10)
        self.l3 = Label(self.f1,text="Contact No.",font="lucida 13",bg="white").grid(row=0,column=4,pady=10)
        self.e3 = Entry(self.f1,textvar=self.contact_no,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=0,column=5,padx=19,pady=10)
       
        self.l4 = Label(self.f1,text="Name            ",font="lucida 13",bg="white",anchor="ne").grid(row=1,column=0,pady=10)
        self.e4 = Entry(self.f1,textvar=self.name,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1,column=1,padx=18,pady=10)
        self.l5 = Label(self.f1,text="D.O.B.",font="lucida 13",bg="white").grid(row=1,column=2,pady=10)
        self.e5 = Entry(self.f1,textvar=self.dob,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1,column=3,padx=19,pady=10)
        self.l6 = Label(self.f1,text="D.O.Joining.",font="lucida 13",bg="white").grid(row=1,column=4,pady=10)
        self.e6 = Entry(self.f1,textvar=self.doj,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1,column=5,padx=19,pady=10)
        
        self.l7 = Label(self.f1,text="Email            ",font="lucida 13",bg="white").grid(row=2,column=0,pady=10)
        self.e7 = Entry(self.f1,textvar=self.email,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=2,column=1,padx=18,pady=10)
        self.l8 = Label(self.f1,text="Password",font="lucida 13",bg="white").grid(row=2,column=2,pady=10)
        self.e8 = Entry(self.f1,textvar=self.password,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=2,column=3,padx=19,pady=10)
        self.l9 = Label(self.f1,text="Salary",font="lucida 13",bg="white").grid(row=2,column=4,pady=10)
        self.e9 = Entry(self.f1,textvar=self.salary,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=2,column=5,padx=19,pady=10)
        
        self.l10 = Label(self.f1,text="Adress          ",font="lucida 13",bg="white").grid(row=3,column=0,pady=10)
        self.e10 = Entry(self.f1,textvar=self.address,font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=3,column=1,pady=10)
        
        self.f2 = Frame(self.f1,bg="white")
        
        self.b1 = Button(self.f2,text="Save",font=("goudy old style","12","bold"),bg="#2f9aed",width=12,command=self.emp_save).grid(row=0,column=0,padx=10)
        self.b1 = Button(self.f2,text="Clear",font=("goudy old style","12","bold"),bg="#1ceb61",width=12,command=self.clear).grid(row=0,column=1,padx=10)
        
        self.f2.grid(row=3,column=2,columnspan=2)
        
        self.f1.pack(fill=X,padx=90)
        #============================ Information Treeview ========================================
        
        self.f3 = LabelFrame(self,text="Employee Record",font="lucida 12",bg="white")
        self.style = ttk.Style()
        self.style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="white",rowheight=25)
        
        self.style.theme_use("default")
        
        
        col = ("S.No","Employee ID","Gender","Contact No.","Employee Name","DOB","DOJ","Email","Password","Salary","Address")
        
        self.yscrollbar = Scrollbar(self.f3)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        self.treeview = ttk.Treeview(self.f3,height=20,show="headings",columns=col,yscrollcommand=self.yscrollbar.set)
        
        for i in range(len(col)):
            self.treeview.column(col[i],width=len(col[i])+2,anchor=W)
            
        for i in range(len(col)):
            self.treeview.heading(col[i],text=col[i])
        
        self.count = 1
        if os.path.exists("Employees.csv"):
            self.employees = Employee.emp_data()
            if len(self.employees) > 1:
                for i in self.employees[1:]:
                    self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
                    self.count+=1
        
        self.treeview.pack(fill=BOTH)
        self.yscrollbar.config(command=self.treeview.yview)
        
        self.f3.pack(padx=90,pady=10,fill=BOTH)
        
        # =========================== Screen Ends =================================================
        self.mainloop()
        
          
    #======================= Data Saving for Employees =================================== 
    
    def emp_save(self):
       
        #============================= Entries Var ========================================

        self.emp = self.emp_no.get()
        self.gen = self.gender.get()
        self.con = self.contact_no.get()
        self.nam = self.name.get()
        self.do  = self.dob.get()
        self.join = self.doj.get()
        self.ema = self.email.get()
        self.passw = self.password.get()
        self.sal = self.salary.get()
        self.add = self.address.get()

        #================================= Saving into the File =================================================

        self.yes_no = askyesno("Confirmation","Do you really want to add the data?",parent=self)
        
        if self.yes_no:
        
            try:
            
                if os.path.exists("Employees.csv"):
                    
                    self.employees = Employee.emp_data()
                    s = len(self.employees)
                
                else:
                    
                    with open("Employees.csv","a+",newline="") as f:
                        
                        write = writer(f)
                        write.writerow(["S.No"," ","Employee ID"," ","Gender"," ","Contact No."," ","Name of Employee"," ","D.O.B"," ","D.O.Joining"," ","Email"," ","Password"," ","Salary"," ","Adress"," "])
                        write.writerow([])
                    
                    s = 1
                
                with open("Employees.csv","a+") as f:
                    pass
                
                try:
                
                    if self.emp=="" or self.nam=="" or self.passw=="":
                        raise Exception() 
                    
                    e = [str(s)," ",self.emp," ",self.gen," ",self.con," ",self.nam," ",self.do," ",self.join," ",self.ema," ",self.passw," ",self.sal," ",self.add," "]
                    data = list(map(lambda x:x if x!="" else "N/A",e))
                    
                    if os.path.exists("Employees.csv"):
                        
                        self.employees = Employee.emp_data()
                        if all(x[1]!=self.emp for x in self.employees):   
                            
                            with open("Employees.csv","a+",newline="") as f:
                            
                                write =writer(f)
                                write.writerow(data)
                            
                            self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,data[2],data[4],data[6],data[8],data[10],data[12],data[14],data[16],data[18],data[20]))
                            self.count+=1
                            
                        else:
                            showerror("Data Error","Employee already present",parent=self)
                
                    else:
                        
                        with open("Employees.csv","a+",newline="") as f:
                            
                            write =writer(f)
                            write.writerow(data)
                        
                        self.count = 1    
                        self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,data[2],data[4],data[6],data[8],data[10],data[12],data[14],data[16],data[18],data[20]))
                        self.count+=1
                    
                except:
                    showinfo("Missing Field","Emploee ID,password and name are required",parent=self)
        
            except:
                showerror("File Error","Please close the file first",parent=self)  
    
    # =============================== Function for Clear ========================================
    
    def clear(self):
        
        self.search.set("")
        self.emp_no.set("")
        self.gender.set("")
        self.contact_no.set("")
        self.name.set("")
        self.dob.set("")
        self.doj.set("")
        self.email.set("")
        self.password.set("")
        self.salary.set("")
        self.address.set("")
    
    # =============================== Search Employee ===========================================
    
    def search_emp(self):
        
        try: 
            
            with open("Employees.csv","r+") as f:
                pass
        
            try:
                
                if self.search.get()!="":
                    
                    self.sea = self.search.get()
                    self.employee = list(filter(lambda x:x[1]==self.sea,self.employees[1:]))
                    
                    if len(self.employee) > 0:
                        
                        for record in self.treeview.get_children():
                            self.treeview.delete(record)
                       
                        self.count=1
                       
                        for i in self.employee:
                            self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
                            self.count+=1
                    
                    else:
                        showinfo("Not Found","No match found",parent=self)
                
                else:
                    
                    for record in self.treeview.get_children():
                        self.treeview.delete(record)
                    self.count = 1
                    if os.path.exists("Employees.csv"):
                        self.employees = Employee.emp_data()
                        if len(self.employees) > 1:
                            for i in self.employees[1:]:
                                self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
                                self.count+=1
                    
            except:
                showinfo("Not Found","No match found",parent=self)
                
        except:
            
            showerror("File Error","File is open or not in the directory",parent=self)
    
    # ========================== Method for Extracting Info from File   ===============================================
    
    @staticmethod
    def emp_data():
       
        if os.path.exists("Employees.csv"):
            
            with open("Employees.csv","r+") as f:
                read = reader(f)
                c = []
               
                for data in read:
                   
                    if data!=[] and not all(x=="" for x in data):
                        c.append(list(filter(lambda x: x!=" ",data)))
            
            return c
        
              
# ************************************** Class for Supplier **********************************************
    
class Supplier(Toplevel):
    
    def __init__(self):
        # ====================== Creating Screen =========================

        super().__init__()
        super().geometry("1110x530+230+135")
        super().minsize(1110,530)
        super().maxsize(1110,530)
        super().config(bg="white")
        super().iconbitmap("icon.ico")
        super().title("Supplier Database")

        # ========================= Heading Label ===============================

        self.l = Label(self,text="Supplier Details",font=("Times New Roman","15","bold"),bg="#000080",fg="white").pack(fill=X,pady=20)

        # ====================== Setting Variables ============================

        self.search = StringVar()
        self.invoice = StringVar()
        self.supp_name = StringVar()
        self.cont_no = StringVar()

        # ======================= Adjusting Entries ===========================

        self.f1 = Frame(self,bg="white")
        
        self.l1 = Label(self.f1,text="Invoice No.",font="lucida 15",bg="white").grid(row=0,column=0,pady=10) 
        self.e1 = Entry(self.f1,font="lucida 12",relief=SOLID,textvar=self.invoice,bg="lightyellow").grid(row=0,column=1,pady=10,padx=10)
        
        self.l2 = Label(self.f1,text="     Supplier Name",font="lucida 15",bg="white").grid(row=1,column=0,pady=10) 
        self.e2 = Entry(self.f1,font="lucida 12",relief=SOLID,textvar=self.supp_name,bg="lightyellow").grid(row=1,column=1,pady=10,padx=10)
        
        self.l3 = Label(self.f1,text="Contact No.",font="lucida 15",bg="white").grid(row=2,column=0,pady=10) 
        self.e3 = Entry(self.f1,font="lucida 12",relief=SOLID,textvar=self.cont_no,bg="lightyellow").grid(row=2,column=1,pady=10,padx=10)
        
        self.l4 = Label(self.f1,text="Description",font="lucida 15",bg="white").grid(row=3,column=0,pady=10) 
        self.t1 = Text(self.f1,width=45,height=10,bg="lightyellow")
        self.t1.grid(row=3,column=1,pady=10,padx=10,sticky=W)
        
        self.b1 = Button(self.f1,text="Save",width=12,font=("goudy old style","13","bold"),bg="#2f9aed",command=self.supp_save).grid(row=4,column=0,padx=25,pady=20)
        self.b2 = Button(self.f1,text="Clear",width=12,font=("goudy old style","13","bold"),bg="#1ceb61",command=self.clear).grid(row=4,column=1,pady=20)
        
        self.f1.pack(side=LEFT,fill=Y,padx=10)

        # ====================== Serach option ===============================================

        self.f2 = Frame(self,bg="white")
        self.lf = LabelFrame(self.f2,relief=GROOVE,text="Searh Supplier",font=("Times New Roman","15"),bg="white")
        
        self.lb1 = Label(self.lf,text="Enter Invoice No.",font=("Times New Roman","14"),bg="white").grid(row=0,column=0,padx=10,pady=5)
        self.en1 = Entry(self.lf,font="lucida 11",relief=SOLID,textvar=self.search,bg="lightyellow").grid(row=0,column=1,pady=5)
        self.bu1 = Button(self.lf,text="Search",font=("goudy old style","13","bold"),bg="#e08d28",width=12,command=self.supp_search).grid(row=0,column=2,padx=10,pady=5)
        
        self.lf.pack(pady=5,side=TOP,ipadx=10)
        self.f2.pack(fill=Y,side=RIGHT,padx=10)

        # ===================== Supplier Record =================================================

        self.f3 = LabelFrame(self.f2,text="Supplier Record",font=("Times New Roman","15"),bg="white")
        
        self.style = ttk.Style()
        self.style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="white",rowheight=25)
        self.style.theme_use("default")
        
        col = ("S.No","Invoice No.","Supplier Name","Contact No.","Description")
        
        self.yscrollbar = Scrollbar(self.f3)
        self.yscrollbar.pack(side=RIGHT,fill=Y,pady=10)
        
        self.treeview = ttk.Treeview(self.f3,height=17,show="headings",columns=col,yscrollcommand=self.yscrollbar.set)
        for i in range(len(col)):
            self.treeview.column(col[i],width=len(col[i])+2,anchor=W)
            
        for i in range(len(col)):
            self.treeview.heading(col[i],text=col[i])
        self.count = 1
        
        self.count = 1
        if os.path.exists("Suppliers.csv"):
            self.suppliers = Supplier.supp_data()
            if len(self.suppliers) > 1:
                for i in self.suppliers[1:]:
                    self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(i[0],i[1],i[2],i[3],i[4]))
                    self.count+=1
        
        self.treeview.pack(fill=BOTH)
        self.f3.pack(fill=BOTH,pady=5)

        # =============================== Screen End =============================================

        self.mainloop() 

        # ========================================================================================  
        
    # ================================ Supplier Data Storing =====================================
    
    def supp_save(self):
       
        # ============================= Entries Var ========================================
       
        self.s = self.search.get()
        self.inv_no = self.invoice.get()
        self.name = self.supp_name.get()
        self.cont = self.cont_no.get()
        self.desc = self.t1.get(1.0,END)
       
        # ==================================================================================
        
        self.yes_no = askyesno("Confirmation","Do you really want to add the data?",parent=self)
        
        if self.yes_no:
        
            try:
            
                if os.path.exists("Suppliers.csv"):
                    
                    self.suppliers = Supplier.supp_data()
                    s = len(self.suppliers)
                
                else:
                    
                    with open("Suppliers.csv","a+",newline="") as f:
                    
                        write = writer(f)
                        write.writerow(["S.No"," ","Supplier's Invoice"," ","Name of Supplier"," ","Contact No."," ","Description"," "])
                        write.writerow([])
                    
                    s = 1
                    
                with open("Suppliers.csv","a+") as f:
                    pass
                
                try:
                        
                    if self.inv_no == "" or self.name=="":
                        raise Exception()
                
                    e = [str(s)," ",self.inv_no," ",self.name," ",self.cont," ",self.desc," "]
                    data = list(map(lambda x:x if x!="" else "N/A",e))
                    
                    if os.path.exists("Suppliers.csv"):
                        
                        self.suppliers = Supplier.supp_data()   
                        if all(x[1] != self.inv_no for x in self.suppliers):
                            
                            with open("Suppliers.csv","a+",newline="") as f:
                            
                                write =writer(f)
                                write.writerow(data)

                            self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,data[2],data[4],data[6],data[8]))
                            self.count+=1
                    
                        else:
                            
                            showerror("Data Error","Supplier already present",parent=self)
                    
                    else:
                        
                        with open("Suppliers.csv","a+",newline="") as f:
                            
                            write =writer(f)
                            write.writerow(data)

                        self.count = 1
                        self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,data[2],data[4],data[6],data[8]))
                        self.count+=1
                        
                except:
                    showinfo("Fields Missing","Invoice number and name are required",parent=self)
            
            except:
                showerror("File Error","Please close the file first",parent=self)
     
    # ================================= Clear Function ===========================================
     
    def clear(self):
      
        self.search.set("")
        self.invoice.set("")
        self.supp_name.set("")
        self.cont_no.set("")
        self.t1.delete("1.0",END)
    
    # ================================ Search Supplier ============================================
    
    def supp_search(self):
        
        try:
            
            with open("Suppliers.csv","r+") as f:
                pass
        
            try:
                
                if self.search.get() != "" and self.search.get() != " ":
                
                    self.sea = self.search.get()
                    self.supplier = list(filter(lambda x:x[1]==self.sea,self.suppliers[1:]))
                  
                    if len(self.supplier) > 0:
                        
                        for record in self.treeview.get_children():
                            self.treeview.delete(record)
                       
                        self.count=1
                       
                        for i in self.supplier:
                            self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(i[0],i[1],i[2],i[3],i[4]))
                            self.count+=1
                    
                    else:
                        
                        showinfo("Not Found","No match found",parent=self)
                        
                else:
                    
                    for record in self.treeview.get_children():
                        self.treeview.delete(record)
                    
                    self.count = 1
                    
                    if os.path.exists("Suppliers.csv"):
                       
                        self.suppliers = Supplier.supp_data()
                        if len(self.suppliers) > 1:
                           
                            for i in self.suppliers[1:]:
                                self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(i[0],i[1],i[2],i[3],i[4]))
                                self.count+=1
                        
            except:
                
                showinfo("Not Found","No match found",parent=self)
            
        except:
            
            showerror("File Error","File is open or not in the directory",parent=self)
            
    # ================================== Method to Extract data from file ===============================
    
    @staticmethod       
    def supp_data():
        
        if os.path.exists("Suppliers.csv"):
            
            with open("Suppliers.csv","r+") as f:
                read = reader(f)
                
                c = []
                for data in read:
                    
                    if data!=[] and not all(x=="" for x in data):
                        c.append(list(filter(lambda x: x!=" ",data)))
           
            return c

# ************************************** Class for Category **********************************************

class Category(Toplevel):
    
    def __init__(self):
        
        # ======================= Creating Screen ================================
        
        super().__init__()
        super().geometry("1110x530+230+135")
        super().minsize(1110,530)
        super().maxsize(1110,530) 
        super().config(bg="white")
        super().iconbitmap("icon.ico")
        super().title("Category Database")
        
        # ========================= Adding Label of the Screen ===============================
        
        self.l = Label(self,text="Manage Product Category",font=("Time New Roman","20","bold"),bg="cyan",fg="white").pack(pady=20,fill=X)
        
        # ======================= Setting Variable s===============================
        
        self.category = StringVar()
        
        #======================= Adjusting Entries ===============================
        
        self.f = Frame(self,bg="white")
        self.l1 = Label(self.f,text="Enter Category Name   ",font=("Times New Roman","15"),bg="white").grid(row=0,column=0,padx=10,pady=10)
        self.e1 = Entry(self.f,font=("Times New Roman",13),textvar=self.category,relief=SOLID,bg="lightyellow").grid(row=1,column=0,pady=20,padx=40)
        self.b1 = Button(self.f,text="ADD",font=("goudy old style","13","bold"),bg="#2f9aed",width=10,command=self.add_cat).grid(row=1,column=1,pady=20,padx=10)
        self.b2 = Button(self.f,text="Delete",font=("goudy old style","13","bold"),bg="#1ceb61",width=10,command=self.delete).grid(row=1,column=2,pady=20,padx=10)
        self.f.pack(padx=20,side=LEFT,fill=Y)
        
        #============================= Category Record ==================================
        
        self.f1 = LabelFrame(self,text="Category Record",font="lucida 15",bg="white")
        
        self.style = ttk.Style()
        self.style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="white",rowheight=25)
        
        self.style.theme_use("default")
        
        
        col = ("S.No","Name")
        
        self.yscrollbar = Scrollbar(self.f1)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        self.treeview = ttk.Treeview(self.f1,height=20,show="headings",columns=col,yscrollcommand=self.yscrollbar.set)
        
        for i in range(len(col)):
            self.treeview.column(col[i],width=80,anchor=CENTER)
            
        for i in range(len(col)):
            self.treeview.heading(col[i],text=col[i])
            
        self.count=1
        self.categories = list(map(lambda x:x[:-4],list(filter(lambda x:x.endswith(".csv") and (x!="Suppliers.csv" and x!="Employees.csv" and x!="Sales.csv"), os.listdir(".")))))
        if len(self.categories)>0:
            for i in self.categories:
                self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i))
                self.count+=1
        
        self.treeview.pack(fill=BOTH)
        self.yscrollbar.config(command=self.treeview.yview) 
            
        self.f1.pack(fill=BOTH,pady=20,padx=20,anchor=E)
        
        #==========================================================================
        self.mainloop()
        
    #================================= Creating File for Category ==========================================
    
    def add_cat(self):
        
        self.cat = self.category.get()
        
        try:
            
            if self.cat == "" or self.cat == " ":
                raise Exception()
            
            if os.path.exists(f"{self.cat}.csv"):
                showinfo("Message","Category already provided",parent=self)
            
            else:
                self.yes_no = askyesno("Confirmation","Do you really want to add the category?",parent=self)
                
                if self.yes_no:
                    with open(f"{self.cat}.csv","a+",newline="") as f:
                        pass
                    
                    self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,self.cat))
                    self.count+=1
        
        except:
            
            showinfo("Name Missing","Please enter the name of category",parent=self)
    
    # ================================ Deleting Category ==============================================
    
    def delete(self):
        
        try:
            
            self.select = self.treeview.selection()
            
            if list(self.select) == []:
                raise Exception()
            
            else:
                
                self.warning = askokcancel("Confirmation","Category file will be deleted. Do you want to continue?",parent=self,icon="warning")
                
                if self.warning:  
                    
                    self.category_name = ""
                    
                    for i in self.select:
                        self.category_name = self.treeview.item(i,"values")[1]
                   
                    os.remove(f"{self.category_name}.csv")
                    self.treeview.delete(self.select)
        
        except:
            showerror("Selection Error","No entry selected",parent=self)
              
# ************************************** Class for Products ***********************************************
        
class Products(Toplevel):
    
    def __init__(self):
    
        # ========================= Creating Screen ====================================
        
        super().__init__()
        super().geometry("1110x530+230+135")
        super().minsize(1110,530)
        super().maxsize(1110,530) 
        super().config(bg="white")
        super().iconbitmap("icon.ico")
        super().title("Products Database")
    
        # ======================== Setting Variable ====================================
        
        self.search = StringVar()
        
        #for category menu
        self.category = StringVar() 
        self.category.set("Select Category")
        self.categories = list(map(lambda x:x[:-4],list(filter(lambda x:x.endswith(".csv")  and (x!="Suppliers.csv" and x!="Employees.csv" and x!="Sales.csv"),os.listdir(".")))))
        
        #for supplier menu
        self.supp = StringVar()  
       
        data = []
        if os.path.exists("Suppliers.csv"):
            data = Supplier.supp_data()
        
        self.suppliers = []
        if data != []:
            self.suppliers = list(map(lambda x:x[2],data[1:])) 
        
        self.supp.set("Select Supplier")
        
        # Other Variables
        self.name = StringVar()
        self.price = StringVar()
        self.qty = StringVar()
        
        # ========================= Adjusting Search ===================================
        
        self.f1 = Frame(self,bg="white")
        
        self.lf = LabelFrame(self.f1,text="Search products",relief=GROOVE,bg="white",font=("Times New Roman","15"))
        
        self.lab = Label(self.lf,text="Enter Category Name",font="lucida 13",bg="white").grid(row=0,column=0,padx=15,pady=5)
        self.e = Entry(self.lf,textvar=self.search,font="lucida 13",relief=SOLID,bg="lightyellow").grid(row=0,column=1,padx=5,pady=5)
        self.b = Button(self.lf,text="Search",font=("goudy old style","13","bold"),bg="#e08d28",width=12,command=self.search_product).grid(row=0,column=2,padx=15,pady=5) 
        
        self.lf.pack(pady=5)
        
        # ==================================== Creating Products Treeview ==============================
        
        self.f2 = LabelFrame(self.f1,text="Products Record",font="lucida 15",bg="white")
        
        self.style = ttk.Style()
        self.style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="white",rowheight=25)
        
        self.style.theme_use("default")
        
        
        col = ("S.No","Category of Product","Supplier Name","Name of Product","Price of the Product","Quantity Available")
        
        self.yscrollbar = Scrollbar(self.f2)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        self.xscrollbar = Scrollbar(self.f2,orient="horizontal")
        self.xscrollbar.pack(side=BOTTOM,fill=X)
        
        self.treeview = ttk.Treeview(self.f2,height=20,show="headings",columns=col,yscrollcommand=self.yscrollbar.set,xscrollcommand=self.xscrollbar.set)
        
        for i in range(len(col)):
            self.treeview.column(col[i],width=80,anchor=CENTER)
            
        for i in range(len(col)):
            self.treeview.heading(col[i],text=col[i])
        
        self.products = []
        for i in self.categories:
            products = Products.data_pro(i)
            for j in products[1:]:
                self.products.append(j)
                
        self.count = 1
        if len(self.products)>0:
            for i in self.products:
                self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5]))
                self.count+=1
        
        self.treeview.pack(fill=BOTH)
        self.yscrollbar.config(command=self.treeview.yview)
        self.xscrollbar.config(command=self.treeview.xview)
        
        self.f2.pack(pady=5,fill=BOTH)
        
        # =============================== End of Treeview and Search Frame  ==================================
        
        self.f1.pack(fill=Y,side=RIGHT,padx=10,pady=10)
    
        # ======================= Heading Products =======================================
       
        self.l =  Label(self,text="Enter Product Details",font=("Times New Roman","15"),bg="#000080",fg="white").pack(side=TOP,fill=X,padx=15,pady=30)
        
        # ======================= Setting Entries ======================================= 
        
        self.f2 = Frame(self,bg="white")
        
        # Categories
        self.l1 = Label(self.f2,text="Category",font="lucida 15",bg="white").grid(row=0,column=0,pady=10,padx=10)
        if self.categories != []:
            self.opt1 = OptionMenu(self.f2,self.category,*self.categories)
            self.opt1.grid(row=0,column=1,pady=10,padx=10)
            self.opt1.config(bg="white",fg="black",font="lucida 12 bold",width=15)
            self.opt1["menu"].config(bg="white",fg="black",font="lucida 12 bold")
        else:
            self.opt1 = OptionMenu(self.f2,self.category,"")
            self.opt1.grid(row=0,column=1,pady=10,padx=10)
            self.opt1.config(bg="white",fg="black",font="lucida 12 bold",width=15)
            self.opt1["menu"].config(bg="white",fg="black",font="lucida 12 bold")
            
        # Suppliers
        self.l2 = Label(self.f2,text="Supplier",font="lucida 15",bg="white").grid(row=1,column=0,pady=10,padx=10)
        if self.suppliers != []:
            self.opt2 = OptionMenu(self.f2,self.supp,*self.suppliers)
            self.opt2.grid(row=1,column=1,pady=10,padx=10)
            self.opt2.config(bg="white",fg="black",font="lucida 12 bold",width=15)
            self.opt2["menu"].config(bg="white",fg="black",font="lucida 12 bold")
        else:
            self.opt2 = OptionMenu(self.f2,self.supp,"")
            self.opt2.grid(row=1,column=1,pady=10,padx=10)
            self.opt2.config(bg="white",fg="black",font="lucida 12 bold",width=15)
            self.opt2["menu"].config(bg="white",fg="black",font="lucida 12 bold")
            
        self.l3 = Label(self.f2,text="Name",font="lucida 15",bg="white").grid(row=2,column=0,pady=10,padx=10)
        self.e3 = Entry(self.f2,textvar=self.name,font="lucida 13",bg="lightyellow",relief=SOLID).grid(row=2,column=1,pady=10,padx=10)
        
        self.l4 = Label(self.f2,text="Price",font="lucida 15",bg="white").grid(row=3,column=0,pady=10,padx=10)
        self.e4 = Entry(self.f2,textvar=self.price,font="lucida 13",relief=SOLID).grid(row=3,column=1,pady=10,padx=10)
        
        self.l5 = Label(self.f2,text="QTY",font="lucida 15").grid(row=4,column=0,pady=10,padx=10)
        self.e5 = Entry(self.f2,textvar=self.qty,font="lucida 13",bg="lightyellow",relief=SOLID).grid(row=4,column=1,pady=10,padx=10)       
        
        self.b1 = Button(self.f2,text="Save",width=12,font=("goudy old style","13","bold"),bg="#2f9aed",command=self.pro_save).grid(row=5,column=0,padx=10,pady=20)
        self.b2 = Button(self.f2,text="Clear",width=12,font=("goudy old style","13","bold"),bg="#1ceb61",command=self.clear).grid(row=5,column=1,pady=20,padx=10)                 
        
        self.f2.pack(fill=Y,side=LEFT,padx=20,pady=10)
    
    # =================================== Product Save ======================================================
    
    def pro_save(self):
       
        # =============================== Arranging Variables ==============================================
        
        self.cat = self.category.get()
        self.sup = self.supp.get()
        self.nam = self.name.get()
        self.pri = self.price.get()
        self.qt = self.qty.get()
       
        # =============================== File Saving =======================================================
           
        try:
            
            with open(f"{self.cat}.csv","r+",newline="") as f:
                pass
            
            try:
                
                if self.cat == "Select Category" or self.sup == "Select Supplier" or self.nam == "" or self.price == "" or self.qt == "":
                    raise Exception()
                
                self.yes_no = askyesno("Confirmation",f"Do you really want to add the product in {self.cat} category?",parent=self)
        
                if self.yes_no:
                
                    products = Products.data_pro(self.cat)
                    s_no = len(products)
                    
                    if s_no==0:
                       
                        with open(f"{self.cat}.csv","a+",newline="") as f:
                         
                            write = writer(f)
                            write.writerow(["S.No"," ","Category of Product"," ","Supplier Name"," ","Name of Product"," ","Price of the Product"," ","Quantity Available"," "])
                            write.writerow([])
                       
                        s_no += 1
                    
                    with open(f"{self.cat}.csv","a+",newline="") as f:
                      
                        write = writer(f)
                        write.writerow([str(s_no)," ",self.cat," ",self.sup," ",self.nam," ",f"Rs.{self.pri}"," ",self.qt," "])
                    
                    self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,self.cat,self.sup,self.nam,f"Rs.{self.pri}",self.qt))
                    self.count+=1
            
            except:
                
                showinfo("Missing Data","Please complete all the fields",parent=self)
    
        except:
            
            showerror("File Error","File not found or the file is open",parent=self)
            
    # ==================================== Clear Fields =====================================================
    
    def clear(self):
      
        self.search.set("")
        self.name.set("")
        self.price.set("")
        self.qty.set("")
        self.category.set("Select Category")
        self.supp.set("Select Supplier")
    
    # ===================================== Search Record =================================================
    
    def search_product(self):
       
        self.sea = self.search.get()
        self.product = list(filter(lambda x:x[1]==self.sea,self.products))
        
        try:
            
            if self.sea != "" and self.sea != " ":
                
                with open(f"{self.sea}.csv","r+"):
                    pass
            
            try:
                
                if self.sea != "" and self.sea != " ":
                    
                    for record in self.treeview.get_children():
                        self.treeview.delete(record)
                    
                    self.count=1
                    for i in self.product:
                        self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5]))
                        self.count+=1
                        
                else:
                    
                    for record in self.treeview.get_children():
                        self.treeview.delete(record)
                        
                    self.count = 1
                    if len(self.products)>0:
                        for i in self.products:
                            self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5]))
                            self.count+=1
                    
            except:
                showinfo("Not Found","No match found",parent=self)
        
        except:
            showerror("File Error","File is open or not in the directory",parent=self)
    
    # =================================== Function for file Read ============================================
    @staticmethod
    def data_pro(filename):
       
        with open(f"{filename}.csv","r+") as f:
           
            read = reader(f)
            c = []
           
            for data in read:
               
                if data!=[] and not all(x=="" for x in data):
                   
                    c.append(list(filter(lambda x: x!=" ",data)))
        
        return c
              
# ************************************** Class for Sales ***************************************************
           
class Sales(Toplevel):
    
    def __init__(self):
        
        # ========================= Creating Screen ====================================
        
        super().__init__()
        super().geometry("1110x530+230+135")
        super().minsize(1110,530)
        super().maxsize(1110,530) 
        super().config(bg="white")
        super().iconbitmap("icon.ico")
        super().title("Sales Database")
        
        # ========================= Search Sold Item ===============================
        
        self.search = StringVar()
        
        self.f1 = LabelFrame(self,text="Search Sold Item",font=("Times New Roman","15"),bg="white")
        
        self.l1 = Label(self.f1,text="Enter Bill No:",font=("lucida","15"),bg="white").grid(row=0,column=0,padx=15,pady=5)
        self.e1 = Entry(self.f1,font="lucida 14",textvar=self.search,bg="lightyellow",relief=SOLID).grid(row=0,column=1,padx=5,pady=5)
        self.b1 = Button(self.f1,text="Search",font=("goudy old style","13","bold"),bg="#2f9aed",width=12,command=self.search_sale).grid(row=0,column=2,padx=15,pady=5)
        
        self.f1.pack(side=TOP,anchor=CENTER,pady=10)
        
        # ========================= Treeview for sold items ============================
    
        self.f2 = LabelFrame(self,text="Sales Record",font="lucida 13")
        
        self.style = ttk.Style()
        self.style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="white",rowheight=25)
        self.style.theme_use("default")
        
        
        col = ("S.No","Bill No","Date","Emp ID","Customer Name","Customer Number","Product Name","Category","Unit Price","Units")
        
        self.yscrollbar = Scrollbar(self.f2)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        self.treeview = ttk.Treeview(self.f2,height=20,show="headings",columns=col,yscrollcommand=self.yscrollbar.set)
        
        for i in range(len(col)):
            self.treeview.column(col[i],width=len(col[i])+2,anchor=W)
            
        for i in range(len(col)):
            self.treeview.heading(col[i],text=col[i])
        
        self.count = 1
        if os.path.exists("Sales.csv"):
            self.sales = Products.data_pro("Sales")
           
            if len(self.sales) > 1:
              
                for i in self.sales:
                  
                    if i == ["S.No","Bill No","Date","Emp ID","Customer Name","Customer Number","Product Name","Category","Unit Price","Units"] :
                        self.sales.remove(i)
               
                for i in self.sales:
                  
                    self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
                    self.count+=1
        
        self.treeview.pack(fill=BOTH)
        self.yscrollbar.config(command=self.treeview.yview)
        
        self.f2.pack(padx=30,pady=10,fill=BOTH)
        
    
        # ================================= End Screen ===============================================
        super().mainloop()
        
    # ================================= Funtion for Search in sales ============================
    
    def search_sale(self):
        
        try:
          
            self.search_sale_item = self.search.get()
           
            if self.search_sale_item != "":
                self.sale = list(filter(lambda x:x[1]==self.search_sale_item,self.sales))
              
                if len(self.sale)!=0:
                
                    for record in self.treeview.get_children():
                       self.treeview.delete(record)
                   
                    self.count=1
                    for i in self.sale:
                        self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(self.count,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
                        self.count+=1
                
                else:
                
                    raise Exception()
        
        except:
          
            showerror("Error","No match found",parent=self)

# ************************************** Class for Cart ****************************************************

class Cart:
    
    cart = [["S.No"," ","Bill No"," ","Date"," ","Emp ID"," ","Customer Name"," ","Customer Number"," ","Product Name"," ","Category"," ","Unit Price"," ","Units"," "]]
    s_no = 1
    
    def __init__(self,bill_no,date,emp_id,customer_name,customer_number,product_name,category,unit_price,units):
        
        self.a = [Cart.s_no," ",bill_no," ",date," ",emp_id," ",customer_name," ",customer_number," ",product_name," ",category," ",unit_price," ",units," "]
        self.cart = list(map(lambda x: x if x!="" else "N/A",self.a))
        Cart.cart.append(self.cart)
        Cart.s_no+=1
    
    #======================================== Add Sales Record to File ====================================== 
           
    def add_to_file(self):
  
        if os.path.exists("Sales.csv"):
          
            with open("Sales.csv","a+",newline="") as f:
           
                write = writer(f)
                write.writerow([])
                write.writerow(Cart.cart[0])
                write.writerow([])
       
        else:
          
            with open("Sales.csv","a+",newline="") as f:
             
                write = writer(f)
                write.writerow(Cart.cart[0])
                write.writerow([])
        
        with open("Sales.csv","a+",newline="") as f:
               
                write = writer(f)
              
                for i in Cart.cart[1:]:
                    write.writerow(i)
                    write.writerow([])
 
    # ========================================= Changing Class Attributes ===================================
     
    @classmethod               
    def remove_cart(cls):
        cls.cart = [["S.No"," ","Bill No"," ","Date"," ","Emp ID"," ","Customer Name"," ","Customer Number"," ","Product Name"," ","Category"," ","Unit Price"," ","Units"," "]]
        cls.s_no = 1      
    
    # ====================================== Function for bill calculation ==================================
    
    @staticmethod
    def calculate():
        if len(Cart.cart)>1:
            prices = list(map(lambda x: float(x[16][3:])*int(x[18]),Cart.cart[1:]))
            return reduce(lambda x,y:x+y,prices)
        else:
            showinfo("Empty Cart","Please purchase some products first",parent=self)
    
# *************************************** Class to See Cart **************************************

class See_Cart(Toplevel,Cart):
    

    def __init__(self):
        
        # =============================== Creating Screen ==============================
        
        super().__init__()
        super().geometry("730x480+350+135")
        super().wm_minsize(600,400)
        super().wm_maxsize(600,400)
        super().iconbitmap("icon.ico")
        
        # =============================== Info Retriving from cart ====================================
        
        if len(super().cart)>1:
            self.cart_show = list(map(lambda x:[x[0],x[12],x[16],x[18],"0",f"Rs.{str(float(x[16][3:])*float(x[18]))}"] ,super().cart[1:]))
        else:
            self.cart_show = []
        
        
        # ===================== Buttons to Remove Data from Cart ======================
        
        self.f1 = Frame(self)
        
        self.b1 = Button(self.f1,text="Remove Item",font="lucida 14",width=15,command=self.remove_item).grid(row=0,column=0,padx=10,pady=2)
        
        self.f1.pack(side=BOTTOM,anchor=CENTER,padx=30,pady=5)
        
        # =============================== Cart Screen ==================================
        
        self.f2 = LabelFrame(self,text="Cart",font="lucida 15")
        self.style = ttk.Style()
        self.style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="white",rowheight=25)
        
        self.style.theme_use("default")
        
        
        col = ("S.No","Product Name","Price","Quantity","Discount (%)","Total Price")
        
        self.yscrollbar = Scrollbar(self.f2)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        self.treeview = ttk.Treeview(self.f2,height=20,show="headings",columns=col,yscrollcommand=self.yscrollbar.set)
        
        for i in range(len(col)):
            self.treeview.column(col[i],width=len(col[i])+2,anchor=W)
            
        for i in range(len(col)):
            self.treeview.heading(col[i],text=col[i])
        
        try:
            self.count=1
            for i in self.cart_show:
                self.treeview.insert(parent="",index="end",iid=self.count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5]))
                self.count+=1
        except:
            showinfo("No Product","Your cart is empty, add some products first",parent=self)
        
        self.treeview.pack(fill=BOTH)
        self.yscrollbar.config(command=self.treeview.yview)
        
        self.f2.pack(padx=10,pady=5,fill=BOTH,ipadx=10)
    
    # ================================= Funtion to Remove Items from Cart ==================================
    
    def remove_item(self):
        
        self.select = self.treeview.selection()
        self.item = []
      
        for i in self.select:
            self.item = list(self.treeview.item(i,"values"))
       
        Cart.cart = list(filter(lambda x: (x[12]!=self.item[1]) or (x[16]!=self.item[2]) or (x[18]!=self.item[3]),Cart.cart))
        
        for i in range(len(super().cart)):
         
            if i>0:
                Cart.cart[i][0] = str(i)
       
        Cart.s_no = len(super().cart)
       
        self.treeview.delete(self.select)
        
        
# ************************************** Main Program *******************************************************

if __name__ == '__main__':
    
    window = Main()
