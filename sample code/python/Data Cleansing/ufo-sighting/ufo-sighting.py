import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

data_dir = 'D:\\repo\\big-data-course\\sample code\\python\\Data Cleansing\\ufo-sighting\\data\\'
ufo = pd.read_csv(os.path.join(data_dir, 'complete.csv'))
