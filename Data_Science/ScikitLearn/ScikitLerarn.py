"""

===============================================================================
                           Scikit-Learn Documentation
===============================================================================

Overview
--------
Scikit-Learn (sklearn) is a widely used Python machine learning library that 
provides efficient tools for data analysis, data preprocessing, model training, 
and evaluation. It is built on top of NumPy, SciPy, and Matplotlib, and offers 
a consistent API for classical machine learning tasks.

Scikit-Learn is commonly used for:
- Supervised learning (classification, regression)
- Unsupervised learning (clustering, dimensionality reduction)
- Data preprocessing and feature engineering
- Train/test splitting and model selection
- Hyperparameter tuning using cross-validation
- Building ML workflows using Pipelines


Key Modules
-----------
1. sklearn.preprocessing
   - StandardScaler: Standardizes features (mean=0, std=1)
   - MinMaxScaler: Normalizes features to a given range
   - LabelEncoder: Encodes labels as integers
   - OneHotEncoder: Encodes categorical variables into one-hot vectors

2. sklearn.model_selection
   - train_test_split: Splits dataset into training and testing
   - GridSearchCV: Exhaustive hyperparameter search
   - RandomizedSearchCV: Faster random search for hyperparameters
   - cross_val_score: Cross-validation scoring helper

3. Supervised Learning Algorithms
   Classification:
     * LogisticRegression
     * RandomForestClassifier
     * SVC (Support Vector Machine)
     * KNeighborsClassifier
     * GradientBoostingClassifier

   Regression:
     * LinearRegression
     * RandomForestRegressor
     * Ridge / Lasso Regression
     * SVR (Support Vector Regression)

4. Unsupervised Learning Algorithms
   - KMeans (clustering)
   - PCA (dimensionality reduction)
   - DBSCAN
   - AgglomerativeClustering (hierarchical clustering)

5. Pipelines
   Pipelines allow chaining preprocessing steps and models into one workflow.
   Example:
       Pipeline([
           ('scaler', StandardScaler()),
           ('model', LogisticRegression())
       ])


Common Scikit-Learn Workflow
----------------------------
1. Import the necessary modules
   from sklearn.model_selection import train_test_split
   from sklearn.preprocessing import StandardScaler
   from sklearn.linear_model import LogisticRegression

2. Split data into training and testing
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

3. Preprocess data using scalers or encoders
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)
   X_test_scaled = scaler.transform(X_test)

4. Train the model
   model = LogisticRegression()
   model.fit(X_train_scaled, y_train)

5. Make predictions and evaluate
   predictions = model.predict(X_test_scaled)

   from sklearn.metrics import accuracy_score
   accuracy = accuracy_score(y_test, predictions)


Pipeline Example (Recommended)
------------------------------
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

pipeline.fit(X_train, y_train)
score = pipeline.score(X_test, y_test)


Advantages
----------
- Simple and consistent API
- Wide range of ML algorithms
- Built-in tools for preprocessing and model tuning
- Excellent documentation and community support
- Integrates well with NumPy, pandas, and matplotlib


Limitations
-----------
Scikit-Learn is NOT designed for:
- Deep learning (use PyTorch or TensorFlow)
- Large-scale distributed training
- Very large datasets that do not fit into memory
- Building or training LLMs

Miscellaneous
--------------
a. Traditional, Algorithmic Models - Sci-Kit Learn
b. Nural Network Models - Tensorflow, Pytorch


### Links
[SciKit Learn Video - Keith Galli](https://www.youtube.com/watch?v=M9Itm95JzL0)
[SciKit Learn Github - Keith Galli](https://github.com/keithgalli/sklearn)
[SciKit Learn Tutorials and Documentations](https://scikit-learn.org/stable/index.html)



===============================================================================
"""

import json
import random


# ===============================================================================
# 📌 Sentiment & Review Classes
# ===============================================================================

class Sentiment:
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    POSITIVE = "POSITIVE"

class Review:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()
        
    def get_sentiment(self):
        if self.score <= 2:
            return Sentiment.NEGATIVE
        elif self.score == 3:
            return Sentiment.NEUTRAL
        else: #Score of 4 or 5
            return Sentiment.POSITIVE
        
class ReviewContainer:
    def __init__(self, reviews):
        self.reviews = reviews
        
    def get_text(self):
        return [x.text for x in self.reviews]
    
    def get_sentiment(self):
        return [x.sentiment for x in self.reviews]
        
    def evenly_distribute(self):
        negative = list(filter(lambda x: x.sentiment == Sentiment.NEGATIVE, self.reviews))
        positive = list(filter(lambda x: x.sentiment == Sentiment.POSITIVE, self.reviews))
        positive_shrunk = positive[:len(negative)]
        self.reviews = negative + positive_shrunk
        random.shuffle(self.reviews)        

# -----------------------------------------------------------------------------------
# ⚙️ 1. Load Data
# -----------------------------------------------------------------------------------

file_name = 'Books_small'
reviews = []
with open(f'./data/sentiment/{file_name}.json') as f:
   for line in f:
      review = json.loads(line)
      reviews.append((Review(review['reviewText'], review['overall'])))
#print(reviews[5].sentiment)
#print(len(reviews))

# -----------------------------------------------------------------------------------
# ⚙️ 2. Prep Data
# -----------------------------------------------------------------------------------

# SkLearn traning and test data link (split 1000 reviews in training and test set )
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html 
# Sklearn - bags of words - counter vactorizer
# pip install scikit-learn

from sklearn.model_selection import train_test_split

training, test = train_test_split(reviews, test_size=0.33, random_state=42)

train_x = [x.text for x in training]
train_y = [x.sentiment for x in training]

test_x = [x.text for x in test]
test_y = [x.sentiment for x in test]

train_container = ReviewContainer(training)
test_container = ReviewContainer(test)

train_container.evenly_distribute()
train_x = train_container.get_text()
train_y = train_container.get_sentiment()

test_container.evenly_distribute()
test_x = test_container.get_text()
test_y = test_container.get_sentiment()

#print(train_y.count(Sentiment.POSITIVE))
#print(train_y.count(Sentiment.NEGATIVE))


# -----------------------------------------------------------------------------------
# ⚙️ 3. Bag of words vactorization
# -----------------------------------------------------------------------------------
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

"""
In scikit-learn, a vectorizer converts text into numerical vectors so machine-learning models can understand it.
Models cannot work directly with raw strings — they need numbers. A vectorizer transforms sentences, documents, 
or tokens into fixed-size numeric feature arrays.

A vectorizer:
Reads text
Builds a vocabulary of unique words (or tokens)
Converts each document into a numeric vector based on:
word counts (CountVectorizer)
word importance (TfidfVectorizer)

The resulting numeric vectors can be used in ML models like logistic regression, SVM, Naive Bayes, etc.

from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()
array(['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third',
       'this'], ...)
print(X.toarray())
[[0 1 1 1 0 0 1 0 1]
 [0 2 0 1 0 1 1 0 1]
 [1 0 0 1 1 0 1 1 1]
 [0 1 1 1 0 0 1 0 1]]
vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
X2 = vectorizer2.fit_transform(corpus)
vectorizer2.get_feature_names_out()
array(['and this', 'document is', 'first document', 'is the', 'is this',
       'second document', 'the first', 'the second', 'the third', 'third one',
       'this document', 'this is', 'this the'], ...)
 >>> print(X2.toarray())
 [[0 0 1 1 0 0 1 0 0 0 0 1 0]
 [0 1 0 1 0 1 0 1 0 0 1 0 0]
 [1 0 0 1 0 0 0 0 1 1 0 1 0]
 [0 0 1 0 1 0 1 0 0 0 0 0 1]]
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
vectorizer = CountVectorizer()

# One step (It both fits and transforms both in one funciton)
# train has to be trained and transformed for the model
train_x_vectors = vectorizer.fit_transform(train_x)

# For test data, we do not a model, we just need to test it.
test_x_vectors = vectorizer.transform(test_x)

print(train_x[0])
print(train_x_vectors[0])


# -----------------------------------------------------------------------------------
# ⚙️ 4. Classification
# -----------------------------------------------------------------------------------

# Classification comparision
# https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html