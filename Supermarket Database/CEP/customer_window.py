from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from datetime import *
import os
from csv import *
from filing import *
import pickle
from seller_window_class import *
from tkinter import ttk
from Cart import *


class CustomerHomePage(Tk):

    def __init__(self, customer_info=[]):
        # =========================== Setting up the Screen =======================
        left_bg = "#FFFFFF"
        super().__init__()
        super().title("customer")
        width = super().winfo_screenwidth()
        height = super().winfo_screenheight()
        super().geometry(f"{width}x{height}")
        # super().iconbitmap(icon)
        super().maxsize(width=width, height=height)
        super().minsize(width=width, height=height)
        super().config(background=("white"))
        
        # =====================================    ==================================
        
        self.customer_info = customer_info
        self.bluejay_pic = ImageTk.PhotoImage(PIL.Image.open("bird.png").resize((90, 90), PIL.Image.ANTIALIAS))
        self.bottom_pic = ImageTk.PhotoImage(PIL.Image.open("images/category.png").resize((290, 260), PIL.Image.ANTIALIAS))
        self.cart_pic = ImageTk.PhotoImage(PIL.Image.open("images/logo1.png").resize((40, 40), PIL.Image.ANTIALIAS))
        self.account_pic = ImageTk.PhotoImage(PIL.Image.open("accountpic.png").resize((40, 40), PIL.Image.ANTIALIAS))
        self.date_time = datetime.now()
        

        # ========================= =================================
        # Title Frame on the left side
        self.left_frame = Frame(self, bg=left_bg, relief=RIDGE, bd=1)

        self.title_lab = Label(self.left_frame, text="BLUE JAY  ", font=("Goudy Old Style", "29", "bold italic"),
                               bg=left_bg, image=self.bluejay_pic, compound=LEFT)
        self.title_lab.pack()

        self.tagline = Label(self.left_frame, text="Where shopping becomes easy!", font=("Chiller", 22, "bold italic"),
                             fg="#2196F3", bg=left_bg)
        self.tagline.pack()

        self.market_lab = Label(self.left_frame, text="Categories", font=("Times", "20", "bold italic"), bg=left_bg)
        self.market_lab.pack(anchor=W, pady=18)

        # ========================================   =============================
        # category buttons frame
        self.cat_frame = Frame(self.left_frame, bg=left_bg)

        self.c1 = Button(self.cat_frame, text="All Categories", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c1)
        self.c2 = Button(self.cat_frame, text="Grocery", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c2)
        self.c3 = Button(self.cat_frame, text="Fashion", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c3)
        self.c4 = Button(self.cat_frame, text="Beauty products", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c4)
        self.c5 = Button(self.cat_frame, text="Computers & Accessories", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c5)
        self.c6 = Button(self.cat_frame, text="Home Appliances", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c6)

        buttons = (self.c1, self.c2, self.c3, self.c4, self.c5, self.c6)
        for i in range(6):
            b = buttons[i]
            b.pack(anchor=W, pady=2)

        self.cat_frame.pack(anchor=W)
        # =================================    =================================
        # bottom left pic
        self.left_pic_frame = Frame(self.left_frame)
        self.bottom_pic_lab = Label(self.left_pic_frame, image=self.bottom_pic)
        self.bottom_pic_lab.pack()

        self.left_pic_frame.pack(side=LEFT)
        self.left_frame.pack(fill=Y, side=LEFT, pady=1)

        #=============================== The Top Frame  ==================================
        self.top_frame = Frame(self, bg=left_bg)

        # ================================   ==============================

        self.top_frame1 = Frame(self.top_frame, bg=left_bg)
        
        self.user_info_button = Button(self.top_frame1, text="View Account", bg="#00BCD4", font=("Comic Sans MS", 16),
                                       image=self.account_pic, compound=LEFT, relief=GROOVE)
        self.history_button = Button(self.top_frame1, text="View Shopping History", bg="#F8BBD0",
                                     font=("Comic Sans MS", 16), relief=GROOVE)
        self.seecart_button = Button(self.top_frame1, image=self.cart_pic, bd=0, bg=left_bg, command=self.show_cart)

        # ======================= log out =======================
        #
        # self.checkout_pic = ImageTk.PhotoImage(PIL.Image.open("checkout_pic.jpg").resize((140, 50), PIL.Image.ANTIALIAS))
        # self.checkout_button = Button(self.top_frame1, image=self.checkout_pic, bd=0, bg=left_bg)
        # self.checkout_button.place(x=900, y=0)
        # ======================   =========================
        self.user_info_button.grid(row=0, column=0, padx=35)
        self.history_button.grid(row=0, column=1, padx=35)
        self.seecart_button.grid(row=0, column=3,  padx=250)
        self.top_frame1.pack(fill=X)

        # ==================================      ==========================
        # login time details
        self.top_frame2 = Frame(self.top_frame, bg=left_bg)
        self.time_details_frame = Frame(self.top_frame2, bg="#2196F3", pady=3, padx=125)

        self.user_lab = Label(self.time_details_frame, text=f"Username: {self.customer_info[2]}",
                              bg="#2196F3", fg="white",
                              font=("Times New Roman", 14)).grid(row=0, column=0)

        self.date_label = Label(self.time_details_frame, bg="#2196F3", fg="white",
                                text=f"Date: {self.date_time.day}/{self.date_time.month}/{self.date_time.year}",
                                font=("Times New Roman", 14), ).grid(row=0, column=1, padx=125)

        self.time_label = Label(self.time_details_frame, bg="#2196F3", fg="white",
                                text=f"Login Time: {self.date_time.strftime('%I:%M:%S %p')}",
                                font=("Times New Roman", 14)).grid(row=0, column=2, padx=125)

        self.time_details_frame.pack(fill=X)

        
        self.top_frame2.pack(fill=X, pady=3)

        self.top_frame.pack(fill=X)



        # ====================================  =====================================
        
        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)

        if os.path.isdir("Categories"):
            
            print("Hello World")
            self.product_pic = ""
            self.categories_list = list(filter(lambda x: x.endswith(".csv"), os.listdir("Categories")))
            self.all_products_pic = []
            self.all_catetegories_data = []
            self.show_product()
   
    # ==========================   =======================

    def show_product(self, cat=""):
        
        # ---------------------    -------------------------------
        self.categories_list = list(filter(lambda x: x.endswith(".csv"), os.listdir("Categories")))
        if cat != "":
            if os.path.exists(f"Categories/{cat}.csv"):
                cat += ".csv"
                self.categories_list = [cat]
            else:
                self.categories_list = []
        
        
        # ---------------------    -------------------------------
        
        # inside product frame
        self.show_prod_canvas = Canvas(self.products_frame, bg="khaki")
        self.show_prod_canvas.pack(side=LEFT, fill=BOTH, expand=1, padx=70, pady=50)
        
        self.scroll_bar = ttk.Scrollbar(self.products_frame, orient="vertical", command=self.show_prod_canvas.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        
        self.show_prod_canvas.config(yscrollcommand=self.scroll_bar.set)
        self.show_prod_canvas.bind("<Configure>", lambda e: self.show_prod_canvas.configure(scrollregion=self.show_prod_canvas.bbox("all")))
        
        self.in_product_frame = Frame(self.show_prod_canvas, bg="khaki")
        self.show_prod_canvas.create_window((0,0), window=self.in_product_frame, anchor=NW)
        
        # -----------------------  ------------------------------
        self.all_products_pic = []
        self.all_catetegories_data = []
        
        for i in self.categories_list:
            self.category_data = Filing.file_read(dir_name="Categories", file_name=i[:-4])
            for j in self.category_data[1:]:
                self.all_catetegories_data.append(j[1:])    # product : [id, name, shop name, price, quantity, description]

        for i in range(len(self.all_catetegories_data)):
            self.product_pic = ""
            if os.path.isdir("Product Pics"):
                if os.path.exists(f"Product Pics/{self.all_catetegories_data[i][0]}.pkl"):
                    self.product_pic = Filing.pic_file_read(dir_name="Product Pics",
                                                            file_name=self.all_catetegories_data[i][0])


                    if self.product_pic.startswith("C:/Users/Imran Hussain/PycharmProjects/main/CEP"):
                        self.product_pic = os.getcwd() + self.product_pic[47:]

                    self.product_pic = PIL.Image.open(self.product_pic)
                    self.product_pic = self.product_pic.resize((300, 200), PIL.Image.ANTIALIAS)
                    self.product_pic = ImageTk.PhotoImage(self.product_pic)

            if self.product_pic == "":
                self.product_pic = "addpic.png"
                self.product_pic = ImageTk.PhotoImage(PIL.Image.open(self.product_pic).resize((300, 200), PIL.Image.ANTIALIAS))

            self.all_products_pic.append(self.product_pic)


            if i % 2 == 0:
                self.product_button = Button(self.in_product_frame, image=self.all_products_pic[i],
                                             text=f"{self.all_catetegories_data[i][1]}\n{self.all_catetegories_data[i][2]}\nRs.{self.all_catetegories_data[i][3]}",
                                             font=("Times", 16, "bold"), bg="khaki", justify=LEFT, anchor=W, pady=5,
                                             compound=TOP, relief=SOLID, bd=2, 
                                             width=300, wraplength=300)
                self.product_button.grid(row=int(i / 2), column=0, padx=70, pady=15, sticky=W)
                self.product_button.config(image=self.all_products_pic[i])
                self.product_button.bind("<Button-1>", self.prod_details)



            else:
                self.product_button = Button(self.in_product_frame, image=self.all_products_pic[i],
                                             text=f"{self.all_catetegories_data[i][1]}\n{self.all_catetegories_data[i][2]}\nRs.{self.all_catetegories_data[i][3]}",
                                             font=("Times", 16, "bold"), justify=LEFT, anchor=W, pady=5,
                                             compound=TOP, relief=SOLID, bd=2, bg="khaki",
                                             width=300, wraplength=300)
                self.product_button.grid(row=int(i / 2), column=1, padx=50, pady=15, sticky=W)
                self.product_button.config(image=self.all_products_pic[i])
                self.product_button.bind("<Button-1>", self.prod_details)

        # =============================     =====================================
    def func_c1(self):
        """The function for all categories to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)

        self.show_product()

    def func_c2(self):
        """The function for grocery to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Grocery.csv"):
            self.show_product(cat="Grocery")
        else:
            self.show_product(cat=" ")

    def func_c3(self):
        """The function for fashion to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Fashion.csv"):
            self.show_product(cat="Fashion")
        else:
            self.show_product(cat=" ")

    def func_c4(self):
        """The function for beauty products to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Beauty Products.csv"):
            self.show_product(cat="Beauty Products")
        else:
            self.show_product(cat=" ")

    def func_c5(self):
        """The function for computer & Accessories to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Computers & Accessories.csv"):
            self.show_product(cat="Computers & Accessories")
        else:
            self.show_product(cat=" ")

    def func_c6(self):
        """The function for home appliances to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Home Appliances.csv"):
            self.show_product(cat="Home Appliances")
        else:
            self.show_product(cat=" ")



        # ==================================    =========================================
    def prod_details(self, event):
        
        self.button_text = event.widget.cget("text")
        self.button_text = self.button_text.strip().split("\n")

        for i in self.all_catetegories_data:
            if (self.button_text[2][3:] == i[3]) and (self.button_text[1] == i[2]) and (self.button_text[0] == i[1]):
                self.button_text = i

        self.each_pic = ""

        if os.path.isdir("Product Pics"):
            if os.path.exists(f"Product Pics/{self.button_text[0]}.pkl"):
                self.each_pic = Filing.pic_file_read(dir_name="Product Pics",
                                                        file_name=self.button_text[0])

                if self.each_pic.startswith("C:/Users/Imran Hussain/PycharmProjects/main/CEP"):
                    self.each_pic= os.getcwd() + self.each_pic[47:]
                
                self.each_pic = PIL.Image.open(self.each_pic)
                self.each_pic = self.each_pic.resize((230, 200), PIL.Image.ANTIALIAS)
                self.each_pic = ImageTk.PhotoImage(self.each_pic)

        if self.each_pic == "":
            self.each_pic= "addpic.png"
            self.each_pic = ImageTk.PhotoImage(PIL.Image.open(self.each_pic).resize((230, 200), PIL.Image.ANTIALIAS))

        self.window = Toplevel(self)
        self.product_detail = ProductInfo(self.window, customer_info=self.customer_info, product_info=self.button_text, product_pic=self.each_pic, c_width=340, c_height=120, max_width=980, max_height=565)
        self.window.mainloop()


    def save_info_customer(self):
        
        self.cust_info_screen = Toplevel()
        self.info_screen = CustomerInfo(self.cust_info_screen, c_width=320, c_height=120, max_width=1020, max_height=565, customer_info=self.customer_info)
        self.cust_info_screen.mainloop()
        
    def show_cart(self):
        
        if len(Cart.Customer_cart) > 0:
           
            self.all_cust_info = Filing.file_read(dir_name="Accounts Info", file_name="Customer Accounts")
            self.customer_account = list( filter(lambda x: x[-1]==self.customer_info[-1] and x[-2]==self.customer_info[-2] and x[-3]==self.customer_info[-3],self.all_cust_info))
            self.customer_account = self.customer_account[0][1:]
            
            self.show_cart_win = Toplevel()
            self.cart_win = ShowCart(self.show_cart_win, customer_info=self.customer_account)
            self.show_cart_win.mainloop()    
        
        


class ProductInfo:

    def __init__(self, root=None, title="", max_width=800, max_height=500, c_width=100, c_height=50, icon=None,
                 windowbg="#FFFFFF", product_info=[], customer_info=[], product_pic=None):
        # =============================================    ===============================

        self.root = root
        self.root.title(title)
        self.root.grab_set()
        self.root.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self.root))

        self.root.geometry(f"{max_width}x{max_height}+{c_width}+{c_height}")
        self.root.maxsize(max_width, max_height)
        self.root.minsize(max_width, max_height)

        if icon != None:
            self.root.iconbitmap(icon)
        self.root.config(bg=windowbg)

        # ========================================    ======================================

        self.customer_info = customer_info
        self.product_info = product_info
        self.prod_info = []
        self.select_quant = StringVar()

        # ============================================    ================================

        self.heading = Label(self.root, text="Product Detail", font=("Times", 20, "bold"), bg="lightgrey").pack(
            side=TOP, fill=X)

        # ===========================================     =================================

        self.pic_prod_frame = Frame(self.root, bg=windowbg, pady=3)
        self.pic_prod_frame.pack(pady=17, padx=10, anchor=NW, fill=X)

        # -----------------------------    -------------------------------

        self.pic_canvas = Canvas(self.pic_prod_frame, width=270, height=230, bg=windowbg)
        self.pic_canvas.pack(side=LEFT, anchor=NW, padx=7)
        self.pic_canvas.create_image(0, 0, image=product_pic, anchor=NW)

        # ------------------------------    ---------------------------------------

        self.pic_des_frame = Frame(self.pic_prod_frame, pady=5, padx=5, width=50, height=50, bg=windowbg)

        self.prod_name_label = Label(self.pic_des_frame, text=f"{self.product_info[1]}", font="Times 17",
                                     wraplength=620, anchor=NW, justify=LEFT, bg=windowbg).pack(anchor=W)
        self.prod_price_lab = Label(self.pic_des_frame, text=f"Rs.{self.product_info[3]}", font="Times 17 bold",
                                    fg="dark orange", bg=windowbg).pack(pady=15, anchor=W)

        ####################################    #########################################

        self.quant_frame = Frame(self.pic_des_frame, pady=3, bg=windowbg)
        self.quant_label = Label(self.quant_frame, text="Quantity:", font="Times 16", bg=windowbg).grid(row=0, column=0)
        self.quant_select = Spinbox(self.quant_frame, from_=1, to=int(self.product_info[-2]), font="Times 12",
                                    textvariable=self.select_quant, state="readonly", readonlybackground="white",
                                    selectbackground="white", selectforeground="black").grid(row=0, column=1, padx=50)
        self.quant_frame.pack(anchor=W, fill=X)

        self.pic_des_frame.pack(fill=X, anchor=NW, padx=7)

        # ----------------------------------    ---------------------------------------

        self.add_cart_button = Button(self.pic_des_frame, text="Add to Cart", font="Times 15", width=15, relief=FLAT,
                                      bg="DarkOrange1", command=self.add_to_cart).pack(pady=32)

        # ======================================    =======================================

        self.prod_des_frame = Frame(self.root, pady=3, padx=5, bg=windowbg)

        self.prod_head_lab = Label(self.prod_des_frame, text=f"Product Details of {self.product_info[1]}",
                                   font="Times 15 bold", anchor=NW, justify=LEFT, bg=windowbg).pack(fill=X, pady=5,
                                                                                                    anchor=NW)
        self.prod_desc = Label(self.prod_des_frame, text=f"{self.product_info[-1]}", font="Times 13", anchor=NW,
                               justify=LEFT, wraplength=720, bg=windowbg).pack(pady=5, anchor=W, fill=X)

        self.prod_des_frame.pack(pady=20, fill=BOTH, padx=10, anchor=NW, side=LEFT)
        
    # =========================================    ========================================
    
    def add_to_cart(self):
        
        self.prod_info = []
        if os.path.exists("Accounts Info/Customer Accounts.csv"):        
            
            self.all_cust_info = Filing.file_read(dir_name="Accounts Info", file_name="Customer Accounts")
            self.customer_account = list(filter(lambda x: x[-1]==self.customer_info[-1] and x[-2]==self.customer_info[-2] and x[-3]==self.customer_info[-3],self.all_cust_info))
            if len(self.customer_account)!=0: 
                self.customer_account = self.customer_account[0][1:]
                self.prod_info = [self.product_info[0], self.product_info[1], self.product_info[2], self.product_info[-3], self.select_quant.get(), self.product_info[-2], self.product_info[-1]]
                print(self.prod_info)
                Cart.Customer_cart.append(self.prod_info)
                
            else:
                showerror("", "", parent=self.root) # add account details first
        
        else:
            showerror("", "", parent=self.root) # add account details first

# *********************************************   ***********************************

class CustomerInfo:
    
    def __init__(self, root=None, title="User", max_width=1100, max_height=600, c_width=200, c_height=100, customer_info=[], pic=None):
        
        # ================================= Setting Screen =============================================
        
        self.root = root
        self.root.title(f"{title} - Edit Info")
        self.root.grab_set()
        self.root.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self.root))
        
        self.root.geometry(f"{max_width}x{max_height}+{c_width}+{c_height}")
        self.root.maxsize(max_width, max_height)
        self.root.minsize(max_width, max_height)
        
        self.root.configure(bg="#FFFFFF")
        
        # ======================================= Heading ================================================= 
        
        if pic != None:
            # heading pic
            self.edit_pic = ImageTk.PhotoImage(PIL.Image.open(pic).resize((32, 32), PIL.Image.ANTIALIAS))
            self.l1 = Label(self.root, text="  Edit Account Info", image=self.edit_pic, compound=LEFT, font=("Times New Roman", 20, "bold"), bg="light grey").pack(fill=X)
        else:
            self.l1 = Label(self.root, text="  Edit Account Info", font=("Times New Roman", 20, "bold"), bg="light grey").pack(fill=X)
            
        # ====================================== Assigning Variables ======================================
        
        self.customer_fname = StringVar()
        self.customer_username = StringVar()
        self.customer_email = StringVar()
        self.customer_password = StringVar()
        self.customer_lname = StringVar()
        self.customer_age = StringVar()
        self.customer_dob = StringVar()
        self.customer_contact = StringVar()
        self.customer_gender = StringVar()
        
        self.customer_fname.set(f"{customer_info[0]}")
        self.customer_username.set(f"{customer_info[2]}")
        self.customer_lname.set(f"{customer_info[1]}")
        self.customer_email.set(f"{customer_info[3]}")
        self.customer_password.set(f"{customer_info[4]}")
        
        
        # ====================================== Fields Frame ==========================================
        
        # customer list is like [name, mall name, username, email, password]
        # Main Frame
        self.fields_frame = Frame(self.root, bd=3, relief=GROOVE)
        
        # Setting Entry Labels
        customer_info_lab = ("First Name", "Gender", "Age", "Last Name", "Contact No.", "D.O.B", "Username", "Email", "Password", "Address")
        
        for i in range(3):
            for j in range(3):
                self.customer_info_entry_lab = Label(self.fields_frame, text=f"{customer_info_lab[3 * i + j]}", font="Times 16").grid(row=i, column=2 * j, padx=20, pady=15)
                    
        self.customer_info_entry_lab = Label(self.fields_frame, text=f"{customer_info_lab[-1]}", font="Times 16").grid(row=3, column=0, padx=8, pady=15, sticky=N)
        
        # ------------------------ Setting Entries ----------------------
        
        customer_entry_var = (self.customer_fname, self.customer_age, self.customer_username, self.customer_email, self.customer_password, self.customer_lname, self.customer_contact, self.customer_dob)
        
        for i in range(3):
            self.customer_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=customer_entry_var[2 + i], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=2, column=2 * i + 1, padx=8, pady=15)
            if i != 0:
                self.customer_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=customer_entry_var[-3 + i], font="Times 16", width=15).grid(row=1, column=2 * i + 1, padx=8, pady=15)
            else:
                self.customer_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=customer_entry_var[-3 + i], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=1, column=2 * i + 1, padx=8, pady=15)
            if i == 0:
                self.customer_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=customer_entry_var[0], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=0, column=2 * i + 1, padx=8, pady=15)
            elif i == 2:
                self.customer_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=customer_entry_var[1], font="Times 16", width=15).grid(row=0, column=2 * i + 1, padx=8, pady=15)
            
        # Creating Combobox for gender
        self.gender_sel = ttk.Combobox(self.fields_frame, textvar=self.customer_gender, values=("Male", "Female"), font="Times 12", justify=CENTER, state="readonly")
        self.gender_sel.grid(row=0, column=3, padx=8, pady=15)
        self.customer_gender.set("Male")
        
        # Textbox for Address
        self.customer_address_info = Text(self.fields_frame, width=80, height=7, relief=RIDGE, bd=3)
        self.customer_address_info.grid(row=3, column=1, sticky=W, pady=15, columnspan=8)
        
        
        # Packing main frame
        self.fields_frame.pack(pady=55, padx=10)
        
        # =================================== Save Button =============================
        
        self.save_customer_info_button = Button(self.root, text="Save changes", font=("Times", "20"), fg="white",  padx=20, width=10, bg="#FF4081", pady=5, command=self.save_customer_info).pack(pady=10)

    
    # =======================================    ==================================================
        
    def save_customer_info(self):

        # ========================================   =========================================
        
        self.fname = self.customer_fname.get()
        self.user = self.customer_username.get()
        self.mail = self.customer_email.get()
        self.passw = self.customer_password.get()
        self.lname = self.customer_lname.get()
        self.age = self.customer_age.get()
        self.dob = self.customer_dob.get()
        self.cont = self.customer_contact.get()
        self.gender = self.customer_gender.get()
        self.address = self.customer_address_info.get(1.0, END)[:-1]

        # ==========================    ======================================================
        
        if self.address!="" and self.address != " " and self.cont != "" and self.cont != " ":
       
            self.ask = askquestion("Confirm Changes", "Are you sure to save this changes?", parent=self.root)

            if self.ask == "yes":
               
                # ============================================   ======================================

                if os.path.exists("Accounts Info/Customer Accounts.csv"):

                     #
                    self.all_customer_data = Filing.file_read(dir_name="Accounts Info", file_name="Customer Accounts")
                    self.all_customer_data = self.all_customer_data[1:]
                    self.customer_data = []

                    #
                    for cust_dat in self.all_customer_data:

                        if (cust_dat[7] == self.user and cust_dat[9] == self.passw) or (cust_dat[8] == self.user and cust_dat[9] == self.passw):
                            self.customer_data = cust_dat
                            
                    #
                    if len(self.customer_data) != 0:

                        self.all_customer_data.remove(self.customer_data)

                        self.customer_data_all = []
                        for i in self.all_customer_data:
                            self.customer_data_all.append(i[1:])

                        self.customer_data_all.append([self.fname, self.lname, self.cont, self.address, self.gender, self.age, self.dob, self.user, self.mail, self.passw])

                        #
                        for i in self.customer_data_all:
                            for j in range(1,len(i)+len(i)-2,2):
                                i.insert(j, " ")

                        #
                        with open("Accounts Info/Customer Accounts.csv", "w+", newline="") as f:
                            write = writer(f)
                            write.writerow(["S.No", " ", "First Name", " ", "Last Name", " ", "Contact No.", " ", "Address", " ","Gender", " ", "Age", " ", "Date of Birth", " ", "Username", " ", "Email", " ", "Password"])
                            write.writerow([])
                            for i in range(1, len(self.customer_data_all)+1):
                                write.writerow([str(i), " "]+self.customer_data_all[i-1])

                    # ------------------------------------   ---------------------------
                    else:
                        self.customer_info_file = Filing("Accounts Info")
                        self.customer_info_file.general_filing(file_name="Customer Accounts", data_list=[self.fname, self.lname, self.cont, self.address, self.gender, self.age, self.dob, self.user, self.mail, self.passw], col_list=["S.No", " ", "First Name", " ", "Last Name", " ", "Contact No.", " ", "Address", " ","Gender", " ", "Age", " ", "Date of Birth", " ", "Username", " ", "Email", " ", "Password"])

                # -------------------------------------   -----------------------------------
                else:
                    self.customer_info_file = Filing("Accounts Info")
                    self.customer_info_file.general_filing(file_name="Customer Accounts", data_list=[self.fname, self.lname, self.cont, self.address, self.gender, self.age, self.dob, self.user, self.mail, self.passw], col_list=["S.No", " ", "First Name", " ", "Last Name", " ", "Contact No.", " ", "Address", " ","Gender", " ", "Age", " ", "Date of Birth", " ", "Username", " ", "Email", " ", "Password"])

                showinfo("Confirmation", "The changes has been saved successfully.", parent=self.root)

        else:
            showerror("", "", parent=self.root)

if __name__ == '__main__':
    
    o = CustomerHomePage(customer_info=["Hamza", "Malik", "hamzamalik", "hamzamalik@gmail.com","hello"])
    o.mainloop()












