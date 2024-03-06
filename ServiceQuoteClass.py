class ServiceQuote: 

    def __init__(self,pcharge,lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
        self.__sales_tax = 0 
        self.__total_charges = 0 


    #set the methods 
    def set_parts_charges(self,pcharge):
        self.__parts_charges = pcharge
    
    def set_labor_charges(self,lcharge):
        self.__labor_charges = lcharge

    def set_sales_tax(self, pcharge,lcharge): 
        self.__sales_tax = (pcharge + lcharge) * 0.0825

    def set_total_charges(self, pcharge,lcharge):
        self.__total_charges = self.__sales_tax + pcharge + lcharge 


    #return the value
    def get_parts_charges(self): 
        return self.__parts_charges
    
    def get_labor_charges(self): 
        return self.__labor_charges

    def get_sales_tax(self): 
        return self.__sales_tax
    
    def get_total_charges(self):
        return self.__total_charges
        

