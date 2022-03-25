import pandas as pd
import janitor #Clean APIs for data cleaning. 
import datetime

from IPython.core.display import display, HTML
from pyvis import network as net
import networkx as nx

df_ori = pd.read_csv("Connections.csv", skiprows=2) #The original csv file has notes on the first two rows, so we’re reading starting from line 3
df_ori.info()

#Data cleaning:
df = (
    df_ori
    .clean_names() # remove spacing and capitalization
    .drop(columns=['first_name', 'last_name', 'email_address']) # drop for privacy
    .dropna(subset=['company', 'position']) # drop missing values in company and position
    .to_datetime('connected_on', format='%d %b %Y')
  )
df.head()