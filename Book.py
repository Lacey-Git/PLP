class Book:
    def __init__(self,title,author,publication_year,is_available):
        self.title=title
        self.author=author
        self.publication_year=publication_year
        self.is_available = is_available
        
    def check_out(self):

        self.is_available = self.is_avaliable = False
        return 

    def check_in(self):

        self.is_available = self.is_available = True
        
        return self.is_available

    def __str__(self):
        return f"Title:{self.title},Author:{self.author},Year:{self.publication_year},Available:{self.is_available}"

    

    
    

    

   
        
        
