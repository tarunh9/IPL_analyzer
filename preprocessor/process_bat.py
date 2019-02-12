import pandas as pd
import numpy as np
import operator
file={}
bats={}
yrs=[8,9,10,11,12,13,15,16,17,18]
bats_final={}
def processor():

    file[8]=pd.read_csv("2008_batsman_ranked.csv")
    file[9]=pd.read_csv("2009_batsman_ranked.csv")
    for i in yrs[2:]:
        file[i]=pd.read_csv("20{}_batsman_ranked.csv".format(i))
    
    basefile=pd.read_csv("2008_batsman_ranked.csv")
    
    for i in range(basefile.shape[0]):
        name=(basefile.iloc[i])["Player's Name"]
        val=[]
        for n in yrs:
            temp=file[n].iloc[i]
            if(temp["Ball"]==0):
                val.append(0)
            else:
                temp_value=temp["Strike Rate"]*(temp["Run"]/temp["Ball"])
                val.append(temp_value)
        bats[name]=val
        
        
 
def predictor():
     yr=np.asarray(yrs)
     basefile=pd.read_csv("2008_batsman_ranked.csv")  
     for i in range(basefile.shape[0]):
         name=(basefile.iloc[i])["Player's Name"]
         z=np.polyfit(yr,np.asarray(bats[name]),5)
         z1=np.poly1d(z)
         bats_final[name]=z1(19)
         
    
         
         
def analyser():
    processor() 
    predictor()
    final_bats= sorted(bats_final.items(), key=operator.itemgetter(1))
    return(final_bats)
        
    
    

final_batsmen_ranklist=analyser()

          
        
        
            
