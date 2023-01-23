# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:27:32 2022

@author: Daniel
"""
import pandas as pd
#import matplotlib.pyplot as plt

class SubPrimeHome:
    
    def __init__(self,principal,downpayment,int_rate,yr):
        
        self.principal = principal
        self.downpayment = downpayment
        self.int_rate = int_rate / 12
        self.yr = yr

        self.loan_amt = principal - downpayment
        """
        #total monthly payment
        #self.m = int(input("Insert Total Monthly Payment: "))
        
        #add to main
        #amount of your loan
        #self.p = int(input("Insert Principal: "))
        self.p = 500000
        
        self.down_payment = self.p * 0.1
        
        self.p = self.p - self.down_payment
        #interest rate as monthly percentage
        #self.i = float(input("Insert rate: "))
        self.i = 0.038
        self.int_rate = self.i/12
        
        #total amount of months paying off ur mortgage
        #self.time_ = int(input("Months paying off the man's debt: "))
        self.time_ = 15 * 12
        self.time_array=self.create_list(self.time_)
        
        self.amor_table = self.create_dataframe(self.time_,self.time_array)
        
        #self.read_excel_1530 = self.import_excel()
        
        
        #discount rates
        
        
        #self.amor_table2 = self.create_dataframe2(self.time_,self.time_array,self.read_excel_1530)
        
        print("Principal of Loan: ", self.p)
        print("Amor total interest without extra payment: ", self.amor_table.Interest.sum())
        #print("Amor total interest with extra payment: ", self.amor_table2.Interest.sum())
        print("Monthly Payment:",self.amor_table["Monthly"].loc[0])
        print("Cash Payment: ",self.cash_payment)
        print("Yearly Payment: ",self.yearly_payment)
        """
        
        

        

    
    def create_df_to_excel(self,df):
        df.to_csv(r'C:\Users\Daniel\.spyder-py3\Mortgage\amortization.csv')
        
    def create_dataframe(self):
        
        Int_table = pd.DataFrame(data=None,index = range(self.yr*12))
        
        Int_table["Monthly"] = self.loan_amt * self.int_rate * (1 + self.int_rate) ** (self.yr *12) / ( (1 + self.int_rate) ** (self.yr * 12 ) -1 )   
        
        for j,k in enumerate(Int_table.index):
            
            if j == 0:
                Int_table.loc[j,"Principal"] = self.loan_amt
                
            else:
                Int_table.loc[j,"Principal"] = Int_table.loc[j-1,"Post_Payment"]

            Int_table.loc[j,"Interest"] = Int_table.loc[j,"Principal"] * (self.int_rate)
            Int_table.loc[j,"Post_Payment"] = Int_table.loc[j,"Principal"] - (Int_table.loc[j,"Monthly"] - Int_table.loc[j,"Interest"])
            Int_table["Post_Payment"].astype(float).round(2)
        
        pd.options.display.float_format = '{:20,.2f}'.format
        print(Int_table)
        return Int_table
    
    
    def scipigraphy(self,amortable):
        
        
        
        plt.plot(amortable.index,amortable.Principal, label = "Principal")
        plt.plot(amortable.index,amortable.Interest, label = "Interest")
        plt.ylabel("$")
        plt.xlabel("Months")
        plt.legend(loc='best')
        plt.twinx()
        plt.plot(amortable.index,amortable.PM, label = "Principal/Monthly Amor 1",color='red')
        
        #plt.plot(amortable.index,amortable.Beg, label = "Balance")
        
        
        #plt.legend()
        plt.show()
        
    
    
    
    
    def create_dataframe2(self,time,time_array,ready_var):
        
        Int_table = pd.DataFrame(data=None,index = time_array )
        
        Int_table["Monthly"] = self.p * (self.int_rate * (1+self.int_rate)**self.time_) / (( (1+self.int_rate)**self.time_) - 1    )
        
        for j,k in enumerate(Int_table.index):
            
            if j == 0:
                Int_table.loc[j,"Beg"] = self.p
                Int_table.loc[j,"Interest"] = self.p * self.int_rate
            
            elif Int_table.loc[j-1,"Beg"] <= 0:
                Int_table.loc[j,"Beg"] = 0
            
            
            else:
                Int_table.loc[j,"Beg"] = Int_table.loc[j-1,"Beg"] - Int_table.loc[j-1,"Principal"] - ready_var.loc[j-1,"ExtraPay"]
            Int_table.loc[j,"Interest"] = Int_table.loc[j,"Beg"] * (self.int_rate)
            
            Int_table.loc[j,"Principal"] = Int_table.loc[0,"Monthly"] - Int_table.loc[j,"Interest"]
            Int_table.loc[j,"ExtraPayment"] = ready_var.loc[j,"ExtraPay"]  
            Int_table.loc[j,"DCFPrincipal"] = Int_table.loc[j,"Principal"] * (1/((1+self.discount_rate)**(j+1)))
            
            Int_table["PM"] = Int_table.Principal / Int_table.Monthly 
        return Int_table
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def graphy(self,amortable,amortable2):
        
        #plt.plot(amortable.index,amortable.Interest,label ="Interest" )
        #plt.plot(amortable.index,amortable.Principal, label = "Principal")
        plt.plot(amortable.index,amortable.PM, label = "Principal/Monthly Amor 1")
        plt.plot(amortable2.index,amortable2.PM, label = "Principal/Monthly Amor 2")
        plt.ylabel("$")
        plt.xlabel("Months")
        plt.legend()
        plt.show()
    
    
if __name__ == "__main__":
    r = SubPrimeHome(100000,0,0.06,30)
    #r.graphy(r.amor_table,r.amor_table2)
    #r.scipigraphy(r.amor_table)
    r.create_dataframe()
    
         
            
            
            
        
