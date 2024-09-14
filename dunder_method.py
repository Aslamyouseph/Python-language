class auther:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages

    def __len__(self):               #dunder method  for length finding 
        return self.pages
    
    def __str__(self):     #dunder method for string type printting 
        return (f"{self.book_name} by {self.name}")
   
   
    def __call__(self,*arg,**kwargs):  #dunder method for funtion calling 
        print("Hello")

            
    def __del__(self):         #dunde method for delelteing an object  
        print("delete used ")


d=auther("Aslam","pyton",300)
print(len(d))          # calling the cound section  
print(d)                  # calling the string section  
d()                        #calling the funtions section  
del d                           # calling the delete section 