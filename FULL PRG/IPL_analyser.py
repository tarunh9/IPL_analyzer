import pandas as pd
import numpy as np
import operator
file={}
bats={}
yrs=[12,13,15,16,17,18]
bats_final={}

bowls={}
bowls_final={}

def processor_bat():

   
    for i in yrs:
        file[i]=pd.read_csv("20{}_batsman_ranked.csv".format(i))
    
    basefile=pd.read_csv("2012_batsman_ranked.csv")
    
    for i in range(basefile.shape[0]):
        name=(basefile.iloc[i])["Player's Name"]
        val=[]
        for n in yrs:
            temp=file[n].iloc[i]
            if(temp["Ball"]==0):
                val.append(0)
            else:
                temp_value=temp["Strike Rate"]*temp["Ball"]
                val.append(temp_value)
        bats[name]=val
        
        
 
def predictor_bat():
     yr=np.asarray(yrs)
     basefile=pd.read_csv("2012_batsman_ranked.csv")  
     for i in range(basefile.shape[0]):
         name=(basefile.iloc[i])["Player's Name"]
         z=np.polyfit(yr,np.asarray(bats[name]),5)
         z1=np.poly1d(z)
         bats_final[name]=z1(19)
         
    
         
         
def analyser_bat():
    processor_bat() 
    predictor_bat()
    final_bats= sorted(bats_final.items(), key=operator.itemgetter(1),reverse=True)
    return(final_bats)
        
#======================#


def processor_bowl():

    
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
                temp_value=(1/((float(temp["Economy"])*temp["Balls Bowled"])))
                val.append(temp_value)
        bowls[name]=val
        
        
 
def predictor_bowl():
     yr=np.asarray(yrs)
     basefile=pd.read_csv("2012_bowlers_ranked.csv")  
     for i in range(basefile.shape[0]):
         name=(basefile.iloc[i])["Player's Name"]
         z=np.polyfit(yr,np.asarray(bowls[name]),5)
         z1=np.poly1d(z)
         bowls_final[name]=z1(19)
         
    
         
         
def analyser_bowl():
    processor_bowl() 
    predictor_bowl()
    final_bowlers= sorted(bowls_final.items(), key=operator.itemgetter(1),reverse=True)
    return(final_bowlers)
        
    





def main():
    final_batsmen_ranklist=analyser_bat()  #list of all batsmen
    final_bowlers_ranklist=analyser_bowl() #list of all bowlers
    
    print("Batsmen top 10")
    for i in final_batsmen_ranklist[:10]:
        print(i[0])
    print("\n\nBowlers, top 10")
    for i in final_bowlers_ranklist[:10]:
        print(i[0])
        
main()        
        
            
