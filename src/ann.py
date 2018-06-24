import numpy as np
import matplotlib.pyplot as plt
import json
import pickle

seed = 499
np.random.seed(seed=seed)

from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
from keras.optimizers import RMSprop as rm
from keras.optimizers import Adagrad as ada
from keras.optimizers import SGD as sgd
from keras import initializers, regularizers

mean = 0
std = 0

min_values = 0
max_values = 0

dataset = np.genfromtxt('full_final.csv', delimiter=',')

# min-max scaling
def min_max_scaling(data):
    global min_values
    global max_values
    min_values = np.amin(data, axis=0)
    max_values = np.amax(data, axis=0)
    return (data-min_values)/(max_values-min_values)

# normalizing
def normalize(data):
    global mean
    global std
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean)/std

dataset[:,:34] = normalize(dataset[:,:34])

# shuffled the dataset
np.random.seed(seed)
np.random.shuffle(dataset)

# Split the dataset into train and test parts
size_100 = dataset.shape[0]
size_80 = int(size_100*0.8)

x_train = dataset[:size_80, :34]
x_test = dataset[size_80:, :34]

y_train = dataset[:size_80, 34:]
y_test = dataset[size_80:, 34:]

batch_size = 32
epochs = 1000

model = Sequential()
model.add(Dense(34,
                input_dim=34,
                bias_initializer=initializers.Constant(0.01),
                bias_regularizer=regularizers.l2(0.01),
                kernel_initializer=initializers.he_normal(seed=seed),
                kernel_regularizer=regularizers.l2(0.01),
                activation='relu'))
model.add(BatchNormalization())
#model.add(Dropout(0.2))
model.add(Dense(17,
                bias_initializer=initializers.Constant(0.01),
                bias_regularizer=regularizers.l2(0.01),
                kernel_initializer=initializers.he_normal(seed=seed),
                kernel_regularizer=regularizers.l2(0.01),
                activation='relu'))
model.add(BatchNormalization())
#model.add(Dropout(0.2))
model.add(Dense(9,
                bias_initializer=initializers.Constant(0.01),
                bias_regularizer=regularizers.l2(0.01),
                kernel_initializer=initializers.he_normal(seed=seed),
                kernel_regularizer=regularizers.l2(0.01),
                activation='relu'))
model.add(BatchNormalization())
#model.add(Dropout(0.2))
model.add(Dense(8,
                bias_initializer=initializers.Constant(0.01),
                bias_regularizer=regularizers.l2(0.01),
                kernel_initializer=initializers.he_normal(seed=seed),
                kernel_regularizer=regularizers.l2(0.01),
                activation='relu'))
model.add(BatchNormalization())
#model.add(Dropout(0.2))
model.add(Dense(3,
                bias_initializer=initializers.Constant(0.01),
                bias_regularizer=regularizers.l2(0.01),
                kernel_initializer=initializers.he_normal(seed=seed),
                kernel_regularizer=regularizers.l2(0.01),
                activation='softmax'))

#opt = rm()
#opt = ada()
opt = sgd(lr=1e-4, momentum=0.9, decay=1e-5, nesterov=True)

model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

history = model.fit(x=x_train, y=y_train, batch_size=batch_size, epochs=epochs, verbose=2, callbacks=None,
                    validation_split=0.2, validation_data=None, shuffle=True, class_weight=None,
                    sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None)

# make predictions
score = model.evaluate(x_test, y_test, batch_size=batch_size)
print(model.metrics_names)
print(score)

# list all data in history
print(history.history.keys())

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='lower right')
plt.savefig('accuracy.png')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.savefig('loss.png')
plt.show()

model.save('model/model.h5')
model.save_weights('model/model_weight.h5')
json_data = model.to_json()

with open('model/json_data.txt', 'w') as outfile:
    json.dump(json_data, outfile)

with open('model/mean_std.pkl', 'wb') as file:
    pickle.dump((mean, std), file, pickle.HIGHEST_PROTOCOL)