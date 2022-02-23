
# **************************************   ***************************************

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import os
import pickle
from filing import *
from random import randint
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno, showerror, showinfo, askquestion
from Exceptions import *
import PIL.Image

# ******************************************   **************************************


class SellerGui(Tk):
   
    def __init__(self, theme="light grey", seller_info=[]):

        # =========================== Setting up the Screen =======================
        
        super().__init__()
        super().title("seller")
        width = super().winfo_screenwidth()
        height = super().winfo_screenheight()
        super().geometry(f"{width}x{height}")
        # super().iconbitmap(icon)
        super().maxsize(width=1366, height=768)
        super().minsize(width=1366, height=768)
        super().config(background=("#9C27B0"))
        
        # -----------------------------     ------------------------------------
        
        self.credit_label = Label(self, text="Created By", fg="white", bg="grey").pack(side=BOTTOM, fill=X)

        # ========================= 

        self.common_color = theme
        self.seller_info = seller_info
        self.sort_var = StringVar()
        self.count = 1
        self.sort_list = ("category", "any option2")
        self.add_icon_pic = PIL.Image.open("images/add_product.jpeg").resize((20, 20), PIL.Image.ANTIALIAS)
        self.add_icon_pic = ImageTk.PhotoImage(self.add_icon_pic)
        self.shop_lab_image = PIL.Image.open("images/shop_pic.jpeg")
        self.shop_lab_image = self.shop_lab_image.resize((40, 40), PIL.Image.ANTIALIAS)
        self.shop_lab_image = ImageTk.PhotoImage(self.shop_lab_image)

        # =========================
        
        # Label for name of the shop
        print(self.shop_lab_image)
        self.main_lab = Label(self, text=f"{self.seller_info[1]}", font=("Times", "23", "bold"),
                              bd=4, image=self.shop_lab_image,
                              bg=self.common_color, compound=LEFT)
        self.main_lab.pack(fill=X)

        # sub frame for seller options and sort
        self.sort_frame = Frame(self, bg=self.common_color, pady=10, bd=2)
        self.sort_frame.pack(fill=X, pady=5)

        # option menu for sort
        self.sort_lab = Label(self.sort_frame, text="Sort Products By", font=("Times", "13"),
                              bg=self.common_color)
        
        self.sort_option_menu = OptionMenu(self.sort_frame, self.sort_var, *self.sort_list)
        self.sort_option_menu.config(width=5, height=1, relief=RIDGE)
        self.sort_option_menu.pack(side=RIGHT, padx=20)
        self.sort_lab.pack(side=RIGHT, padx=10)

        # buttons inside the frame
        self.button_frame = Frame(self, pady=20, bd=5, bg=self.common_color)
        self.button_frame.pack(fill=Y, side=LEFT, pady=1)

        # add product image on the button
        self.add_product_button = Button(self.button_frame, text="Add Product", padx=20, command=self.add_prod  ,
                                         font=("Times", "18", "bold italic"), activeforeground="white",
                                         relief=GROOVE, bg="#03A9F4", activebackground="#03A9F4",
                                         disabledforeground="white", width=150, fg="white", image=self.add_icon_pic, compound=LEFT)
        self.add_product_button.grid(row=0, column=0, pady=15)


        self.edit_pic = PIL.Image.open("edit_pic.png").resize((20, 20), PIL.Image.ANTIALIAS)
        self.edit_pic = ImageTk.PhotoImage(self.edit_pic)


        self.b2 = Button(self.button_frame, text="Edit Account Info", padx=20, image=self.edit_pic,
                         font=("Times", "18", "bold italic"), compound=LEFT,
                         relief=GROOVE, bg="#03A9F4", fg="white", command=self.edit_info)
        self.b2.grid(row=1, column=0, pady=15)

        self.b3 = Button(self.button_frame, text="View Sales", padx=20,
                         font=("Times", "18", "bold italic"),
                         relief=GROOVE, bg="#03A9F4", fg="white")
        self.b3.grid(row=2, column=0, pady=15)
        
        # ===================================== Treeview for Data =======================================
        
        self.treeview_frame = Frame(self)
        
        # ----------------------------------    ------------------------------
        
        self.style = ttk.Style()
        self.style.configure("Treeview", background="#D3D3D3", foreground="black", fieldbackground="white", rowheight=25)
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading", font=("Times", 15))
        self.style.configure(".", font="Times 12")
        # ---------------------------------   ----------------------------
            
        self.yscrollbar = Scrollbar(self.treeview_frame)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        # -----------------------------------    ------------------------------------------
        
        #
        col = ("S.No", "Product ID", "Category", "Product Name", "Product Price", "Quantity", "Description")
        
        #
        self.treeview = ttk.Treeview(self.treeview_frame, height=29, show="headings", columns=col, yscrollcommand=self.yscrollbar.set)
        
        #
        for i in range(len(col)):
            self.treeview.column(col[i], width=len(col[i])+2, anchor=W)
            
        #
        for i in range(len(col)):
            self.treeview.heading(col[i], text=col[i], anchor=CENTER)

        #
        if os.path.exists(f"Products/{self.seller_info[2]}.csv"):
            self.products = Filing.file_read(dir_name="Products", file_name=self.seller_info[2])
            if len(self.products) > 1:
                for i in self.products[1:]:
                    self.treeview.insert(parent="", index="end", iid=self.count, text="", values=(self.count, i[1], i[2], i[3], i[4], i[5], i[6]))
                    self.count += 1
        
        #
        self.treeview.pack(fill=BOTH)
        #
        self.yscrollbar.config(command=self.treeview.yview)

        #
        self.treeview_frame.pack(fill=BOTH, pady=1)

        # -------------------------------     ----------------------------------------
    
        super().mainloop()

    # ==========================================   ===========================================
    
    def add_prod(self):
        self.add_product_scr = Toplevel()
        
        self.add_product = ProductAdd(self.add_product_scr, seller_info=self.seller_info)
        self.confirm_add_button = Button(self.add_product.add_window, text="Add", command=self.prod_file,
                                    font=("Times", "20"), fg="white",
                                    padx=20, width=10, bg="#FF4081", pady=5)

        self.confirm_add_button.place(x=350, y=555)

        self.add_product_scr.mainloop()

    # ==========================================    ===========================================
    
    def edit_info(self):
        
        self.edit_info_scr = Toplevel()
        
        self.seller_info_edit = SellerInfo(self.edit_info_scr, max_width=1100, max_height=600, title=self.seller_info[2], seller_info=self.seller_info) 

        self.edit_info_scr.mainloop()

    # ========================================   ========================================
    
    def prod_file(self):
        
        self.add_product.filing()
        
        if self.add_product.c != "Select a category" and self.add_product.n != "" and self.add_product.p != "" and self.add_product.q != "" and self.add_product.d != "" and self.add_product.d != "\n":
            self.treeview.insert(parent="", index="end", iid=self.count, text="", values=(self.count, self.add_product.i, self.add_product.c, self.add_product.n, self.add_product.p, self.add_product.q, self.add_product.d))
            self.count += 1




    # ==========================================    ==========================================
        
    @staticmethod
    def callback(newwindow):
        response = messagebox.askokcancel("Quit", "Do you want to close this window?", parent=newwindow)
        if response == 1:  # if window is closed (ok)
            newwindow.grab_release()
            newwindow.destroy()

# ***********************************************   **********************************************

class ProductAdd:
    
    def __init__(self, root=None, max_width=835, max_height=630, seller_info=[]):

        """Opens the top level window for add product button"""

        # ===============================   ===================================
        
        self.add_window = root
        self.add_window.title("Add Product")
        self.add_window.grab_set()
        self.add_window.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self.add_window))
        self.width = self.add_window.winfo_screenwidth()
        self.height = self.add_window.winfo_screenheight()
        self.cen_width = int((self.width/2) - (max_width/2))
        self.cen_height = int((self.height/2) - (max_height/2))
        self.add_window.geometry(f"{max_width}x{max_height}+{self.cen_width}+{self.cen_height}")
        self.add_window.minsize(width=max_width, height=max_height)
        self.add_window.maxsize(width=max_width, height=max_height)
        self.add_window.config(bg="#FFFFFF")

        # ==============================  ======================

        # cat for category of the product
        self.p_id = StringVar()
        self.cat = StringVar()
        self.product_name = StringVar()
        self.product_price = StringVar()
        self.product_quantity = StringVar()
        
        #
        self.pic = ImageTk.PhotoImage(PIL.Image.open("addpic.png").resize((220, 220), PIL.Image.ANTIALIAS))
        self.product_pic_path = ""
        
        #
        self.seller_info = seller_info
        
        # ===========================   =========================
        
        self.header_add_lab = Label(self.add_window, text="Add New Product",
                                    font=("Times", "16", "bold"), bg="light grey")
        self.header_add_lab.pack(fill=X)


        self.add_product_frame = Frame(self.add_window, bd=2, relief=RIDGE)
        self.add_product_frame.place(x=40, y=80)


        self.details_lab = Label(self.add_product_frame, text="Product Details",
                                    font=("Times", "16", "bold"), bg="light grey")
        self.details_lab.grid(row=0, column=0, sticky=EW)

        
        # option menu for the category of products
        self.cat_list = ("Grocery", "Fashion", "Beauty Products", "Computers & Accessories", "Home Appliances")
        self.cat.set("Select a category")


        self.category_menu = OptionMenu(self.add_product_frame, self.cat, *self.cat_list)
        self.category_menu.config(width=20, height=1, relief=RIDGE)
        self.category_menu.grid(row=4, column=2, padx=20)

        # All the labels for adding the product
        self.add_labs_text = ("Product ID", "Select a category", "Product Name",
                 "Product Price (PKR)", "Product Quantity", "Product Description")
        
        for index in range(6):
            self.add_product_labs = Label(self.add_product_frame, text=self.add_labs_text[index],
                                          font=("Times", "13"))
            if index != 5:
                self.add_product_labs.grid(row=index+3, column=0, padx=4, pady=10, sticky=N)
            else:
                self.add_product_labs.grid(row=index+3, column=0, padx=4, pady=10, sticky=N)

        # All the entries for adding the product
        self.add_vars = (self.p_id, self.product_name, self.product_price, self.product_quantity)
        self.p_id.set(f"{randint(10000000000000, 999999999999999)}")
        
        for index in range(4):
            if index !=0:
                self.add_products_entry = Entry(self.add_product_frame, textvar=self.add_vars[index],
                                                relief=RIDGE, bg="#FFFFFF",  width=25)
                self.add_products_entry.grid(row=index+4, column=2, pady=10, padx=20)
            else:
                self.add_products_entry = Entry(self.add_product_frame, textvar=self.add_vars[index],
                                                relief=RIDGE, bg="#FFFFFF",  width=25, 
                                                state=DISABLED, disabledbackground="#CFD8DC")
                self.add_products_entry.grid(row=index+3, column=2, pady=10, padx=20)
                
                
        # Product description text box
        self.product_des = Text(self.add_product_frame, width=55, height=8, wrap=WORD)
        self.product_des.grid(row=9, column=0, columnspan=5, pady=10, padx=10, sticky=NW)
         

        # Product Pic Frame
        self.product_pic_frame = Frame(self.add_window, bd=2, relief=RIDGE, bg="#FFFFFF")
        self.add_pic_lab = Label(self.product_pic_frame, text="Upload Product Photo",
                            font=("Times", "16", "bold"), bg="light grey")
        self.add_pic_lab.pack(fill=X)

        # Creating for the product photo

        self.can_frame = Frame(self.product_pic_frame)
        self.can_frame.pack(pady=20)

        self.default_pic = Label(self.product_pic_frame, image=self.pic)
        self.default_pic.pack()

        # Browse for a photo
        self.browse_button = Button(self.product_pic_frame, text="Browse", font=("Times", "14"),
                            relief=GROOVE, bg="#9E9E9E", fg="white",
                            command=self.browse_photo)
        self.browse_button.pack(pady=5)

        self.product_pic_frame.place(x=580, y=80)

        

    # ==============================================   =================================================    
        
    def browse_photo(self):
        
        """Chooses a picture from the system for the product photo.
        And returns the path of the file photo"""
        
        # -------------------------
        
        self.product_pic_path = askopenfilename(parent=self.add_window, title='Choose a photo', initialdir='/',
                                        filetypes=(("PNG File (*.png)", "*.png"), ("JPEG File (*.jpg)", "*.jpg")))

        # -----------------------------

        if self.product_pic_path != "":
            self.product_pic = ImageTk.PhotoImage(PIL.Image.open(self.product_pic_path).resize((220, 220), PIL.Image.ANTIALIAS))
            self.default_pic.config(image=self.product_pic)
    
    
    # =========================================   ======================================================
    
    def filing(self):
        
        """Stores all the information of the product in the file,
        when add button is pressed"""

        # =========================== 
        
        self.i = self.p_id.get()
        self.c = self.cat.get()
        self.n = self.product_name.get()
        self.p = self.product_price.get()
        self.q = self.product_quantity.get()
        self.d = self.product_des.get(1.0, END)
        self.d = self.d[:-1]

        # =====================================   
        try:

            if self.c != "Select a category" and self.n != "" and self.p != "" and self.q != "" and self.d != "" and self.d != "\n":
                self.confirm = askquestion("Product Confirmation", "Do you confirm this information about the product?", parent=self.add_window)

                if self.confirm == "yes":
                    # -----------------------------

                    self.seller_product_file = Filing(dir_name="Products")
                    self.seller_product_file.general_filing(file_name=self.seller_info[2],
                                                            col_list=["S.No", "Product ID", "Category", "Product Name",
                                                                      "Product Price", "Quantity", "Description"],
                                                            data_list=[self.i, self.c, self.n, self.p, self.q, self.d])


                    self.cat_product_file = Filing(dir_name="Categories")
                    self.cat_product_file.general_filing(file_name=self.c,
                                                         col_list=["Product ID", "Product Name", "Shop Name",
                                                                   "Product Price", "Quantity", "Product Description"],
                                                         data_list=[self.i, self.n, self.seller_info[1], self.p, self.q,
                                                                    self.d])


                    # ------------------------------

                    if self.product_pic_path != "":

                        if os.path.isdir("Product Pics"):
                            self.pic_save = Filing.pic_file_save(dir_name="Product Pics", file_name=self.i, obj=self.product_pic_path)
                        else:
                            os.mkdir("Product Pics")
                            self.pic_save = Filing.pic_file_save(dir_name="Product Pics", file_name=self.i, obj=self.product_pic_path)

                showinfo("Confirmation", "Product has been added successfully", parent=self.add_window)
                self.add_window.update()
                self.p_id.set(f"{randint(10000000000000, 999999999999999)}")
                self.cat.set("Select a category")
                self.product_name.set("")
                self.product_price.set("")
                self.product_quantity.set("")
                self.product_des.delete(1.0, END)
                self.default_pic.config(image=self.pic)
                self.product_pic_path = ""

            else:
                showerror("Invalid Information", "All the fields are required to fill.", parent=self.add_window)

        except:
            showerror("oops!", "oops! Something went wrong!")

    # ==============================================   =========================================


# *************************************************    ****************************************

class SellerInfo:
    
    def __init__(self, root=None, title="User", max_width=1100, max_height=600, seller_info=[], pic=None):
        
        # ================================= Setting Screen =============================================
        
        self.root = root
        self.root.title(f"{title} - Edit Info")
        self.root.grab_set()
        self.root.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self.root))
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.center_width = int((self.screen_width/2) - (max_width/2))
        self.center_height = int((self.screen_height/2) - (max_height/2))
        
        self.root.geometry(f"{max_width}x{max_height}+{self.center_width}+{self.center_height}")
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
        
        self.seller_name = StringVar()
        self.seller_username = StringVar()
        self.seller_email = StringVar()
        self.seller_password = StringVar()
        self.seller_shopname = StringVar()
        self.seller_age = StringVar()
        self.seller_dob = StringVar()
        self.seller_contact = StringVar()
        self.seller_gender = StringVar()
        
        self.seller_name.set(f"{seller_info[0]}")
        self.seller_username.set(f"{seller_info[2]}")
        self.seller_shopname.set(f"{seller_info[1]}")
        self.seller_email.set(f"{seller_info[3]}")
        self.seller_password.set(f"{seller_info[4]}")
        
        
        # ====================================== Fields Frame ==========================================
        
        # seller list is like [name, mall name, username, email, password]
        # Main Frame
        self.fields_frame = Frame(self.root, bd=3, relief=GROOVE)
        
        # Setting Entry Labels
        seller_info_lab = ("Name", "Gender", "Age", "Shop Name", "Contact No.", "D.O.B", "Username", "Email", "Password", "Address")
        for i in range(3):
            for j in range(3):
                self.seller_info_entry_lab = Label(self.fields_frame, text=f"{seller_info_lab[3 * i + j]}", font="Times 16").grid(row=i, column=2 * j, padx=20, pady=15)
                    
        self.seller_info_entry_lab = Label(self.fields_frame, text=f"{seller_info_lab[-1]}", font="Times 16").grid(row=3, column=0, padx=8, pady=15, sticky=N)
        
        # ------------------------ Setting Entries ----------------------
        
        seller_entry_var = (self.seller_name, self.seller_age, self.seller_username, self.seller_email, self.seller_password, self.seller_shopname, self.seller_contact, self.seller_dob)
        
        for i in range(3):
            self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[2 + i], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=2, column=2 * i + 1, padx=8, pady=15)
            if i != 0:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[-3 + i], font="Times 16", width=15).grid(row=1, column=2 * i + 1, padx=8, pady=15)
            else:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[-3 + i], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=1, column=2 * i + 1, padx=8, pady=15)
            if i == 0:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[0], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=0, column=2 * i + 1, padx=8, pady=15)
            elif i == 2:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[1], font="Times 16", width=15).grid(row=0, column=2 * i + 1, padx=8, pady=15)
            
        # Creating Combobox for gender
        self.gender_sel = ttk.Combobox(self.fields_frame, textvar=self.seller_gender, values=("Male", "Female"), font="Times 12", justify=CENTER, state="readonly")
        self.gender_sel.grid(row=0, column=3, padx=8, pady=15)
        self.seller_gender.set("Male")
        
        # Textbox for Address
        self.seller_address_info = Text(self.fields_frame, width=80, height=7, relief=RIDGE, bd=3)
        self.seller_address_info.grid(row=3, column=1, sticky=W, pady=15, columnspan=8)
        
        
        # Packing main frame
        self.fields_frame.pack(pady=55, padx=10)
        
        # =================================== Save Button =============================
        
        self.save_seller_info_button = Button(self.root, text="Save changes", font=("Times", "20"), fg="white",  padx=20, width=10, bg="#FF4081", pady=5, command=self.save_seller_info).pack(pady=10)

    
    # =======================================    ==================================================
        
    def save_seller_info(self):
        # try:
        self.ask = askquestion("Confirm Changes", "Are you sure to save this changes?", parent=self.root)

        if self.ask == "yes":
            # ========================================   =========================================
            self.nam = self.seller_name.get()
            self.user = self.seller_username.get()
            self.mail = self.seller_email.get()
            self.passw = self.seller_password.get()
            self.shop_name = self.seller_shopname.get()
            self.age = self.seller_age.get()
            self.dob = self.seller_dob.get()
            self.cont = self.seller_contact.get()
            self.gender = self.seller_gender.get()
            self.address = self.seller_address_info.get(1.0, END)[:-1]

            # ============================================   ======================================

            if os.path.exists("Accounts Info/Seller Accounts.csv"):

                # -------------------------------   --------------------------

                #
                self.all_seller_data = Filing.file_read(dir_name="Accounts Info", file_name="Seller Accounts")
                self.all_seller_data = self.all_seller_data[1:]
                self.seller_data = []

                #
                for sell_dat in self.all_seller_data:

                    if (sell_dat[7] == self.user and sell_dat[9] == self.passw) or (sell_dat[8] == self.user and sell_dat[9] == self.passw):
                        self.seller_data = sell_dat

                print(self.seller_data)

                #
                if len(self.seller_data) != 0:

                    self.all_seller_data.remove(self.seller_data)

                    self.seller_data_all = []
                    for i in self.all_seller_data:
                        self.seller_data_all.append(i[1:])

                    self.seller_data_all.append([self.nam, self.gender, self.age, self.dob, self.shop_name, self.cont, self.user, self.mail, self.passw, self.address])

                    #
                    for i in self.seller_data_all:
                        for j in range(1,len(i)+len(i)-2,2):
                            i.insert(j, " ")

                    #
                    with open("Accounts Info/Seller Accounts.csv", "w+", newline="") as f:
                        write = writer(f)
                        write.writerow(["S.No", " ", "Name", " ", "Gender", " ", "Age", " ", "Date of Birth", " ", "Shop Name", " ", "Contact No.", " ", "Username", " ", "Email", " ", "Password", " ", "Address"])
                        write.writerow([])
                        for i in range(1, len(self.seller_data_all)+1):
                            write.writerow([str(i), " "]+self.seller_data_all[i-1])

                # ------------------------------------   ---------------------------
                else:
                    self.seller_info_file = Filing("Accounts Info")
                    self.seller_info_file.general_filing(file_name="Seller Accounts", data_list=[self.nam, self.gender, self.age, self.dob, self.shop_name, self.cont, self.user, self.mail, self.passw, self.address], col_list=["Name", "Gender", "Age", "Date of Birth", "Shop Name", "Contact No.", "Username", "Email", "Password", "Address"])

            # -------------------------------------   -----------------------------------
            else:
                self.seller_info_file = Filing("Accounts Info")
                self.seller_info_file.general_filing(file_name="Seller Accounts", data_list=[self.nam, self.gender, self.age, self.dob, self.shop_name, self.cont, self.user, self.mail, self.passw, self.address], col_list=["Name", "Gender", "Age", "Date of Birth", "Shop Name", "Contact No.", "Username", "Email", "Password", "Address"])
            #
            showinfo("Confirmation", "The changes has been saved successfully.", parent=self.root)

        # except:
        # showerror("oops!", "oops! Something went wrong!", parent=self.root)

# ***************************************************   **********************************************

if __name__ == '__main__':

    s = SellerGui(seller_info=["Syed", "Shop name", "username", "email", "password"])

