"""

===============================================================================
                           TensorFlow - Documentation
===============================================================================

1. Introduction

This Python file serves as the foundation for building and running TensorFlow-based machine learning 
and deep learning programs. It provides configurations, helper functions, and reusable code to streamline 
model development, training, evaluation, and deployment.

KERAS is a high-level deep learning library built on top of TensorFlow.
It allows developers to build, train, and evaluate neural networks with simple, readable, and modular code.

TensorFlow is a powerful open-source platform widely used for:
    - Neural networks (CNN, RNN, Transformers)
    - Image classification
    - Natural language processing (NLP)
    - Time-series forecasting
    - Reinforcement learning

2. Installing TensorFlow
    pip install tensorflow

3. Recommended Structure for TensorFlow Projects
    project/
    │── data/               # Training/validation datasets
    │── models/             # Saved models (.keras / .h5)
    │── utils/              # Helper scripts
    │── train.py            # Training script
    │── evaluate.py         # Testing/metrics
    │── config.py           # Global configuration
    │── main.py             # Main entry point

===============================================================================
                           Neural Networks - Documentation
===============================================================================    
1. What Is a Neural Network?

    A Neural Network (NN) is a computational model inspired by the structure of the human brain.
    It consists of layers of interconnected nodes (“neurons”) that learn patterns from data.
    
2. Basic Structure of a Neural Network

    A neural network usually has three types of layers:
    1. Input Layer
    2. Hidden Layers
    3. Output Layer

3. How Neural Networks Work (Simplified)
    Each neuron performs:
    weighted_sum = w1*x1 + w2*x2 + ... + b
    output = activation(weighted_sum)    

    Key components:
    Weights (w) → learned parameters
    Bias (b) → adjustment term
    Activation Function → introduces non-linearity

4. Types of Neural Networks
    1. Feedforward Neural Network (FNN)
    2. Convolutional Neural Network (CNN)
    3. Recurrent Neural Network (RNN)
    4. LSTM/GRU Networks
    5. Transformer Networks
    6. Autoencoders

6. Training a Neural Network
    Training involves:
    1.  Forward Pass: compute outputs
    2.  Compute Loss: measure error
    3.  Backward Pass: compute gradients

### Links
[TensorFlow Video - Keith Galli](https://www.youtube.com/watch?v=aBIGJeHRZLQ&t=14s)
[TensorFlow Github - Keith Galli](https://github.com/KeithGalli/neural-nets)
[Neural Network Video - 3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk&t=15s)


"""


import tensorflow as tf
from tensorflow import keras

import pandas as pd
import numpy as np

train_df = pd.read_csv('./examples/linear/data/train.csv')
np.random.shuffle(train_df.values)

print(train_df.head())

model = keras.Sequential([
	keras.layers.Dense(4, input_shape=(2,), activation='relu'),
	keras.layers.Dense(2, activation='sigmoid')])

model.compile(optimizer='adam', 
	          loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
	          metrics=['accuracy'])

x = np.column_stack((train_df.x.values, train_df.y.values))

model.fit(x, train_df.color.values, batch_size=4, epochs=5)

test_df = pd.read_csv('./examples/linear/data/test.csv')
test_x = np.column_stack((test_df.x.values, test_df.y.values))

print("EVALUATION")
model.evaluate(test_x, test_df.color.values)
