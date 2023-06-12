#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:19:45 2023

@author: williamnehemia
"""

# -*- coding: utf-8 -*-


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
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras import regularizers
from keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
from sklearn.preprocessing import StandardScaler





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





#est = KerasClassifier(build_fn= get_base_model, epochs=200, batch_size=5, verbose=0)

#kfold = KFold(n_splits=5, shuffle=True)



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

x_train, x_test, y_train, y_test = train_test_split(x.values, y, test_size=0.2)

print(x_train)
print(y_train)
print(x_test)
print(y_test)

from keras.engine import sequential
def get_model():
    model =  tf.keras.Sequential([
        
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dense(128, activation='relu'),
        
        Dense(128, activation='relu'),
        BatchNormalization(),
        
        
        
        
        
        
        
        Dense(banyak_kategori, activation='softmax')
    ])
    
    optimizer = Adam(learning_rate=0.01)

    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

#x_train=np.asarray(x_train).astype(np.int)

#y_train=np.asarray(y_train).astype(np.int)

my_callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=2),
    tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
    tf.keras.callbacks.TensorBoard(log_dir='./logs'),
]

model = get_model()

model_fit = model.fit(x_train, 
                      y_train, 
                      epochs = 100,
                      validation_data = (x_test, y_test))

def plot_accuracy(history):
    
    plt.plot(history.history['accuracy'],label='train accuracy')
    plt.plot(history.history['val_accuracy'],label='validation accuracy')
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(loc='best')
    plt.savefig('Accuracy_v1_model_inceptionv3')
    plt.show()
    
def plot_loss(history):
    
    plt.plot(history.history['loss'],label="train loss")
    plt.plot(history.history['val_loss'],label="validation loss")
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(loc='best')
    plt.savefig('Loss_v1_model_inceptionv3')
    plt.show()
    
plot_accuracy(model_fit)
plot_loss(model_fit)




predict_x = model.predict(x_test) 
classes_x = np.argmax(predict_x,axis=1)
#y_pred_class = model.predict_classes(x_test)

y_pred = model.predict(x_test)
y_test_class = np.argmax(y_test, axis=1)
confusion_matrix = confusion_matrix(y_test_class, classes_x)

#print(classification_report(y_test_class, classes_x))

report = classification_report(y_test_class, classes_x, output_dict=True, zero_division=0)
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



#print(type(confusion_matrix(y_test_class, classes_x)))
#print(y_test_class)
#print(y_test)
#print(len(y_test_class))

dict_activity = dict(enumerate(df_new['activity'].cat.categories))
df_new['activity_code'] = df_new['activity'].cat.codes
print(df_new['activity_code'])
print(dict_activity)
df_new['activity_reversed'] = df_new['activity_code'].map(dict_activity)
df_y_test_class = pd.DataFrame(y_test_class, columns = ['activity_class'])
df_y_test_class['activity_class_reversed'] = df_y_test_class['activity_class'].map(dict_activity)
print(df_y_test_class)

#cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
#cm_display.plot()
#plt.show()

#import seaborn as sns
#sns.heatmap(confusion_matrix,figsize=(200,200), annot=True)

# Commented out IPython magic to ensure Python compatibility.
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline


df_cm = pd.DataFrame(confusion_matrix(y_test_class, classes_x), columns=np.unique(y_test_class), index=np.unique(y_test_class))
df_cm.index.name = 'Actual'
df_cm.columns.name = 'Predicted'


f, ax = plt.subplots(figsize=(500, 500))
cmap = sns.cubehelix_palette(light=1, as_cmap=True)

sns.heatmap(df_cm, cbar=False, annot=True, cmap=cmap, square=True, fmt='.0f',
            annot_kws={'size': 10})
plt.title('Actuals vs Predicted')
plt.show()