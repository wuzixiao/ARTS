# Introduction to tensorflow -- three

In this part, he introduced a very important concept for computer vision. It is called *Convolution*. You must have used it before if you used any camera app to add a fitler on top of image.

The idea behind *convolution* is using a filter matrix to multiple the original matrix. There is more information on this [wiki](https://en.wikipedia.org/wiki/Kernel_(image_processing)) page. 

```python
import tensorflow as tf
print(tf.__version__)
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images.reshape(60000, 28, 28, 1)
training_images=training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images=test_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(training_images, training_labels, epochs=5)
test_loss = model.evaluate(test_images, test_labels)
```

Some highlights of the code:

* tensorflow use function *Conv2D* to transform the image. In this case, it only uses 'relu' activation funciton to filte the image in order to highlight the features we need for training.
* *MaxPooling2D* is used for compressing. 