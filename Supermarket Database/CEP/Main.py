# ************************************** Importing Modules ********************************************

import os
from tkinter.messagebox import showerror, showinfo, askyesno, showwarning
from filing import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from signin_class import *
from signup_class import *
from seller_window_class import *
from Exceptions import *
import PIL.Image


class Main(Tk):
    
    def __init__(self, title="My Window", icon="", max_width= 900, max_height=650, windowbg="#9C27B0"):
        
        # ==================================    =====================================================
        
        super().__init__()
        super().title(title)
        
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.center_width = int((self.screen_width/2) - (max_width/2))
        self.center_height = int((self.screen_height/2) - (max_height/2))
        
        super().geometry(f"{max_width}x{max_height}+{self.center_width}+{self.center_height}")
        #super().iconbitmap(icon)
        super().maxsize(width=max_width, height=max_height)
        super().minsize(width=max_width, height=max_height)
        super().config(background=(windowbg))
        
        # =========================================    ======================================

        # title pic
        self.titlepiccan = Canvas(self, width=400, height=650, bg="white")
        self.titlepiccan.pack(side=LEFT)
        
        self.titlepic = ImageTk.PhotoImage(PIL.Image.open("phone.png").resize((400, 500), PIL.Image.ANTIALIAS))
        self.titlepiccan.create_image(0, 0, anchor="nw", image=self.titlepic)

        # title name and login part
        self.titlelab = Label(self, text="Welcome To\nVirtual shoping Cart",
                       font=("Times", "30", "italic"), bg=windowbg).pack(pady=10)
      
        # =====================================    ==========================================
         
        self.options = ("Customer", "Seller")
        self.option = StringVar()
        self.frame_option = ttk.Combobox(self, textvar=self.option, values=self.options, font=("goudy old style", 13), justify=CENTER, state="readonly")
        self.frame_option.current(0)
        self.frame_option.bind("<<ComboboxSelected>>", self.comboclick)
        self.frame_option.place(x=520, y=115)  
        
        
        # ==================================    ===================================

        # user icon image in the username frame
        self.signin_form_customer = Signin_Form()
        
        self.signin_form_customer.signin_form(self, user_image="login.png", user_icon="user_icon.png", pass_icon="pass_icon.png", place_x=460, place_y=150)
        
        self.login_button = Button(self.signin_form_customer.login_frame, text="Sign In", font="Times 16",
                                      relief=SUNKEN, bd=3, padx=20, width=14, fg="white", bg="#1976D2", command=self.signin)
        self.login_button.pack(pady=20)
        
        # ===================================     ==================================
        
        self.signin_form_customer.signup_ask(self, place_x=460, place_y=580)
        self.sign_up_button = Button(self.signin_form_customer.ask_signup, text="Sign Up", font=("Times New Roman",13,"bold"), bg="white", fg="#00759E", relief=FLAT, activebackground="white", activeforeground="#00759E", command=self.signup)
        self.sign_up_button.grid(row=0, column=1, pady=15)
        
    # ==========================================    ===============================================         
    
    def signin(self):
        
        self.login_system = self.option.get()
        self.username_data = self.signin_form_customer.username.get()
        self.password_data = self.signin_form_customer.password.get()        
        
        if self.login_system == "Seller":
            
            self.seller_sign_in = Signin(username=self.username_data, password=self.password_data, scr=self)
            self.seller_sign_in.seller_signin()
            #self.seller_logout_button = Button(self.seller_sign_in.seller_screen, command=self.seller_logout).place()
                
                    
        else:
            
            self.customer_sign_in = Signin(username=self.username_data, password=self.password_data, scr=self)
            self.customer_sign_in.customer_signin()
            #self.customer_logout_button = Button(self.seller_sign_in.seller_screen, command=self.seller_logout).place()
                
            
    # =========================================    ===========================================
            
    def signup(self):
        
   
        self.login_system = self.option.get()
        
        self.signup_user = Signup(scr=self, option=self.login_system)
        
    # =================================    ===============================================
    
    def seller_logout(self):
        
        self.seller_screen.destroy()
        Main()
    
    # ===================================   ===============================================
    
    def comboclick(self, event):
        
        self.login_system = self.option.get()
        
        if self.login_system == "Seller":
            self.signin_form_customer.username_lab["text"] = "Email"
        else:
            self.signin_form_customer.username_lab["text"] = "Username"
        
        
    # =================================    =====================================================
    
    



if __name__ == '__main__':
    
    Gui = Main()
    Gui.mainloop()
    


