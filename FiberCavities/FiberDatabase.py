import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class FibersDatabase(object):
    def __init__(self,fileLocation=r"C:\Users\bmehl\Desktop\Fibers_Database.xlsx",sheetName= "2019"):
        self.database = pd.read_excel(fileLocation,sheet_name=sheetName)
        self.database['NA'] = self.database['Dia-Avg']/(self.database['ROC-Avg'])
        self.fibersRemoved()
        self._smallestROC = self.database['ROC-Avg'].min()
        self._largestROC = self.database['ROC-Avg'].max()
        self._smallestDia = self.database['Dia-Avg'].min()
        self._largestDia = self.database['Dia-Avg'].max()
        self._smallestEllipticity = self.database['Ellipticity'].min()

    def minimumROC(self):
        return self._smallestROC

    def acceptableNA(self,NA):
        """
        The idea of this function is to identify the fibers which
        have NA that are considered acceptable for the experiment
        """
        print(self.database[self.database['NA']>=NA])

    def acceptableROC(self,ROC):
        """
        The idea of this function is to identify the fibers which
        have ROC that are considered acceptable for the experiment
        """
        print(self.database[self.database['ROC-Avg']>=ROC])

    def acceptableDiameter(self,diameter):
        """
        The idea of this function is to identify the fibers which
        have diameter that are considered acceptable for the experiment
        """
        print(self.database[self.database['Dia-Avg']>=diameter])

    def fibersRemoved(self):
        """
        This function is used to remove all fibers that
        are either in use in an experiment or do not exist any longer
        """
        self.database = self.database[pd.isnull(self.database['Date Removed'])]

    def head(self,entries=5):
        print(self.database.head(entries))

    def head(self,entries=5):
        print(self.database.tail(entries))

if __name__ == "__main__":
    database = FibersDatabase()
    print(database.database.head())
    database.minimumROC()
