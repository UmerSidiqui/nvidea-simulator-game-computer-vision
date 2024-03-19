import numpy as np
import cv2
import pandas as pd
import tensorflow
import os




def importDataInfo(path):
    columns=['centre','left','right','steering','throttle','brake','speed']
    data=pd.read_csv(os.path.join(path,"driving_log.csv"),names=columns)
    print(data.head)