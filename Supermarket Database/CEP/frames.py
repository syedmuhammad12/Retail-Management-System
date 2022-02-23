def show_product(self):
    self.lst = [["mango", 40, "80 Rs per kg, sweet and juicy", "mango.jpg"],
                ["Apple", 40, "40 Rs per kg, sweet and fresh", "apples.jpg"],
                ]
    if self.lst:
        # Main product frame where all products are shown

        self.canvas_frame = Frame(self.root)
        self.canvas = Canvas(self.canvas_frame, bg="pink")

        for product in range(len(self.lst)):
            self.show_product_frame = Frame(self.canvas)
            self.pic_frame = Frame(self.show_product_frame)
            self.product_pic = ImageTk.PhotoImage(
                PIL.Image.open(self.lst[product][3]).resize((120, 120), PIL.Image.ANTIALIAS))
            self.product_pic_lab = Label(self.pic_frame, image=self.product_pic)
            self.product_pic_lab.pack()
            self.pic_frame.pack(side=LEFT)

            self.lab1 = Label(self.show_product_frame, text=self.lst[product][0], font=("Times", 18))
            self.lab2 = Label(self.show_product_frame, text=self.lst[product][1], font=("Times", 18))
            self.lab3 = Label(self.show_product_frame, text=self.lst[product][2], font=("Times", 18))
            self.lab1.pack()
            self.lab2.pack()
            self.lab3.pack()
            self.show_product_frame.pack(pady=5)

        self.canvas.pack()

        self.canvas_frame.pack(pady=25)


    else:
        self.nothing_lab = Label(self.root, text="NOTHING TO SHOW")
        self.nothing_lab.pack()

        # ===================================== ============================

from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from datetime import *
import os
from csv import *
from filing import *
import pickle
from seller_window_class import *


class CustomerHomePage:

    def __init__(self, root=None):
        left_bg = "#FFFFFF"
        self.root = root
        self.root.title("Customer")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}")
        # super().iconbitmap(icon)
        self.root.maxsize(width=width, height=height)
        self.root.minsize(width=width, height=height)
        self.root.config(background=("white"))


        # ========================= =================================
        # Title Frame on the left side
        self.left_frame = Frame(self.root, bg=left_bg)

        self.bluejay_pic = ImageTk.PhotoImage(PIL.Image.open("bird.png").resize((90, 90), PIL.Image.ANTIALIAS))
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

        self.c1 = Button(self.cat_frame, text="All Categories", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT)
        self.c2 = Button(self.cat_frame, text="Grocery", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT)
        self.c3 = Button(self.cat_frame, text="Fashion", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT)
        self.c4 = Button(self.cat_frame, text="Beauty products", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT)
        self.c5 = Button(self.cat_frame, text="Computers & Accessories", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT)
        self.c6 = Button(self.cat_frame, text="Home Appliances", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT)

        buttons = (self.c1, self.c2, self.c3, self.c4, self.c5, self.c6)
        for i in range(6):
            b = buttons[i]
            b.pack(anchor=W, pady=2)

        self.cat_frame.pack(anchor=W)
        # =================================    =================================
        # bottom left pic
        self.left_pic_frame = Frame(self.left_frame)
        self.bottom_pic = ImageTk.PhotoImage(PIL.Image.open("images/category.png").resize((290, 260), PIL.Image.ANTIALIAS))
        self.bottom_pic_lab = Label(self.left_pic_frame, image=self.bottom_pic)
        self.bottom_pic_lab.pack()

        self.left_pic_frame.pack(side=LEFT)
        self.left_frame.pack(fill=Y, side=LEFT, pady=1)

        #=============================== The Top Frame  ==================================
        self.top_frame = Frame(self.root, bg=left_bg)

        # ================================   ==============================

        self.top_frame1 = Frame(self.top_frame, bg=left_bg)
        self.cart_pic = ImageTk.PhotoImage(PIL.Image.open("images/logo1.png").resize((40, 40), PIL.Image.ANTIALIAS))
        self.account_pic = ImageTk.PhotoImage(PIL.Image.open("accountpic.png").resize((40, 40), PIL.Image.ANTIALIAS))

        self.user_info_button = Button(self.top_frame1, text="View Account", bg="#00BCD4", font=("Comic Sans MS", 16),
                                       image=self.account_pic, compound=LEFT, relief=GROOVE)
        self.history_button = Button(self.top_frame1, text="View Shopping History", bg="#F8BBD0",
                                     font=("Comic Sans MS", 16), relief=GROOVE)
        self.seecart_button = Button(self.top_frame1, image=self.cart_pic, bd=0, bg=left_bg)

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
        self.date_time = datetime.now()
        self.customer_info = ["1", "2", "My name"]
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



        self.products_frame = Frame(self.root, bg="white")

        if os.path.isdir("Categories"):
            # ==========================   =======================
            # inside product frame
            self.in_product_frame = Frame(self.products_frame, bg="khaki")
            self.in_product_frame.pack(padx=100, pady=100)
            # -----------------------  ------------------------------

            self.categories_list = list(filter(lambda x: x.endswith(".csv"), os.listdir("Categories")))

            self.all_catetegories_data = []
            for i in self.categories_list:
                self.category_data = Filing.file_read(dir_name="Categories", file_name=i[:-4])
                for j in self.category_data[1:]:
                    self.all_catetegories_data.append(j[1:])    # product : [id, name, shop name, price, quantity, description]

            for i in range(len(self.all_catetegories_data)):
                self.product_pic = ""
                if os.path.isdir("Products Pic"):
                    if os.path.exists(f"Products Pic/{self.all_catetegories_data[i][0]}.pkl"):
                        self.product_pic = Filing.pic_file_read(dir_name="Products Pic",
                                                                file_name=self.all_catetegories_data[i][0])

                if self.product_pic == "":
                    self.product_pic = "addpic.png"
                self.product_pic = ImageTk.PhotoImage(PIL.Image.open(self.product_pic).resize((120, 120), PIL.Image.ANTIALIAS))

                if i % 2 == 0:
                    self.product_button = Button(self.in_product_frame, image=self.product_pic,
                                                 text=f"{self.all_catetegories_data[i][1]}\n{self.all_catetegories_data[i][2]}\nRs.{self.all_catetegories_data[i][3]}",
                                                 font=("Times", 16, "bold"),bg="khaki", justify=LEFT, anchor=W, padx=1, pady=8,
                                                 compound=TOP, relief=FLAT, bd=2).grid(row=int(i / 2), column=0)
                else:
                    self.product_button = Button(self.in_product_frame, image=self.product_pic,
                                                 text=f"{self.all_catetegories_data[i][1]}\n{self.all_catetegories_data[i][2]}\nRs.{self.all_catetegories_data[i][3]}",
                                                 font=("Times", 16, "bold"), justify=LEFT, anchor=W, padx=1, pady=8,
                                                 compund=TOP, relief=FLAT, bd=2, bg="white").grid(row=int(i / 2), column=1)

        self.products_frame.pack(side=LEFT, fill=BOTH)




        # ==================================    =========================================
    def prod_details(self, prod_info=[]):
        root = Toplevel(self)
        self.product_deatil = ProductInfo(self, product_info=prod_info)
        root.mainloop()



        # Canvas for category products to show up

        # ==========================    ==================================


class ProductInfo:

    def __init__(self, root=None, title="", max_width=800, max_height=500, c_width=100, c_height=50, icon=None,
                 windowbg="#FFFFFF", product_info=[], seller_info=[], product_pic=None):
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

        self.seller_info = seller_info
        self.product_info = product_info
        self.select_quant = StringVar()

        # ============================================    ================================

        self.heading = Label(self.root, text="Product Detail", font=("Times", 20, "bold"), bg="lightgrey").pack(
            side=TOP, fill=X)

        # ===========================================     =================================

        self.pic_prod_frame = Frame(self.root, bg=windowbg, pady=3)
        self.pic_prod_frame.pack(pady=17, padx=10, anchor=NW, fill=X)

        # -----------------------------    -------------------------------

        self.pic_canvas = Canvas(self.pic_prod_frame, width=230, height=200, bg=windowbg)
        self.pic_canvas.pack(side=LEFT, anchor=NW, padx=7)
        self.pic_canvas.create_image(0, 0, image=product_pic)

        # ------------------------------    ---------------------------------------

        self.pic_des_frame = Frame(self.pic_prod_frame, pady=5, padx=5, width=50, height=50, bg=windowbg)

        self.prod_name_label = Label(self.pic_des_frame, text=f"{self.product_info[1]}", font="Times 15",
                                     wraplength=520, anchor=NW, justify=LEFT, bg=windowbg).pack(anchor=W)
        self.prod_price_lab = Label(self.pic_des_frame, text=f"Rs.{self.product_info[3]}", font="Times 15 bold",
                                    fg="dark orange", bg=windowbg).pack(pady=15, anchor=W)

        ####################################    #########################################

        self.quant_frame = Frame(self.pic_des_frame, pady=3, bg=windowbg)
        self.quant_label = Label(self.quant_frame, text="Quantity:", font="Times 15", bg=windowbg).grid(row=0, column=0)
        self.quant_select = Spinbox(self.quant_frame, from_=1, to=int(self.product_info[-2]), font="Times 12",
                                    textvariable=self.select_quant, state="readonly", readonlybackground="white",
                                    selectbackground="white", selectforeground="black").grid(row=0, column=1, padx=30)
        self.quant_frame.pack(anchor=W, fill=X)

        self.pic_des_frame.pack(fill=X, anchor=NW, padx=7)

        # ----------------------------------    ---------------------------------------

        self.add_cart_button = Button(self.pic_des_frame, text="Add to Cart", font="Times 15", width=15, relief=FLAT,
                                      bg="DarkOrange1").pack(pady=12)

        # ======================================    =======================================

        self.prod_des_frame = Frame(pady=3, padx=5, bg=windowbg)

        self.prod_head_lab = Label(self.prod_des_frame, text=f"Product Details of {self.product_info[1]}",
                                   font="Times 15 bold", anchor=NW, justify=LEFT, bg=windowbg).pack(fill=X, pady=5,
                                                                                                    anchor=NW)
        self.prod_desc = Label(self.prod_des_frame, text=f"{self.product_info[-1]}", font="Times 13", anchor=NW,
                               justify=LEFT, wraplength=720, bg=windowbg).pack(pady=5, anchor=W, fill=X)

        self.prod_des_frame.pack(pady=20, fill=BOTH, padx=10, anchor=NW, side=LEFT)


if __name__ == '__main__':

    root = Tk()
    o = CustomerHomePage(root=root)
    root.mainloop()











