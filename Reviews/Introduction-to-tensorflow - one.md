# Introduction to tensorflow -- one

Yesterday, I came across a course on coursera. It is [Introduction to tensorflow](https://www.coursera.org/learn/introduction-tensorflow). I heard about it several years ago and I thought it is very complex so I didn't pay much attention to it. But the course is only 4weeks long and taught by a famous guy working in Google, and it is free for audit. Why not give it a try this week?

By the end of the course, I hope I will know how to build up a model for training a fish recogisation API.

Here is what I learnt in *Week 1*.

* What is Machine learning? What is the difference between ML and traditional program?

  * Traditional program:

  ``` mermaid
  graph LR
  Rules --> Result
  Data --> Result
  ```

  * ML

  ```mermaid
  graph LR;
  Result --> Rules
  Data --> Rules
  ```

* How to use tensorflow library

  ```python
  import tensorflow as tf
  import numpy as np
  from tensorflow import keras
  model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
  model.compile(optimizer='sgd', loss='mean_squared_error')
  xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
  ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)
  model.fit(xs, ys, epochs=500)
  print(model.predict([7.0]))
  ```

  The code above looks quite easy to understand if you know the meaning of some keywords:

  * Dense : The layer of connected neorons
  * loss : the function measure how good the current guess is
  * optimizer : generate a new and improved guess
  * model.fit : train the neural network
