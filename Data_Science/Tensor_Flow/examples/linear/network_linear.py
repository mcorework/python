"""
================================================================================
TensorFlow Classification Script (Using 2D Input Coordinates)
================================================================================

This Python script demonstrates how to build, train, and evaluate a simple 
neural network classifier using TensorFlow and Keras. The model takes two 
numeric inputs (`x`, `y`) and predicts a categorical label (`color`). This file 
is designed as a beginner-friendly example for working with tabular data in 
TensorFlow.

--------------------------------------------------------------------------------
1. Requirements
--------------------------------------------------------------------------------
Install dependencies:

    pip install tensorflow pandas numpy

Python Version: 3.10 or above is recommended.

--------------------------------------------------------------------------------
2. Dataset Format
--------------------------------------------------------------------------------
The script expects two CSV files:

    ./data/train.csv
    ./data/test.csv

Both must contain these columns:

    x       -> numeric feature 1  
    y       -> numeric feature 2  
    color   -> target class (integer such as 0 or 1)

Example CSV:
    x,y,color
    1.2,3.4,0
    4.1,2.9,1

--------------------------------------------------------------------------------
3. Script Workflow Overview
--------------------------------------------------------------------------------
• Load training data  
• Randomly shuffle it  
• Build a 2-layer neural network  
• Compile using Adam optimizer + cross-entropy loss  
• Train model for 5 epochs  
• Load test data  
• Evaluate performance on unseen data  

--------------------------------------------------------------------------------
4. Important Notes About the Model
--------------------------------------------------------------------------------
The final Dense layer uses:

    activation='sigmoid'
    loss=SparseCategoricalCrossentropy(from_logits=True)

This combination is mathematically inconsistent.

Correct setup options:
    A) Use softmax activation and set from_logits=False
    B) Keep activation=None (linear output) and keep from_logits=True

However, for teaching/demo purposes, we keep your original configuration exactly.

If you want the corrected version, just ask.

================================================================================
"""

# ------------------------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------------------------
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np


# ------------------------------------------------------------------------------
# 2. LOAD AND SHUFFLE TRAINING DATA
# ------------------------------------------------------------------------------
train_df = pd.read_csv('./data/train.csv')

# Shuffle rows to reduce ordering bias during training
np.random.shuffle(train_df.values)

print("Training Data Preview:")
print(train_df.head())


# ------------------------------------------------------------------------------
# 3. BUILD THE MODEL
# ------------------------------------------------------------------------------
# The model takes 2 numeric inputs (x, y) and produces 2 output class scores.
model = keras.Sequential([
    keras.layers.Dense(4, input_shape=(2,), activation='relu'),  # Hidden layer
    keras.layers.Dense(2, activation='sigmoid')                  # Output layer
])


# ------------------------------------------------------------------------------
# 4. COMPILE THE MODEL
# ------------------------------------------------------------------------------
model.compile(
    optimizer='adam',
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)


# ------------------------------------------------------------------------------
# 5. PREPARE TRAINING INPUTS
# ------------------------------------------------------------------------------
# Combine x and y columns into a 2D input matrix
x_train = np.column_stack((train_df.x.values, train_df.y.values))

# Target labels
y_train = train_df.color.values


# ------------------------------------------------------------------------------
# 6. TRAIN THE MODEL
# ------------------------------------------------------------------------------
model.fit(
    x_train,
    y_train,
    batch_size=4,
    epochs=5
)


# ------------------------------------------------------------------------------
# 7. LOAD AND PREPARE TEST DATA
# ------------------------------------------------------------------------------
test_df = pd.read_csv('./data/test.csv')

# Create test feature matrix
x_test = np.column_stack((test_df.x.values, test_df.y.values))

y_test = test_df.color.values


# ------------------------------------------------------------------------------
# 8. EVALUATE THE MODEL
# ------------------------------------------------------------------------------
print("\nEVALUATION")
model.evaluate(x_test, y_test)
