from __future__ import print_function
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop as rm
from keras.optimizers import Adagrad as ada
from keras import regularizers as rg
from keras.models import load_model
from keras.models import model_from_json
import json

dataset = np.genfromtxt('full_final.csv', delimiter=',')

# shuffled the dataset
np.random.shuffle(dataset)

dataset[:,:18] = 1/(dataset[:,:18])

# normalize min-max scaling
def normalize(data):
    min_values = np.amin(data, axis=0)
    max_values = np.amax(data, axis=0)
    return (data-min_values)/(max_values-min_values)

dataset[:,:34] = normalize(dataset[:,:34])

# Split the dataset into train and test parts
x_train = dataset[:10077, :34]
x_validation = dataset[10077:13436, :34]
x_test = dataset[13436:, :34]

y_train = dataset[:10077, 34:]
y_validation = dataset[10077:13436, 34:]
y_test = dataset[13436:, 34:]

batch_size = 1000
epochs = 70

model = Sequential()
model.add(Dense(2000, kernel_regularizer=rg.l2(0.01), input_shape=(34,), activation='relu'))
model.add(Dense(2000, activation='relu'))
model.add(Dense(2000, activation='relu'))
model.add(Dense(2000, activation='relu'))
model.add(Dense(2000, activation='relu'))
model.add(Dense(3, activation='softmax'))

opt = rm(lr=0.001, rho=0.9, decay=0.005)
#opt = ada(lr=0.001, decay=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            verbose=2,
            shuffle=False,
            validation_data=(x_validation, y_validation))

# make predictions
testPredict = model.predict(x_test, batch_size=batch_size)

# list all data in history
print(history.history.keys())

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='lower right')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.show()

# accuracy for test
truePrediction = 0
testPredictIndices = np.argmax(testPredict, axis=1)
testActualIndices = np.argmax(y_test, axis=1)

for i in range(len(testPredict)):
    if(testPredictIndices[i] == testActualIndices[i]):
        truePrediction = truePrediction + 1

print ('true prediction number: ' + str(truePrediction))
print ('test accuracy: ' + str((truePrediction/len(y_test))*100))

model.save('model.h5')
model.save_weights('model_weight.h5')
json_data = model.to_json()
with open('json_data.txt', 'w') as outfile:
    json.dump(json_data, outfile)