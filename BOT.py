import numpy as np      #For the array
import json             #For the conversation dataset between the user and the CHATBOT       
import tensorflow as tf #For training our model

from tensorflow import keras #For training our model for our Tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.preprocessing import LabelEncoder

import os 

os.getcwd()
with open('c:\\Users\\Agent Breslin\\Desktop\\ChatBOT -ML\\intents.json') as file:
    data = json.load(file)
# print(data) #The Contents of the JSON File Printed Out


