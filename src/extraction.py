"""
extraction.py
CST 2213
Project
David Xu (041173885)    
Description:
Contains data extraction methods
"""

import pandas as pd
from .utility import exception_decorator

#load supermarket inventory or purchase history from .csv
@exception_decorator
def load(path):
    #import the dataset
    df = pd.read_csv(path)  #change to path variable later
    return df