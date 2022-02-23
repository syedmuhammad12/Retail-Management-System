

class A(Exception):
    
    def __init__(self, message):
        
        self.message = message
        
    
    
class B(Exception):
    
    def __init__(self, message):
        
        self.message = message
        
    

class C(Exception):
    
    def __init__(self, message):
        
        self.message = message
        
    def __str__(self):
        
        return self.message

class D(Exception):

    def __init__(self, message):
        
        self.message = message
        
    def __str__(self):
        
        return self.message