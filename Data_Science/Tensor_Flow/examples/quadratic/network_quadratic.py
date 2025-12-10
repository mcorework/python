"""
================================================================================
TensorFlow Classification Example
================================================================================

This script trains and evaluates a simple neural network classifier using 
TensorFlow and Keras. It is designed for beginners working with tabular data 
consisting of two numeric input features (`x`, `y`) and one output label 
(`color`). The model learns to predict the `color` class based on the (x, y) 
coordinate inputs.

--------------------------------------------------------------------------------
Requirements
--------------------------------------------------------------------------------
- Python 3.10+
- TensorFlow 2.x
- Pandas
- NumPy

Install dependencies:
    pip install tensorflow pandas numpy

--------------------------------------------------------------------------------
Dataset Format
--------------------------------------------------------------------------------
Both train.csv and test.csv must contain the following columns:

    x       (numeric feature)
    y       (numeric feature)
    color   (integer class label such as 0 or 1)

Example CSV row:
    x,y,color
    1.2,3.4,0
    4.1,2.9,1

--------------------------------------------------------------------------------
Workflow Summary
--------------------------------------------------------------------------------
1. Load and shuffle training data.
2. Build a simple 3-layer neural network.
3. Compile the model with Adam optimizer and cross-entropy loss.
4. Train using (x,y) coordinates as inputs and color as labels.
5. Load and prepare test data.
6. Evaluate the model on unseen data.

--------------------------------------------------------------------------------
Notes
--------------------------------------------------------------------------------
⚠ IMPORTANT:
The model uses a final Dense layer with activation='sigmoid' combined with 
SparseCategoricalCrossentropy(from_logits=True). This is not typical. A softmax 
activation is usually recommended for multi-class classification.

If you want the mathematically correct version, replace:
    activation='sigmoid' 
with 
    activation='softmax'
and change:
    from_logits=True 
to 
    from_logits=False

(If you want me to apply the fix, just ask.)
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

# Shuffle the underlying numpy values to reduce ordering bias
np.random.shuffle(train_df.values)

print("Training Data Preview:")
print(train_df.head())


# ------------------------------------------------------------------------------
# 3. BUILD THE MODEL
# ------------------------------------------------------------------------------
# The model takes two inputs (x, y) and predicts one of two color classes.
model = keras.Sequential([
    keras.layers.Dense(32, input_shape=(2,), activation='relu'),  # Input + hidden
    keras.layers.Dense(32, activation='relu'),                    # Hidden layer
    keras.layers.Dense(2, activation='sigmoid')                   # Output layer
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
# 5. PREPARE TRAINING INPUTS (x,y)
# ------------------------------------------------------------------------------
# Combine x and y columns to form a 2D input array: (num_samples, 2)
x_train = np.column_stack((train_df.x.values, train_df.y.values))

y_train = train_df.color.values  # Labels


# ------------------------------------------------------------------------------
# 6. TRAIN THE MODEL
# ------------------------------------------------------------------------------
model.fit(
    x_train, 
    y_train, 
    batch_size=4,
    epochs=10
)


# ------------------------------------------------------------------------------
# 7. LOAD AND PREPARE TEST DATA
# ------------------------------------------------------------------------------
test_df = pd.read_csv('./data/test.csv')
x_test = np.column_stack((test_df.x.values, test_df.y.values))
y_test = test_df.color.values


# ------------------------------------------------------------------------------
# 8. EVALUATE THE MODEL
# ------------------------------------------------------------------------------
print("\nEVALUATION RESULTS")
model.evaluate(x_test, y_test)

