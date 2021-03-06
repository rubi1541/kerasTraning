from keras import metrics
from keras import losses
from keras import optimizers
from keras import layers
from keras import models
import numpy as np
from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=1000)


def vectorize_sequences(sequences, dimention=1000):
    results = np.zeros((len(sequences), dimention))
    for i, sequence in enumerate(sequences):
        # numpy 만 가능
        results[i, sequence] = 1.

    return results


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(1000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


model.compile(optimizer=optimizers.RMSprop(lr=0.001), loss=losses.binary_crossentropy,metrics=[metrics.binary_accuracy])

x_val = x_train[:1000]
partial_x_train = x_train[1000:]
y_val = y_train[:1000]
partial_y_train = y_train[1000:]


history = model.fit(partial_x_train, partial_y_train, epochs=4, batch_size=256, validation_data=(x_val, y_val))



import matplotlib.pyplot as plt

history_dict = history.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(loss) +1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')

plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')

plt.legend()

plt.savefig('aaa.png')




results = model.evaluate(x_test, y_test)
print(results)