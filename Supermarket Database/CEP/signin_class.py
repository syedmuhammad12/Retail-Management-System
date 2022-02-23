
# ********************************   ************************************

from customer_window import CustomerHomePage
from tkinter import *
from PIL import Image, ImageTk
from filing import *
from seller_window_class import *
from Exceptions import *
import PIL.Image

# ************************** Sign-in class ***************************

class Signin_Form:
    
    # =======================================    ============================================
    
    def signin_form(self, master=None, user_image=None, user_icon=None, pass_icon=None, user_label="Username", bg="white", bd=2, relief=RIDGE, place_x=0, place_y=0):
        
        # user icon image in the username frame
        self.login_frame = Frame(master, bg=bg, relief=relief, bd=bd)  # frame for username & password
       
        if user_image != None:
            self.usericon = ImageTk.PhotoImage(PIL.Image.open(user_image).resize((90, 90), PIL.Image.ANTIALIAS))
            self.usericonlab = Label(self.login_frame, image=self.usericon, bg=bg, bd=0).pack(pady=20)

        self.usernameframe = Frame(self.login_frame, bg=bg)
    
        self.username = StringVar()
        self.password = StringVar()
        
        if user_icon != None:
            self.user_icon = PhotoImage(file=user_icon)
            self.username_lab = Label(self.usernameframe, image=self.user_icon, text=user_label, font="Times 15", compound=LEFT, bg=bg)
            self.username_lab.grid(sticky="w", row=0, column=0, padx=25, pady=10)
        else:
            self.username_lab = Label(self.usernameframe, text=user_label, font="Times 15", bg=bg)
            self.username_lab.grid(sticky="w", row=0, column=0, padx=25, pady=10)    
        
        self.enter_username = Entry(self.usernameframe, textvariable=self.username, relief=SOLID, font=("Times New Roman",15))
        self.enter_username.grid(row=1, column=0, pady=15)
        
        if pass_icon != None:
            self.pass_icon = PhotoImage(file=pass_icon)
            self.passwordlab = Label(self.usernameframe, image=self.pass_icon, text="Password", font="Times 15", compound=LEFT, bg=bg).grid(sticky="w", row=2, column=0, padx=25, pady=15)
        else:
            self.passwordlab = Label(self.usernameframe, text="Password", font="Times 15", bg=bg).grid(sticky="w", row=2, column=0, padx=25, pady=10)
            
        self.enter_password = Entry(self.usernameframe, textvariable=self.password, relief=SOLID, font=("Times New Roman",15))
        self.enter_password.grid(row=3, column=0, pady=10, padx=30)
        
        self.usernameframe.pack(padx=25)
        
        # self.f1 = Frame(self.login_frame, bg=bg)
        
        # self.l1 = Label(self.f1, bg="lightgrey", bd=0, width=13).grid(row=0, column=0)
        # self.l2 = Label(self.f1, text="OR", fg="lightgrey", bg=bg, font= ("Times New Roman", 13)).grid(row=0, column=1, padx=3)
        # self.l3 = Label(self.f1, bg="lightgrey", height=0, bd=0, width=13).grid(row=0, column=2)
        
        # self.f1.pack(pady=10)
        
        # self.f2 = Frame(self.login_frame)
        
        
        # self.f2.pack(pady=10)
        
        self.login_frame.place(x=place_x, y=place_y)
        
    # ======================================      ===========================================
        
    def signup_ask(self, master=None, width=320, height=60, bg="white", bd=2, relief=RIDGE, place_x=0, place_y=0):
        
        self.ask_signup = Frame(master, bg=bg, bd=bd, relief=relief)
        
        self.ask_label = Label(self.ask_signup, text="Don't have an account?", font=("Times New Roman",13,"bold"), bg=bg).grid(row=0, column=0, pady=15, padx=15)
        
        self.ask_signup.place(x=place_x, y=place_y, width=width, height=height)
        
# ***************************************   ****************************************

class Signin:
    
    def __init__(self, username=None, password=None, scr=None):
        
        self.username = username
        self.password = password
        self.screen = scr
    
    def seller_signin(self):
        
        if os.path.exists("Accounts/Seller Accounts.csv"):
         
            #try:
                
            with open("Accounts/Seller Accounts.csv") as f:
                pass
            
            self.seller_dat = Filing.file_read(dir_name="Accounts", file_name="Seller Accounts")
            self.seller_dat = self.seller_dat[1:]
            self.seller_data = []
            for i in self.seller_dat:
                if (i[3] == self.username and i[5] == self.password) or (i[4] == self.username and i[5] == self.password):
                    self.seller_data = i
                                    
            if len(self.seller_data) == 0:
                showinfo("User Not Found", "Please make a new account or enter correct information")
            else:
                self.seller_data = self.seller_data[1:]
                self.screen.destroy()
                self.seller_screen = SellerGui(theme="lightgrey", seller_info=self.seller_data)
                    
            
            # except:
            #     showerror("File Error", "Please close the file first")
        
        else:
            showerror("No file found", "Please Create an account")
    
    
    def customer_signin(self):
        
        if os.path.exists("Accounts/Customer Accounts.csv"):
        
            # try:
                    
            with open("Accounts/Customer Accounts.csv", "r") as f:
                pass
        
            self.customer_dat = Filing.file_read(dir_name="Accounts", file_name="Customer Accounts")
            self.customer_dat = self.customer_dat[1:]
            self.customer_data = []
            for i in self.customer_dat:
                if (i[3] == self.username and i[5] == self.password) or (i[4] == self.username and i[5] == self.password):
                    self.customer_data = i
        
            if len(self.customer_data) == 0:
                showinfo("User Not Found", "Please make a new account or enter correct information")
            else:
                self.customer_data = self.customer_data[1:]
                self.screen.destroy()
                self.customer_screen = CustomerHomePage(customer_info=self.customer_data)
                
            # except:
            #     showerror("File Error", "Please close the file first")
        
        else:
            showerror("No file found", "Please Create an account")
        
        