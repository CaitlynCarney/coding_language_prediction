import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix
# import modeling clasiifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier

import nltk
import unicodedata
import re
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Splitting

# We'll use this split function later to create in-sample and out-of-sample datasets for modeling
def split(df, stratify_by=None):
    """
    3 way split for train, validate, and test datasets
    To stratify, send in a column name
    """
    # split into train and test
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
    # split to vlaidate
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    # return train, validate, and test
    return train, validate, test

def split_top_4(dw):
    '''create the top 4 most used languages
    split these into train test and validate'''
    # create top 4
    top_4_characters = dw.language.value_counts().index[0:4]
    top_4 = dw[dw.language.isin(top_4_characters)]
    # split into train, validate, test
    train, validate, test = split(top_4, 'language')
    return train, validate, test

def split_into_x_y(train, validate, test):
    '''seperates train, validate, and test
    into X and y variables'''
    # Setup our X variables
    X_train = train.all_clean_lemma
    X_validate = validate.all_clean_lemma
    X_test = test.all_clean_lemma
    # set up our y variables
    y_train = train.language
    y_validate = validate.language
    y_test = test.language
    # return them
    return X_train, X_validate, X_test, y_train, y_validate, y_test

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Vectorize
def vectorize_training(X_train, X_validate, X_test):
    # Create the tfidf vectorizer object
    tfidf = TfidfVectorizer()
    # Fit on the training data
    tfidf.fit(X_train)
    # the the training data
    X_train_vectorized = tfidf.transform(X_train)
    X_validate_vectorized = tfidf.transform(X_validate)
    X_test_vectorized = tfidf.transform(X_test)
    # return them
    return X_train_vectorized, X_validate_vectorized, X_test_vectorized

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Logistic Regression Model

def logistic_regression(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    lm = LogisticRegression(random_state=123)
    # Fit a model using only these specified features
    lm.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = lm.predict(X_train_vectorized)
    validate["predicted"] = lm.predict(X_validate_vectorized)
    test['predicted'] = lm.predict(X_test_vectorized)
    # Train Accuracy
    train = (train.actual == train.predicted).mean()
    # Validate Accuracy
    validate = (validate.actual == validate.predicted).mean()
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Balanced Logistic Regression Model

def balanced_log_regression(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    lm2 = LogisticRegression(random_state=123, class_weight='balanced')
    # Fit a model using only these specified features
    lm2.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = lm2.predict(X_train_vectorized)
    validate["predicted"] = lm2.predict(X_validate_vectorized)
    test['predicted'] = lm2.predict(X_test_vectorized)
    # Train Accuracy
    train = lm2.score(X_train_vectorized, y_train)
    # Validate Accuracy
    validate = lm2.score(X_validate_vectorized, y_validate)
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# KNN Model

def knn_model(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    knn = KNeighborsClassifier()
    # Fit a model using only these specified features
    knn.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = knn.predict(X_train_vectorized)
    validate["predicted"] = knn.predict(X_validate_vectorized)
    test['predicted'] = knn.predict(X_test_vectorized)
    # train accuracy
    train = knn.score(X_train_vectorized, y_train)
    # validate accuracy
    validate = knn.score(X_validate_vectorized, y_validate)
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Decision Tree Model

def decision_tree_model(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    clf1 = DecisionTreeClassifier(max_depth=3)
    # Fit a model using only these specified features
    clf1.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = clf1.predict(X_train_vectorized)
    validate["predicted"] = clf1.predict(X_validate_vectorized)
    test['predicted'] = clf1.predict(X_test_vectorized)
    # train accuracy
    train = clf1.score(X_train_vectorized, y_train)
    # validate accuracy
    validate = clf1.score(X_validate_vectorized, y_validate)
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Random Forest Model

def random_forest_model(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    rf = RandomForestClassifier(bootstrap=True, 
                                class_weight=None, 
                                criterion='gini',
                                min_samples_leaf=3,
                                n_estimators=100,
                                max_depth=3, 
                                random_state=123)
    # Fit a model using only these specified features
    rf.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = rf.predict(X_train_vectorized)
    validate["predicted"] = rf.predict(X_validate_vectorized)
    test['predicted'] = rf.predict(X_test_vectorized)
    # train accuracy
    train = rf.score(X_train_vectorized, y_train)
    # validate_accuracy
    validate = rf.score(X_validate_vectorized, y_validate)
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Ridge Classisfier Model

def ridge_class_model(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    clf2 = DecisionTreeClassifier(max_depth=3)
    # Fit a model using only these specified features
    clf2.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = clf2.predict(X_train_vectorized)
    validate["predicted"] = clf2.predict(X_validate_vectorized)
    test['predicted'] = clf2.predict(X_test_vectorized)
    # train accuracy
    train = clf2.score(X_train_vectorized, y_train)
    # validate accuracy
    validate = clf2.score(X_validate_vectorized, y_validate)
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SGD Classifier Model

def sgd_class_model(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    clf3 = SGDClassifier(max_iter=1000, tol=1e-3, random_state=123)
    # Fit a model using only these specified features
    clf3.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = clf3.predict(X_train_vectorized)
    validate["predicted"] = clf3.predict(X_validate_vectorized)
    test['predicted'] = clf3.predict(X_test_vectorized)
    # train accuracy
    train = clf3.score(X_train_vectorized, y_train)
    # validate accuracy
    validate = clf3.score(X_validate_vectorized, y_validate)
    print(f"The accuracy on the train data set is: \n", round(train,3))
    print(f"The accuracy on the validate data set is: \n", round(validate,3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Best and Final Model

def sgd_best_model(y_train, y_validate, y_test, X_train_vectorized, X_validate_vectorized, X_test_vectorized):
    '''makes the model
    fit the model
    make actual and predicted outcomes
    test accuracy on train and validate
    return the accuracy readings'''
    clf3 = SGDClassifier(max_iter=1000, tol=1e-3, random_state=123)
    # Fit a model using only these specified features
    clf3.fit(X_train_vectorized, y_train)
    # make the actual outcomes
    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    # make your predictions
    train['predicted'] = clf3.predict(X_train_vectorized)
    validate["predicted"] = clf3.predict(X_validate_vectorized)
    test['predicted'] = clf3.predict(X_test_vectorized)
    # train accuracy
    train = clf3.score(X_train_vectorized, y_train)
    # validate accuracy
    validate = clf3.score(X_validate_vectorized, y_validate)
    # test accuracy
    test = clf3.score(X_test_vectorized, y_test)
    print(f"SGDClassifier Model Train: \n", round(train,3))
    print(f"SGDClassifier Model Validate: \n", round(validate,3))
    print(f"SGDClassifier Model Test: \n", round(test,3))
