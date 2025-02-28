import logging.config
import ultralytics
import logging
import subprocess
import seaborn as sns 
import matplotlib.pyplot as plt
import os

"""
    This file is where the testing script will reside, the pipeline as well as the loging functions will be in this unique file
    
    Imported libraries:
        Ultralytics: needed for YOLO model 
        loggign: will be used to log the outputs of the model
        seaborn and matplot will be used to plot the data into a visual representaiton
        
    
"""

#logging config
logging.basicConfig(level=logging.INFO, format = '[%(levelname)s] %(message)s')