# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:45:30 2021

@author: enzoa
"""
import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt

DATASET_PATH = "data_10.json"


def load_data(dataset_path):
    with open(dataset_path, "r") as fp:
        data = json.load(fp)

    # convert lists into numpy arrays
    #mapping = np.array(data['mapping'])
    inputs = np.array(data["mfcc"])
    targets = np.array(data['labels'])
    
    return inputs, targets


def plot_history(history):
    
    fig, axs = plt.subplots(2)
    
    # create accuracy subplot
    axs[0].plot(history.history["accuracy"], label="train accuracy")
    axs[0].plot(history.history["val_accuracy"], label="validation accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy evaluation")
    
    # create error subplot
    axs[1].plot(history.history["loss"], label="train error")
    axs[1].plot(history.history["val_loss"], label="validation error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")    
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error evaluation")    

    plt.show()


def prepare_datasets(test_size, validation_size):
    
    # load data
    X, y = load_data(DATASET_PATH)
    
    # create train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    
    # create train/validation split
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)
    
    # CNN needs 3d array -> (t, n_mfcc, 1) 1 is the channel
    X_train = X_train[..., np.newaxis] # 4d array -> (num_samples, 130, 13, 1)
    X_validation = X_validation[..., np.newaxis] # 4d array -> (num_samples, 130, 13, 1)
    X_test = X_test[..., np.newaxis] # 4d array -> (num_samples, 130, 13, 1)
    
    return X_train, X_validation, X_test, y_train, y_validation, y_test


def  build_model(input_shape):
    
    # create model
    model = keras.Sequential()
            
    # 1st conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization()) # speed the train
    
    # 2nd conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization()) # speed the train
      
    # 3rd conv layer
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization()) # speed the train
      
    # flatten the output and feed it into dense layer
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.3)) # reduce overfitting
    
    # output layer
    model.add(keras.layers.Dense(10, activation='softmax')) # 10 probabilities of genres
    
    return model

def predict(model, X, y):
    
    X = X[np.newaxis, ...] # 3d array -> 4d array (1 sample, t, n_mfcc, 1)
    
    prediction = model.predict(X) # 10d array
    
    # extract index with max probability (value)
    predicted_index = np.argmax(prediction, axis=1) # [index]
    print("Expected index: {}, Predicted index: {}".format(y, predicted_index))


if __name__ == "__main__":
    # load data
    inputs, targets = load_data(DATASET_PATH)

    # split the data into train, validation and test set
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(0.25, 0.2)
        
    # build the network architecture (CNN)
    input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3])
    model = build_model(input_shape)
       
    # compile network
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer,
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    
    model.summary()
    
    # train network
    history = model.fit(X_train, y_train,
              batch_size=32,
              epochs=30,
              validation_data=(X_validation, y_validation))
    
    # plot accuracy and error over the epochs
    plot_history(history)
    
    # evaluate the CNN on the test set
    test_error, test_accuracy = model.evaluate(X_test, y_test, verbose=1)
    print("Accuracy on test set is: {}".format(test_accuracy))
    
    # make prediction on a sample
    X = X_test[100]
    y = y_test[100]
    predict(model, X, y)