# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras    
from tensorflow.keras.layers import Flatten   
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import regularizers
from keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline



path = "/Users/williamnehemia/Documents/Bangkit-Course/capstone/dataset/exercise_datasetV2.csv"
df = pd.read_csv(path)
print(df.head())
banyak_kategori = len(df.index)

list_berat = []
for i in range(len(df.index)):
  list_berat.append(1)

df['berat'] =  list_berat
dict_df = {'Activity, Exercise or Sport (1 hour)' : [], 'Duration (minutes)': [], 'Calories per kg': [], 'berat' : []}
df_new = df
for index, row in df.iterrows():
  print(index)
  menit = row['Duration (minutes)']
  activity = row['Activity, Exercise or Sport (1 hour)']
  calories = row['Calories per kg']
  for i in range(1,menit):
    for j in range(2,101):
      new_calories = calories*1.0/60*i*j
      list_activity = dict_df.get('Activity, Exercise or Sport (1 hour)')
      list_duration = dict_df.get('Duration (minutes)')
      list_calories = dict_df.get('Calories per kg')
      list_berat = dict_df.get('berat')
      list_activity.append(activity)
      list_duration.append(i)
      list_calories.append(new_calories)
      list_berat.append(j)
      #new_row = pd.DataFrame({'Activity, Exercise or Sport (1 hour)' : [activity], 'Duration (minutes)': [i], 'Calories per kg': [new_calories], 'berat' : [j]})
      
df_curr = pd.DataFrame(dict_df)   
df_new = pd.concat([df_curr, df_new.loc[:]]).reset_index(drop=True)
#df2 = pd.concat([new_row,df.loc[:]]).reset_index(drop=True)
print(df_new.head())
print(df_new.tail())

print(len(df_new.index))
print(df_new.describe())
print(df_new.dtypes)
df_new.rename(columns = {'Activity, Exercise or Sport (1 hour)':'activity', 'Duration (minutes)' : 'durasi' , 'Calories per kg' : 'calories' }, inplace = True)
print(df_new.head())

target = df['Activity, Exercise or Sport (1 hour)']
print(df_new.head())
numeric_feature_names = ['durasi', 'calories', 'berat']
numeric_features = df_new[numeric_feature_names]
numeric_features.head()



jumlah_class = len(df_new['activity'].value_counts())
print(jumlah_class)

df_new['activity'] = df_new['activity'].astype('category')
df_new['activity_category'] = df_new['activity'].cat.codes.astype('category')
print(df_new.head())

df_new_2 = df_new.drop(columns = ['activity', 'Intensity Description', 'activity_category'])
sc = StandardScaler()
x = pd.DataFrame(sc.fit_transform(df_new_2))

df_new_2['durasi'] = MinMaxScaler().fit_transform(np.array(df_new_2['durasi']).reshape(-1,1))
df_new_2['calories'] = MinMaxScaler().fit_transform(np.array(df_new_2['calories']).reshape(-1,1))
df_new_2['berat'] = MinMaxScaler().fit_transform(np.array(df_new_2['berat']).reshape(-1,1))

y = tf.keras.utils.to_categorical(df_new["activity_category"].values, num_classes=jumlah_class)
print(x.values)
print(type(x.values))
print(y)
print(type(y))
y = np.array(df_new['activity_category'])
print(y)
x_train, x_test, y_train, y_test = train_test_split(x.values, y, test_size=0.2)

print(x_train)
print(y_train)
print(x_test)
print(y_test)

x, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=7)
print(x)
print(y)

model = GradientBoostingClassifier(n_estimators = banyak_kategori)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_test_class = np.argmax(y_test, axis=1)
classes_pred = np.argmax(y_pred,axis=1)
report = classification_report(y_test_class, classes_pred, output_dict=True, zero_division=0)
print(report)

# Extract the metrics
precision = report['macro avg']['precision']
recall = report['macro avg']['recall']
f1_score = report['macro avg']['f1-score']
support = report['macro avg']['support']
accuracy = report['accuracy']

print("accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)
print("support" , support)

