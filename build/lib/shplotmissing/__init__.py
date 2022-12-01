import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno 

def __init__(df:pd.DataFrame):
    '''
    plot missing data.
        1. bar
        2. matrix
    '''
    fig = plt.figure(figsize=((25, 10)))
    font = 12
    for i in range(1,3):
        ax1 = fig.add_subplot(1,2,1)
        missingno.bar(df,color=(0.0, 0.70, 1.00),fontsize=font,ax=ax1)
        ax2 = fig.add_subplot(1,2,2)
        missingno.matrix(df,color=(0.0, 0.70, 1.00),fontsize=font,ax=ax2)
    return plt.tight_layout()
