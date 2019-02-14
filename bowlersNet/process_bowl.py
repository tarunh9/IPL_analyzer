import pandas as pd
import numpy as np
import operator
file={}
bowls={}
yrs=[12,13,15,16,17,18]
bowls_final={}

def processor():

    
    for i in yrs:
        file[i]=pd.read_csv("20{}_bowlers_ranked.csv".format(i))
    
    basefile=pd.read_csv("2012_bowlers_ranked.csv")
    
    for i in range(basefile.shape[0]):
        name=(basefile.iloc[i])["Player's Name"]
        val=[]
        for n in yrs:
            temp=file[n].iloc[i]
            if(temp["Balls Bowled"]==0):
                val.append(0)
            else:
                temp_value=(1/((float(temp["Economy"])*temp["Balls Bowled"]%100)+temp["Wickets"]))
                val.append(temp_value)
        bowls[name]=val
        
        
 
def predictor():
     yr=np.asarray(yrs)
     basefile=pd.read_csv("2008_bowlers_ranked.csv")  
     for i in range(basefile.shape[0]):
         name=(basefile.iloc[i])["Player's Name"]
         z=np.polyfit(yr,np.asarray(bowls[name]),4)
         z1=np.poly1d(z)
         bowls_final[name]=z1(18)
         
    
         
         
def analyser_bowl():
    processor() 
    predictor()
    final_bowlers= sorted(bowls_final.items(), key=operator.itemgetter(1))
    return(final_bowlers)
        
    
    

final_bowlers_ranklist=analyser_bowl()

          
        
        
            