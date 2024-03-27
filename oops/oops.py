import pandas as pd
pd.DataFrame()


class RailwayForm:
    formtype = "Railway Form"
    def printData(self):
        print(f"The Name is {self.name}")
        print(f"The Train name is {self.train}")

dipanshusApplication = RailwayForm()     
dipanshusApplication.name = ("Dipanshu")        
dipanshusApplication.train = ("Mahabodhi")
dipanshusApplication.printData()
