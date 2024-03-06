class Car: 

    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year

    #set the methods 
    def set_make(self,make):
        self.__make = make
    
    def set_model(self,make):
        self.__model = make

    def set_year(self,y):
        self.__year = y


    #return the value
    def get_make(self): 
        return self.__make
    
    def get_model(self): 
        return self.__model

    def get_year(self): 
        return self.__year
