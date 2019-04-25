# Intruduction-to-tensorflow - two

Continue to learn the course of tensorflow. In this class, there is a new test/validate dataset is included. The dataset is called 'Fasion MNIST'. There are 70K 28*28 grey images in the dataset. The images are labelled as 10 different types. 

The code of training dataset is as below:

``` python
import tensorflow as tf
print(tf.__version__)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')<0.4):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images/255.0
test_images=test_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
```

Some highlights of the code:

* *Flatten* has to be the first layer in DNN. It transform the 28*28 pixels into a 724 array.
* The first *Dense* layer is the *hidden* layer in DNN. 512 is an exprience number. You can try to change it to other values like 1024 and check the result. In this dataset, 1024 will increase the training time and the performance of the model as well. But in some other cases, it maybe not.
* callbacks : the function is called after each epoch finishes. You can use it to terminate the training in the middle.

Think about what does normalization use for?

```python
training_images=training_images/255.0
test_images=test_images/255.0
```