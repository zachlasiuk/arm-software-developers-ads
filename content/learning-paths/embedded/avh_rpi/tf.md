---
# User change
title: "Tensorflow"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## TensorFlow for machine learning	
				
To see if TensorFlow can run on both the real Raspberry Pi 4 and the virtual Raspberry Pi 4 install it using:
		
If pip is not installed, it can be installed with:

```bash
sudo apt install python3-pip
```

Next, install TensorFlow. 

```bash			
pip install tensorflow-aarch64 tensorflow_io 
```
				
Run a [TensorFlow quickstart example](https://www.tensorflow.org/tutorials/quickstart/beginner) by following the instructions on both versions of the Raspberry Pi and compare the systems.

The results below show the virtual Raspberry Pi 4 runs much faster than the physical board.

| System | Time to complete              |
|--------|------------------------------:|				
| Physical Raspberry Pi 4 | 1 min 9 sec	|	
| Virtual Raspberry Pi 4  | 22 sec      |

## Summary 

Both systems produced the same results, and the virtual Pi is significantly faster.


## Quickstart example

To save time of entering all of the commands from the TensorFlow example, the code is shared here. Save it in a file named example.py.

```bash
python ./example.py
```

Here is the example code:

```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

probability_model(x_test[:5])

```
