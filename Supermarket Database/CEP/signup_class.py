
# ****************************************  **************************************

from tkinter import *
from PIL import Image, ImageTk
from filing import *
from Exceptions import *
from seller_window_class import *
import PIL.Image

# ***************************************    **************************************

class Signup_Form:
    
    # =======================================      ==============================================
    
    def customer_signup(self, master=None, geometry="515x485", title="Customer Sign Up", icon = None, image=None, relief=SUNKEN, entry_bg = "#F5F5F5", label_font = "Times 16", bg = "#9C27B0", fname=None, lname=None, username=None, email=None, passw=None, place_x=0, place_y=0):  
        
        # ==========================================    ==========================================
        
        self.root = master
        self.root.geometry(geometry)
        self.root.title(title)
        if icon != None:
                self.root.iconbitmap(icon)
                
        self.root.grab_set()
                
        # Form Frame with fields
        self.form_frame = Frame(self.root, relief=relief, bd=5)
        
        if image != None:
            self.image = ImageTk.PhotoImage(PIL.Image.open(image)).resize((360,600))
            self.image_label = Label(self.form_frame, image = self.image).pack(pady = 10)

        self.signup_form = LabelFrame(self.form_frame, text="SIGN UP", font=("Times", "22", "bold"))

        self.subheader_lab = Label(self.signup_form,
                                   text="Please fill in this form to create an account!",
                                   font="Times 15").pack(side=TOP, anchor="w", pady=10, padx=5)
        
        self.form_entries  = Frame(self.signup_form)
        
        # Label for the fields
        self.fields = ("First name", "Last name", "Username", "Email Address", "Password")

        for field in range(len(self.fields)):
            self.field_label = Label(self.form_entries, font=label_font, text=self.fields[field])
            self.field_label.grid(row=field, column=0, pady=15)

        # Entry for the fields
        self.entries = (fname, lname, username, email, passw)

        for entry in range(len(self.entries)):
            self.field_enter = Entry(self.form_entries, textvar=self.entries[entry],
                                     bg=entry_bg, width=40, relief=SOLID)
            self.field_enter.grid(row=entry, column=1, pady=3, padx=15)
            
        # Sign Up Button
        self.register_button = Button(self.form_frame, text="Sign Up", font=label_font,
                                      relief=SUNKEN, bd=3, padx=20, fg="white", bg="#1976D2").pack(side=BOTTOM, pady=10)


        # packing  widgets
        self.form_entries.pack(pady=5, padx=40)
        self.signup_form.pack(pady=10 ,padx=10)
        self.form_frame.place(x=place_x, y=place_y)
        

    # ===================================     =======================================================

    def seller_signup(self, master=None, geometry="515x485", title="Seller Sign Up", image=None, icon=None, relief=SUNKEN, entry_bg = "#F5F5F5", label_font = "Times 16", bg = "#9C27B0", name=None, mall_name=None, username=None, email=None, passw=None, place_x=0, place_y=0):  
        
        self.root = master
        self.root.geometry(geometry)
        self.root.title(title)
        if icon != None:
                self.root.iconbitmap(icon)
        self.root.grab_set()

        # Form Frame with fields
        self.form_frame = Frame(master, relief=relief, bd=5)
        
        if image != None:
            self.image = ImageTk.PhotoImage(PIL.Image.open(image)).resize((360,600))
            self.image_label = Label(self.form_frame, image = self.image).pack(pady = 10)

        self.signup_form = LabelFrame(self.form_frame, text="SIGN UP", font=("Times", "22", "bold"), labelanchor = "n")

        self.subheader_lab = Label(self.signup_form,
                                   text="Please fill in this form to create an account!",
                                   font="Times 15").pack(side=TOP, anchor="w", pady=10, padx=5)
        
        self.form_entries  = Frame(self.signup_form)
        
        # Label for the fields
        self.fields = ("Name", "Shop name", "Username", "Email Address", "Password")

        for field in range(len(self.fields)):
            self.field_label = Label(self.form_entries, font=label_font, text=self.fields[field])
            self.field_label.grid(row=field, column=0, pady=15)

        # Entry for the fields
        self.entries = (name, mall_name, username, email, passw)

        for entry in range(len(self.entries)):
            self.field_enter = Entry(self.form_entries, textvar=self.entries[entry],
                                     bg=entry_bg, width=40, relief=SOLID)
            self.field_enter.grid(row=entry, column=1, pady=3, padx=15)
            
    

        # packing  widgets
        self.form_entries.pack(pady=5,padx=40)
        self.signup_form.pack(pady=10,padx=10)
        self.form_frame.place(x=place_x, y=place_y)



# *******************************************    **********************************************

class Signup:
    
    def __init__(self, option=None, scr=None):
        
        self.login_system = option
        self.screen = scr
        
        # Entry variables
        self.fname = StringVar()
        self.lname = StringVar()
        self.username = StringVar()
        self.mail = StringVar()
        self.password = StringVar()
        self.shop_name = StringVar()
        self.seller_name = StringVar()
        
        self.sign_up_window = Toplevel(self.screen)
        
        self.signup_window = Signup_Form()
        
        self.sign_up_window.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self.sign_up_window))
           
        if self.login_system == "Seller":
            
            self.signup_window.seller_signup(self.sign_up_window, name=self.seller_name, mall_name=self.shop_name, username=self.username, email=self.mail, passw=self.password)
            # Sign Up Button
            self.register_button = Button(self.signup_window.form_frame, text="Sign Up", font="Times 16",
                                      relief=SUNKEN, bd=3, padx=20, fg="white", bg="#1976D2", command=self.register_user).pack(pady=10)
        
        else:
            self.signup_window.customer_signup(self.sign_up_window, fname=self.fname, lname=self.lname, username=self.username, email=self.mail, passw=self.password)
            # Sign Up Button
            self.register_button = Button(self.signup_window.form_frame, text="Sign Up", font="Times 16",
                                      relief=SUNKEN, bd=3, padx=20, fg="white", bg="#1976D2", command=self.register_user).pack(pady=10)
        
        self.sign_up_window.mainloop()
    
    
    
    def register_user(self):
        
        if self.login_system == "Seller":
            
            # 
            self.name = self.seller_name.get()
            self.mall = self.shop_name.get()
            self.user = self.username.get()
            self.seller_mail = self.mail.get()
            self.seller_pass = self.password.get()            
            
            try:
            
                if self.name=="" or self.mall == "" or self.user=="" or self.seller_mail=="" or self.seller_pass=="":
                    raise A("hmmm")
                
                else:
                    if os.path.exists("Accounts/Seller Accounts.csv"):
                       
                        self.sellers_data = Filing.file_read(dir_name="Accounts", file_name="Seller Accounts")
                        self.sellers_data = self.sellers_data[1:]
                        
                        if all(x[2]!=self.mall for x in self.sellers_data):
                            
                            if all(x[3]!=self.user and x[4]!=self.seller_mail and x[5]!=self.seller_pass for x in self.sellers_data):
                                #
                                self.seller_account_file = Filing("Accounts")
                                self.seller_account_file.general_filing(file_name="Seller Accounts", data_list=[self.name, self.mall, self.user, self.seller_mail, self.seller_pass], col_list=["Name", "Shop Name", "Username", "Email", "Password"])

                                #
                                self.signup_window.root.grab_release()
                                self.sign_up_window.destroy()

                            else:
                                raise B("sff")
                        else:
                            showinfo("mall error","mall name exists")
                    
                    else:
                        
                        #
                        self.seller_account_file = Filing("Accounts")
                        self.seller_account_file.general_filing(file_name="Seller Accounts", data_list=[self.name, self.mall, self.user, self.seller_mail, self.seller_pass], col_list=["Name", "Shop Name", "Username", "Email", "Password"])

                        #
                        self.sign_up_window.root.grab_release()
                        self.sign_up_window.destroy()

            
            except A:
                showinfo("","errrrrrr", parent=self.sign_up_window)
        
            except B:
                showinfo("","rrrrrr", parent=self.sign_up_window)
                       
        else:
            
            # 
            self.f_name = self.fname.get()
            self.l_name = self.lname.get()
            self.user = self.username.get()
            self.customer_mail = self.mail.get()
            self.customer_pass = self.password.get()            
            
            try:
                if self.f_name=="" or self.l_name == "" or self.user=="" or self.customer_mail=="" or self.customer_pass=="":
                  
                    raise A("hmmm")
                
                else:
                    if os.path.exists("Accounts/Customer Accounts.csv"):
                        
                        self.customer_data = Filing.file_read(dir_name="Accounts", file_name="Customer Accounts")
                        self.customer_data = self.customer_data[1:]
                        
                        if all(x[3]!=self.user and x[4]!=self.customer_mail and x[5]!=self.customer_pass for x in self.customer_data):
                            
                            #
                            self.seller_account_file = Filing("Accounts")
                            self.seller_account_file.general_filing(file_name="Customer Accounts",data_list=[self.f_name, self.l_name, self.user, self.customer_mail,self.customer_pass], col_list=["First Name", "Last Name", "Username", "Email", "Password"])

                            #
                            self.signup_window.root.grab_release()
                            self.sign_up_window.destroy()
            
                        else:

                            raise B("haha")        
            
                    else:
                        
                        #
                        self.seller_account_file = Filing("Accounts")
                        self.seller_account_file.general_filing(file_name="Customer Accounts",data_list=[self.f_name, self.l_name, self.user, self.customer_mail,self.customer_pass], col_list=["First Name", "Last Name", "Username", "Email", "Password"])

                        #
                        self.signup_window.root.grab_release()
                        self.sign_up_window.destroy()
        
            
            except A as e:
                showinfo("",e, parent=self.sign_up_window)
        
            except B as e:
                showinfo("",e, parent=self.sign_up_window)
        
        
        