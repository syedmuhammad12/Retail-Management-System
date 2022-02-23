from csv import *
import os
from tkinter.messagebox import showerror, showinfo
import pickle


class Filing:
    
    def __init__(self, dir_name="Accounts"):
        
        self.dir_name = dir_name
        
    def general_filing(self, file_name="customer", data_list=[], col_list = []):
        
        self.file_name = file_name
        
        if os.path.isdir(self.dir_name):
            
            if os.path.exists(self.dir_name+"/"+self.file_name+".csv"):
                
                try:
                    
                    with open(self.dir_name+"/"+self.file_name+".csv", "r") as f:
                        pass
                    
                    self.data_file_list = Filing.file_read(dir_name=self.dir_name, file_name=self.file_name)
                    self.s_no = len(self.data_file_list)
                    self.accounts_file_structure(self.s_no, col_list=col_list, data_list=data_list)
               
                
                except:
                    showerror("Open File", "Please close the file first")

            else:
                
                self.accounts_file_structure(s_no=1, col_list=col_list, data_list=data_list)
            
        else:
            
            os.mkdir(self.dir_name)
            self.accounts_file_structure(s_no=1, col_list=col_list, data_list=data_list)
        
    
    def accounts_file_structure(self, s_no=1, col_list=[], data_list=[]):
        
        try:
            
                                    
            self.data_list = data_list
            self.col_list = col_list
            
            self.col_list.insert(0, "S.No")
            for i in range(1, len(self.col_list)+len(self.col_list)-2, 2):
                self.col_list.insert(i, " ")
            
            self.data_list.insert(0, s_no)
            for i in range(1, len(self.data_list)+len(self.data_list)-2, 2):
                self.data_list.insert(i, " ")
                
            

            if os.path.exists(self.dir_name+"/"+self.file_name+".csv"):
                with open(self.dir_name+"/"+self.file_name+".csv", "a+", newline="") as f:
                    write = writer(f)
                    write.writerow(self.data_list)

            else:
                
                with open(self.dir_name+"/"+self.file_name+".csv", "a+", newline="") as f:
                    write = writer(f)
                    write.writerow(self.col_list)
                    write.writerow([])
                    write.writerow(self.data_list)
                            
                
        except:
        
            showinfo("Missing Field","All fields are required")
            
    
                    
    
    @staticmethod
    def file_read(dir_name=None, file_name=None):

        data = []
        with open(f"{dir_name}/{file_name}.csv", "r+") as f:
            
            read = reader(f)
            for dat in read:
                if dat != [] and not all(x=="" for x in dat):
                    data.append(list(filter(lambda x: x!=" ",dat)))
        return data
        

    @staticmethod
    def pic_file_save(dir_name=None, file_name=None, obj=None):
        
        with open(f"{dir_name}/{file_name}.pkl", "wb") as f:
            pickle.dump(obj, f)
    
    
    @staticmethod
    def pic_file_read(dir_name=None, file_name=None):
        
        obj = None
        with open(f"{dir_name}/{file_name}.pkl", "rb") as f:
            obj = pickle.load(f)
        
        return obj