import pandas as pd
import os
from os import listdir
 
#note file csv must be in current working directory

def data_acquire():
    files=[] #array of csv file conatiners
     #obect created from 201 0-9 
    for j in range(9):
        if(j!=2): #2012 missing
            files.append(pd.read_csv(os.getcwd()+"\\csv_files\\ipl201{}.csv".format(j)))
    
    
  
data_acquire()
    