import numpy as np
import pandas as pd
from typing import List


def txn(df1:str, df2:str):
    """ Function for generating new excel files using the
    similarities and dissimilarities between two files

    Parameters
    ----------
    df1 : first supply list 
        
    df2 : second supply list

    Returns
    -------
    two excel files.

    """
    df1 = pd.read_excel(df1)
    df2 = pd.read_excel(df2)

    dff1 = df1.iloc[:,0].to_list()
    dff2 = df2.iloc[:,0].to_list()

    set_a = set(dff1)
    set_b = set(dff2)

    intersection = set_a.intersection(set_b)
    diff = set_b - set_a

    common_items_list = list(intersection)
    uncommon_items_list = list(diff)

    common_items_dict = {"Name of item": common_items_list}
    uncommon_items_dict = {"Name of item": uncommon_items_list}

    new_df1 = pd.DataFrame(common_items_dict)
    new_df2 = pd.DataFrame(uncommon_items_dict)

    file_1 = new_df1.to_excel("file11.xlsx", index=False)
    file_2 = new_df2.to_excel("file22.xlsx", index=False)

    return file_1, file_2
