import numpy as np
import pandas as pd
def chknull(a):
        """a=data_frame """
        nullval={}
        naval=a.isna().sum()
        pd.DataFrame(naval)
        for i in range (len(naval+1)):
            if naval.iloc[i]>0:
                #nullval.append(naval.iloc[i:i+1])
                nullval.update({naval.index[i]:naval.iloc[i]})
        return  nullval
def chktyp(a):
        """a=data_frame"""
        dtypes=a.dtypes
        pd.DataFrame(dtypes)
        lis={}
        for i in range (len(dtypes)):
            if dtypes.iloc[i]==object:
                lis.update({dtypes.index[i]:dtypes.iloc[i]})
        return lis
def convert_string(string_lis,file):
        """string_lis=dtype should be list 
        file=data_frame"""
        #first need to convert 1d array into 2d array
        Lis=np.reshape(string_lis,(-1,1))
        #Use pandas dummy function to convert string into to int
        for i in Lis:
                file[i]=pd.get_dummies(i)
        return file
def fill_na(file):
        """file=data_frame"""
        #fill nullvalues with mean value
        df=file.fillna(file.mean())
        return df